from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RedirectLinkSerializer
from .models import RedirectLink
from django.http import HttpResponse
from django.shortcuts import redirect as djangoredirect
import random


# Create your views here.


# class RedirectLinkView(viewsets.ModelViewSet):
#     serializer_class = RedirectLinkSerializer
#     queryset = RedirectLink.objects.all()


def redirect(request, short_url):
    x = (
        RedirectLink.objects.filter(
            short_link_id=short_url,
        )
        .order_by("?")
        .first()
    )
    y = RedirectLink.objects.create(
        short_link_id="test1", random_link="https://fast.com"
    )
    # created a url and add a redirect link object that contains the short url and contains a test redirect url

    if x == None:
        return HttpResponse("Invalid URL")

    return djangoredirect(y.random_link)


def index(request):
    if request.method == "GET":
        return HttpResponse("Hello World")
