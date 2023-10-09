from rest_framework import serializers
from .models import RedirectLink


class RedirectLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedirectLink
        fields = ("id", "random_link", "short_link_id")
