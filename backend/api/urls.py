from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.users, name='users'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    # path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("application/add/", views.createApplication, name="create-application"),
    path("application/get/", views.getApplicationByID, name="get-application"),
    path("application/", views.getAllApplication, name="get-all-application"),
    path("application/mark", views.markApplicationByID, name="mark-application-result"),
    path("application/update", views.updateApplicationByID, name="update-application"),
    path("application/delete", views.deleteApplicationByID, name="delete-application"),
    path('application/resume/', views.ResumeUpdate.as_view(), name="resume_update"), 
    # path('users/<str:username>/', views.userDetails, name="user"),
    # path('users/<str:username>/update-skills',
    #      views.userSkills, name="user_skills"),
    # path('users/<str:username>/update-interests',
    #      views.userInterests, name="user_interests"),
]
