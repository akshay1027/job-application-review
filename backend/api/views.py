import uuid
import random
import os.path

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from django.core.files.storage import default_storage

from .models import Application, SkillTag
from .serializers import ApplicationSerializer


# Create new application 
@api_view(["POST"])
def createApplication(request):
    data = request.data
    name = data.get("name")
    email = data.get("email")
    collegeName = data.get("collegeName")
    skills = data.get("skills")

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
        application = Application.objects.create(name=name, email=email, collegeName=collegeName)
        application.skills.set(SkillTag.objects.get_or_create(name=skill)[0] for skill in skills)

        # print('user created')
        serializer = ApplicationSerializer(application, many=False)
        # print(serializer.data)

    except Exception as e:
        print(e)
        return Response({"details": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    response={
        'type': 'Success', 
        'message': 'successfully created your info',
        'results': serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)


# Get an application by email 
@api_view(["GET"])
def getApplicationByID(request):
    try:
        id = request.query_params.get("id")
        application = Application.objects.get(id=id)

        serializer = ApplicationSerializer(application, many=False)
        response={
            'type': 'Success', 
            'results': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get all applications | paginated response 
@api_view(["GET"])
def getAllApplication(request):
    try:
        pageSize = request.query_params.get("pageSize") or 10
        applications = Application.objects.all()

        # pagination
        paginator = PageNumberPagination()
        paginator.page_size = pageSize
        result_page = paginator.paginate_queryset(applications, request)
        serializer = ApplicationSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Search applications with name or email fields | filter | paginated response 
@api_view(["GET"])
def searchApplications(request):
    try:
        pageSize = request.query_params.get("pageSize") or 10
        application = Application.objects.all()
        query = request.query_params.get('q') or ''
        if query:
            queryset_list = application.filter(
                Q(name__icontains=query)
                | Q(email__icontains=query)
            ).distinct()

        # print(queryset_list)

        # pagination
        paginator = PageNumberPagination()
        paginator.page_size = pageSize
        result_page = paginator.paginate_queryset(queryset_list, request)
        serializer = ApplicationSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Search applications by skills | filter | paginated response 
# Note: This is not optimized solution, due to lack of time, came up with my own solution!
@api_view(["GET"])
def searchApplicationsBySkills(request):
    try:
        # pageSize = request.query_params.get("pageSize") or 10
        applications = Application.objects.all()
        query = request.query_params.get('q') or ''
        
        # for applicationObj in applications:
        #     skills = SkillTag.objects.get(id=applicationObj.id)
        #     # skills = Application.objects.get(id=applicationObj.id)
        #     print(skills)
        serializer = ApplicationSerializer(applications, many=True)

        result = []
        for application in serializer.data:
            for skill in application['skills']:
                if query == skill:
                    result.append(application)
                    break

        response={
            'type': 'Success', 
            'results': result
        }

        # return paginator.get_paginated_response(serializer.data)
        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Delete an application by email 
@api_view(["DELETE"])
def deleteApplicationByID(request):
    try:
        id = request.query_params.get("id")
        application = Application.objects.get(id=id)

        application.delete()
        response={
            'type': 'Success', 
            'message': 'Application deleted'
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Update an application by email 
@api_view(["PATCH"])
def updateApplicationByID(request):
    try:
        data = request.data
        id = request.query_params.get("id")
        fieldToBeUpdated = data.get("update")
        updatedValue = data.get(fieldToBeUpdated)

        # next feature, update multiple values in the object
        application = Application.objects.get(id=id)
        
        if fieldToBeUpdated == "skills":
            application.skills.set(SkillTag.objects.get_or_create(name=skill)[0] for skill in updatedValue)

        if fieldToBeUpdated == "name":
            application.name = updatedValue
            application.save()

        if fieldToBeUpdated == "email":
            application.email = updatedValue
            application.save()
                 
        serializer = ApplicationSerializer(application, many=False)
        response={
            'type': 'Success', 
            'message': 'successfully updated your info',
            'results': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Mark verdict of an application by email 
@api_view(["PATCH"])
def markApplicationByID(request):
    try:
        id = request.query_params.get("id")
        application = Application.objects.get(id=id)
        data = request.data
        verdict = data.get("verdict")

        if verdict == "True" or verdict == "False":
            # application.selected = True if verdict == "True" else False
            application.selected = verdict
            application.save()
        
        else:
            return Response({"details": "Inappropriate value"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ApplicationSerializer(application, many=False)
        response={
            'type': 'Success', 
            'message': 'successfully marked application',
            'results': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get all the selected applications 
@api_view(["GET"])
def getSelectedApplications(request):
    try:
        applications = Application.objects.all()
        query = "True"

        queryset_list = applications.filter(
            Q(selected__icontains=query)
        ).distinct()

        # print(queryset_list)
        
        serializer = ApplicationSerializer(queryset_list, many=True)

        response={
            'type': 'Success', 
            'message': 'successfully marked application',
            'results': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get all the reject applications 
@api_view(["GET"])
def getRejectedApplications(request):
    try:
        application = Application.objects.all()
        query = "False"

        queryset_list = application.filter(
            Q(selected__icontains=query)
        ).distinct()

        # print(queryset_list)
        serializer = ApplicationSerializer(queryset_list, many=True)

        response={
            'type': 'Success', 
            'message': 'successfully marked application',
            'results': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Upload/Update resume 
class ResumeUpdate(APIView):
    serializer_class=ApplicationSerializer
    parser_class=(FileUploadParser,)

    def patch(self, *args, **kwargs):
        try:
            rd = random.Random()
            resume=self.request.FILES['resume'] 
            extension = os.path.splitext(resume.name)[1]
            resume.name='{}{}'.format(uuid.UUID(int=rd.getrandbits(128)), extension)
            filename = default_storage.save(resume.name, resume)

            data = self.request.data
            id = data['id']
            application = Application.objects.get(id=id)
            
            setattr(application, 'resume', filename)
            serializer=self.serializer_class(
                application, data={}, partial=True)
            if serializer.is_valid():
                res=serializer.save()
                response={
                    'type': 'Success', 
                    'message': 'successfully uploaded your resume',
                    'results': ApplicationSerializer(res).data
                }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'details': f"{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)