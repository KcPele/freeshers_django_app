from rest_framework import serializers
from .models import UploadFile, SubscribedEmail
class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = '__all__'


class SubscribedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedEmail
        fields = ['email_name']