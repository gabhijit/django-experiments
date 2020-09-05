from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Create your views here.


class SimpleExampleViewSet(ViewSet):


    def list(self, request, *args, **kw):

        return Response(dict(message="Ok"), 200)
