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
<<<<<<< HEAD
    Reservation,
    Medicine,
    Prescription,
)


class SpecialtySerializer(ModelSerializer):
    class Meta:
        model = Specialty
        fields = ["id", "title"]

=======
    Reservation
)

class SpecialtySerializer(ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'title']
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
<<<<<<< HEAD
        fields = "__all__"  # Ensure time_slot is included


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "firstname",
            "lastname",
            "age",
            "address",
            "photo",
            "doctor_price",
            "university",
            "specialty",
        ]
=======
        fields = '__all__'  # Ensure time_slot is included
        
class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'firstname', 'lastname', 'age', 'address', 'photo', 'doctor_price', 'university', 'specialty']
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ("email",)
=======
        fields = (
            'email',
        ) 
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class managmentSerializer(ModelSerializer):
    class Meta:
        model = managment

<<<<<<< HEAD

=======
 
>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["patient_status"]


<<<<<<< HEAD
class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = "__all__"
=======

class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacist
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = '__all__'

>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class RefoundSerializer(ModelSerializer):
    class Meta:
        model = Refound
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = '__all__'

>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720


class ReceptionSerializer(ModelSerializer):
    class Meta:
        model = Reception
<<<<<<< HEAD
        fields = "__all__"


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


class PrescriptionSerializer(ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    medicines = MedicineSerializer(many=True)

    class Meta:
        model = Prescription
        fields = "__all__"
=======
        fields = '__all__'





>>>>>>> c465ed859cccc5a8ba1273f9a8d7ad9ca3969720
