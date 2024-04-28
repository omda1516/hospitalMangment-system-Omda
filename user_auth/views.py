from sqlite3 import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                # ... create a Patient instance, etc. ...
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if 'username' in str(e):
                    return Response({'username': ['A user with that username already exists.']}, status=status.HTTP_400_BAD_REQUEST)
                # You can add more error handling for other unique fields if necessary
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)



# Logout View - Uncomment and ensure it uses the correct serializer
#class LogoutAPIView(generics.GenericAPIView):
   # serializer_class = LoginSerializer
   # permission_classes = (IsAuthenticated,)
  #  def post(self, request):
       # serializer = self.serializer_class(data=request.data)
       # serializer.is_valid(raise_exception=True)
      #  serializer.save()
        #return Response(status=status.HTTP_204_NO_CONTENT)


# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)