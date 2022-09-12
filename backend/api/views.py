from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Application, SkillTag
from .serializers import ApplicationSerializer

# from .serializers import UserSerializerWithToken, UserSerializer


# Create your views here.
@api_view(["POST"])
def createApplication(request):
    data = request.data
    name = data.get("name")
    email = data.get("email")
    collegeName = data.get("collegeName")

    messages = {"errors": []}

    # checking for errors
    if name == None:
        messages["errors"].append("name can't be empty")
    if email == None:
        messages["errors"].append("Email can't be empty")
    if collegeName == None:
        messages["errors"].append("College name can't be empty")

    if Application.objects.filter(email=email).exists():
        messages["errors"].append("Already applied")

    if len(messages["errors"]) > 0:
        return Response(
            {"details": messages["errors"]}, status=status.HTTP_400_BAD_REQUEST
        )

    # If no error in request object
    try:
        application = Application.objects.create(
            name=name, email=email, collegeName=collegeName
        )
        # print('user created')
        serializer = ApplicationSerializer(application, many=False)
        # print(serializer.data)
    except Exception as e:
        print(e)
        return Response({"details": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)


# Get a particular application
@api_view(["GET"])
def getApplicationByEmail(request, email):
    application = Application.objects.get(email=email)

    serializer = ApplicationSerializer(application, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get all application | paginated response
@api_view(["GET"])
def getApplicationByEmail(request, email):
    pageSize = request.query_params.get("pageSize") or 10
    application = Application.objects.get(email=email)

    paginator = PageNumberPagination()
    paginator.page_size = pageSize
    result_page = paginator.paginate_queryset(application, request)
    serializer = ApplicationSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
    # return Response(serializer.data, status=status.HTTP_200_OK)
