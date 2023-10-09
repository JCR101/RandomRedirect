from django.contrib import admin
from .models import RedirectLink


class RedirectLinkAdmin(admin.ModelAdmin):
    list_display = ("random_link", "short_link_id")


# Register your models here.

admin.site.register(RedirectLink, RedirectLinkAdmin)
