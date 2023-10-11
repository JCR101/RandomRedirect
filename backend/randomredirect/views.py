from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RedirectLinkSerializer
from .models import RedirectLink
from django.http import HttpResponse
from django.shortcuts import redirect as djangoredirect
import random
import string


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


# start of an api endpoint that frontend can POST to with some x-www-form-urlencoded data and returns a url from the request.


def generate_short_link(length=6):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def create_short_link(request):
    if request.method == "POST":
        random_link = request.POST.get("url", None)
        if not random_link:
            return HttpResponseBadRequest("URL not provided")

        short_id = generate_short_link()

        while RedirectLink.objects.filter(short_link_id=short_id).exists():
            short_id = generate_short_link()

        link = RedirectLink.objects.create(
            short_link_id=short_id, random_link=random_link
        )

        response_data = {
            "short_link": request.build_absolute_uri(
                reverse("redirect_view", args=[short_id])
            )
        }
        return JsonResponse(response_data)
    else:
        return HttpResponseBadRequest("Invalid request")
