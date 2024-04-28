from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from .models import (
    Doctor,
    Specialty,
    managment,
    Patient,
    Pharmacy,
    Pharmacist,
    Refound,
    Reception,
    Reservation
)

class SpecialtySerializer(ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'title']

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'  # Ensure time_slot is included
        
class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'firstname', 'lastname', 'age', 'address', 'photo', 'doctor_price', 'university', 'specialty']


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        ) 


class managmentSerializer(ModelSerializer):
    class Meta:
        model = managment

 
class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["patient_status"]



class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'



class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'



class RefoundSerializer(ModelSerializer):
    class Meta:
        model = Refound
        fields = '__all__'



class ReceptionSerializer(ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'





