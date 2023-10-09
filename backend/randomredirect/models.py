from django.db import models

# Create your models here.


class RedirectLink(models.Model):
    random_link = models.URLField()
    short_link_id = models.TextField()

    def _str_(self):
        return self.short_link + " - " + self.random_link
