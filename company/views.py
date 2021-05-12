from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cldr, Docu, Pd, Pins, Run, Zm, Zuo
from .serializers import CldrSerializer, DocuSerializer, PdSerializer, PinsSerializer, RunSerializer, ZmSerializer, ZuoSerializer
# Create your views here.

class CompanyView(APIView):
    def get(self, request):
        return Response({'Companies:': 'CLDR, DOCU, PD, PINS, RUN, ZM, ZUO'})

class CldrView(APIView):
    def get(self, request):
        cldrs = Cldr.objects.all()
        serializer = CldrSerializer(cldrs, many=True)
        return Response({'CLDR': serializer.data})

class DocuView(APIView):
    def get(self, request):
        docus = Docu.objects.all()
        serializer = DocuSerializer(docus, many=True)
        return Response({'DOCU': serializer.data})

class PdView(APIView):
    def get(self, request):
        pds = Pd.objects.all()
        serializer = PdSerializer(pds, many=True)
        return Response({'PD': serializer.data})

class PinsView(APIView):
    def get(self, request):
        pinss = Pins.objects.all()
        serializer = PinsSerializer(pinss, many=True)
        return Response({'PINS': serializer.data})

class RunView(APIView):
    def get(self, request):
        runs = Run.objects.all()
        serializer = RunSerializer(runs, many=True)
        return Response({'RUN': serializer.data})

class ZmView(APIView):
    def get(self, request):
        zms = Zm.objects.all()
        serializer = ZmSerializer(zms, many=True)
        return Response({'ZM': serializer.data})

class ZuoView(APIView):
    def get(self, request):
        zuos = Zuo.objects.all()
        serializer = ZuoSerializer(zuos, many=True)
        return Response({'ZUO': serializer.data})