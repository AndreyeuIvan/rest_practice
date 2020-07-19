from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.
from .models import Url
from .serializers import UrlSerializer
import csv
from django.shortcuts import HttpResponse


class UrlListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()


class UrlShortener(generics.ListCreateAPIView):
    def post_my(self, request, origin_uri):
        try:
            url = Url.objects.get(url=origin_uri)
        except:
            url = Url(url=origin_uri)
            url.save()

        short_url=url.short_url
        print(short_url)

        return Response(short_url)


class UrlExport(generics.ListCreateAPIView):
    def get(self, request):
        responce = HttpResponse(content_type='text/csv')
        responce['Content-Disposition'] = "attachment; filename='export.csv'"

        writer = csv.writer(responce)
        fields = Url.objects.all().values_list('url', 'short_url')

        for row in fields:
            writer.writerow(row)

        return responce