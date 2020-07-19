from django.db import models
import uuid
import base64
from django.core.validators import URLValidator

# Create your models here.

HOST_NAME = 'https://127.0.0.1:8000/'


class Url(models.Model):
    url = models.CharField(max_length=256, validators=[URLValidator()])
    url_hash = models.CharField(max_length=10, unique=True, db_index=True)
    short_url = models.CharField(max_length=256, validators=[URLValidator()], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_my_hash()
        self.short_url = self.create_short_url()
        super(Url, self).save(*args, **kwargs)

    def generate_my_hash(self):
        my_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
        hash_exist = Url.objects.filter(url_hash=my_hash)
        while hash_exist:
            my_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
            hash_exist = Url.objects.filter(url_hash=my_hash)
            continue

        my_hash = my_hash.decode('utf-8')

        return my_hash

    def create_short_url(self):
        return '' + self.url_hash


