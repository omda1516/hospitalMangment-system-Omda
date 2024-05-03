from django.urls import path
from . import views


urlpatterns = [
    path("doctors/", views.DoctorList.as_view()),
    path("doctor/<int:pk>", views.DoctorDetail.as_view()),
    path("managment/", views.ManagmentList.as_view()),
    # path("managment/<int:pk>", views.managmentDetail.as_view()),
    path("patients/", views.patientList.as_view()),
    path("patient/<int:pk>", views.patientDetail.as_view()),
<<<<<<< HEAD
    path(
        "refounds/",
        views.RefoundListCreateAPIView.as_view(),
        name="refound-list-create",
    ),
    path(
        "receptions/",
        views.ReceptionListCreateAPIView.as_view(),
        name="reception-list-create",
    ),
    path(
        "doctor/<int:doctor_id>/reservations/",
        views.DoctorReservationAPIView.as_view(),
        name="doctor-reservations",
    ),
    path("specialties/", views.SpecialtyList.as_view(), name="specialty-list"),
    path(
        "specialties/<int:specialty_id>/doctors/",
        views.DoctorsBySpecialty.as_view(),
        name="doctors-by-specialty",
    ),
    path(
        "doctor/<int:doctor_id>/reservations/",
        views.DoctorReservationAPIView.as_view(),
        name="doctor-reservations",
    ),
    path(
        "medicine/", views.MedicineListCreateView.as_view(), name="medicine-get-create"
    ),
    path(
        "prescription/",
        views.PrescriptionListCreateView.as_view(),
        name="prescription-get-create",
    ),
    path(
        "medicine/<int:medicine_id>/",
        views.MedicineRetrieveUpdateDestroyView.as_view(),
        name="medicine-retrieve-update-delete",
    ),
    path(
        "prescription/<int:prescription_id>/",
        views.PrescriptionRetrieveUpdateDestroyView.as_view(),
        name="prescription-retrieve-update-delete",
    ),
=======
    path('refounds/', views.RefoundListCreateAPIView.as_view(), name='refound-list-create'),
    path('receptions/', views.ReceptionListCreateAPIView.as_view(), name='reception-list-create'),
    path('doctor/<int:doctor_id>/reservations/', views.DoctorReservationAPIView.as_view(), name='doctor-reservations'),
    path('specialties/', views.SpecialtyList.as_view(), name='specialty-list'),
    path('specialties/<int:specialty_id>/doctors/', views.DoctorsBySpecialty.as_view(), name='doctors-by-specialty'),
    path('doctor/<int:doctor_id>/reservations/', views.DoctorReservationAPIView.as_view(), name='doctor-reservations'),
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720

]


{
    "username": "doctor2",
    "tokens": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjg4NjIyMiwiaWF0IjoxNzEyNzk5ODIyLCJqdGkiOiI2ZTllZjllODU1Mzk0YmMxYmZhMDBmOWM0OTRhYzJkNSIsInVzZXJfaWQiOjR9.qS5Op1LVEO3YbtMZSiwF10mWk-kYyFlUMe_v-8n8Uc4",
<<<<<<< HEAD
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNzk5ODgyLCJpYXQiOjE3MTI3OTk4MjIsImp0aSI6ImJjNmIwNmQ0OWI0MDQ5ODE4ZmFjZWUwNDk2ODBkZjdhIiwidXNlcl9pZCI6NH0.sRp7LwyFBbhptqOq-hckWD4yBuc9dDRAEiB0dAOacBY",
    },
}
=======
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNzk5ODgyLCJpYXQiOjE3MTI3OTk4MjIsImp0aSI6ImJjNmIwNmQ0OWI0MDQ5ODE4ZmFjZWUwNDk2ODBkZjdhIiwidXNlcl9pZCI6NH0.sRp7LwyFBbhptqOq-hckWD4yBuc9dDRAEiB0dAOacBY"
    }
}
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
