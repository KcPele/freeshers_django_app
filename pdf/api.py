from rest_framework import viewsets
from .serializers import UploadFileSerializer
from .models import UploadFile, SubscribedEmail
from rest_framework import generics

class UploadFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer

