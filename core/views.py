from django.shortcuts import render
from rest_framework.views import APIView
<<<<<<< HEAD
from .models import (
    Doctor,
    Specialty,
    managment,
    Patient,
    Pharmacy,
    Refound,
    Reception,
    Reservation,
    Medicine,
    Prescription,
)

from .serializers import (
    SpecialtySerializer,
    DoctorSerializer,
=======
from .models import Doctor, Specialty, managment, Patient, Pharmacy, Refound, Reception,Reservation
from .serializers import (
    SpecialtySerializer,
    doctorSerializer,
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
    managmentSerializer,
    PatientSerializer,
    PharmacySerializer,
    ReceptionSerializer,
    RefoundSerializer,
<<<<<<< HEAD
    ReservationSerializer,
    MedicineSerializer,
    PrescriptionSerializer,
)

from rest_framework import generics, status
=======
    ReservationSerializer
)

from rest_framework import generics,status
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from user_auth.permissions import (
    DoctorPermission,
    ReciptionPermission,
<<<<<<< HEAD
    PharmacyPermission,
)


=======
    PharmacyPermission
)

>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class DoctorReservationAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
<<<<<<< HEAD
        doctor_id = self.kwargs["doctor_id"]
        return Reservation.objects.filter(doctorID_id=doctor_id)


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
=======
        doctor_id = self.kwargs['doctor_id']
        return Reservation.objects.filter(doctorID_id=doctor_id)
        
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = doctorSerializer
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsAdminUser | ReciptionPermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

<<<<<<< HEAD

class DoctorDetail(
    generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView
):  # Added generics.CreateAPIView
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser | ReciptionPermission]


=======
class DoctorDetail(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):  # Added generics.CreateAPIView
    queryset = Doctor.objects.all()
    serializer_class = doctorSerializer
    permission_classes = [IsAdminUser | ReciptionPermission]



>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class ManagmentList(generics.ListCreateAPIView):
    queryset = managment.objects.all()
    serializer_class = managmentSerializer
    permission_classes = [IsAdminUser]


class patientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
<<<<<<< HEAD
=======
    
    
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "GET":
            permission_classes = [IsAdminUser | ReciptionPermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
<<<<<<< HEAD


class patientDetail(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAdminUser | ReciptionPermission]
=======
        
class patientDetail(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
     queryset = Patient.objects.all()
     serializer_class = PatientSerializer
     permission_classes = [IsAdminUser | ReciptionPermission]

>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class pharmacyList(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
<<<<<<< HEAD

=======
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
    def get(self, request):
        user = request.user
        if user.role != 2:
            response = {
<<<<<<< HEAD
                "success": False,
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": "You are not authorized to perform this action",
=======
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            pharamcy = pharamcy.objects.all()
            serializer = self.serializer_class(pharamcy, many=True)
            response = {
<<<<<<< HEAD
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Successfully fetched users",
                "users": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)


class RefoundListCreateAPIView(APIView):
=======
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)
        



class RefoundListCreateAPIView(APIView):
    
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
    def get(self, request):
        refounds = Refound.objects.all()
        serializer = RefoundSerializer(refounds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RefoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD

=======
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class ReceptionListCreateAPIView(APIView):
    def get(self, request):
        receptions = Reception.objects.all()
        serializer = ReceptionSerializer(receptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD


=======
    
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class SpecialtyList(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

<<<<<<< HEAD

class DoctorsBySpecialty(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        specialty_id = self.kwargs["specialty_id"]
        return Doctor.objects.filter(specialty__id=specialty_id)


=======
class DoctorsBySpecialty(generics.ListAPIView):
    serializer_class = doctorSerializer

    def get_queryset(self):
        specialty_id = self.kwargs['specialty_id']
        return Doctor.objects.filter(specialty__id=specialty_id)
    
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class DoctorReservationAPIView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
<<<<<<< HEAD
        doctor_id = self.kwargs["doctor_id"]
        return Reservation.objects.filter(doctorID_id=doctor_id).order_by("time_slot")
=======
        doctor_id = self.kwargs['doctor_id']
        return Reservation.objects.filter(doctorID_id=doctor_id).order_by('time_slot')
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Check for time slot availability
<<<<<<< HEAD
            doctor_id = request.data.get("doctorID")
            time_slot = request.data.get("time_slot")
            if Reservation.objects.filter(
                doctorID_id=doctor_id, time_slot=time_slot
            ).exists():
                return Response(
                    {"error": "Time slot is already booked."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineListCreateView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class MedicineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    lookup_url_kwarg = "medicine_id"


class PrescriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_url_kwarg = "prescription_id"
=======
            doctor_id = request.data.get('doctorID')
            time_slot = request.data.get('time_slot')
            if Reservation.objects.filter(doctorID_id=doctor_id, time_slot=time_slot).exists():
                return Response({"error": "Time slot is already booked."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
