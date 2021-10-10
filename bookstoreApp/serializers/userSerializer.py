from django.db.models import fields
from bookstoreApp.models.user import User
from rest_framework import serializers
from rest_framework.fields import empty

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields= '__all__'
        
    def to_representation(self, instance):
        return {
                    'id':instance.id,
                    'username': instance.username,
                    'fullname': instance.fullname,
                    'datebirth': instance.datebirth,
                    'gender':instance.gender,
                    'email': instance.email,
                    'identification': instance.identification,
                    'phone_number':instance.phone_number,
                    'address': instance.address    
                }
class UserUpdateSerializer(serializers.ModelSerializer):
    username= serializers.CharField()
    id= serializers.IntegerField()
    class Meta:
        model = User
        fields= '__all__'
        