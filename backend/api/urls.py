from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.users, name='users'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    # path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("application/add/", views.createApplication, name="create-application"),
    # path('users/<str:username>/', views.userDetails, name="user"),
    # path('users/<str:username>/update-skills',
    #      views.userSkills, name="user_skills"),
    # path('users/<str:username>/update-interests',
    #      views.userInterests, name="user_interests"),
    # path('sendmail/', views.sendMailToALL, name="sendmail"),
]
