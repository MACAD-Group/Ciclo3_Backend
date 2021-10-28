#Django
from django.conf import settings

#Django Rest framework
from rest_framework import generics, status
from rest_framework.response import Response

#Simple JWT
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

#model
from bookstoreApp.models import User

#Serializer
from bookstoreApp.serializers import UserUpdateSerializer

class CustomerDeleteAccountView(generics.DestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request, *args, **kwargs):
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)