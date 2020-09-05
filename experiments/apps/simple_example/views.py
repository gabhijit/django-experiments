import time
import os

from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

import uwsgi

# Create your views here.


class SimpleExampleViewSet(ViewSet):

    def list(self, request, *args, **kw):

        procname = "worker:(pid:{:d}) {}".format(os.getpid(), self.request.path)
        uwsgi.setprocname(procname)

        # Do some work!
        time.sleep(30)

        # Work Done - Call myself idle
        uwsgi.setprocname("worker:(pid:{:d}) {}".format(os.getpid(), "idle"))

        return Response(dict(message="Ok"), 200)
