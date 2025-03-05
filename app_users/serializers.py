from random import randint
from rest_framework import serializers # type: ignore
from django.contrib.auth import get_user_model # type: ignore

from .models import User


User = get_user_model()


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone', 'full_name', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"non_field_errors": ["Passwords must match"]})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")  # confirm_password ni olib tashlash
        user = User.objects.create_user(**validated_data)
        return user

# class RegisterSerializer(serializers.ModelSerializer): # PASTDA HAM CLASS BOR

#     confirm_password = serializers.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ("id","is_user","is_admin","full_name","phone","password","confirm_password")

#     def validate(self, data):
#         password = data.get("password")
#         confirm_password = data.get("confirm_password")

#         if password != confirm_password:
#             raise serializers.ValidationError("Passwords must match")

#         return data

#     def create(self, validated_data):
#         """ Yangi foydalanuvchini yaratish """
#         password = validated_data.get("password")
#         validated_data.pop("confirm_password")

#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.is_active = True
#         user.save()
#         return user

class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    verification_code = serializers.CharField(max_length=4)




