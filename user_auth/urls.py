from django.urls import path
from . import views
from .views import LoginAPIView, UserRegistrationView


app_name = 'auth'

urlpatterns = [
   # path('login/', views.LoginAPIView.as_view(), name='user-login'),
   # path('logout/', TokenBlacklistView.as_view(), name='user-logout'),
   # path('signup/doctor/', views.DoctorRegisterView.as_view(), name='doctor-signup'),
   # path('signup/patient/', views.PatientRegisterView.as_view(), name='patient-signup'),
   # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

]
