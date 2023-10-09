from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RedirectLinkSerializer
from .models import RedirectLink

# Create your views here.


class RedirectLinkView(viewsets.ModelViewSet):
    serializer_class = RedirectLinkSerializer
    queryset = RedirectLink.objects.all()
