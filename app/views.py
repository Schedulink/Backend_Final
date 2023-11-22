from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .import serializers
from .import models


class DeptList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartSerializer

class DegprmList(generics.ListCreateAPIView):
    queryset = models.Degreeprogram.objects.all()
    serializer_class = serializers.DegprmSerializer

class SemList(generics.ListCreateAPIView):
    queryset = models.Semester.objects.all()
    serializer_class = serializers.SemSerializer

class SubList(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubSerializer

class FacList(generics.ListCreateAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacSerializer

class TimetableList(generics.ListCreateAPIView):
    queryset = models.TimetableData.objects.all()
    serializer_class = serializers.TimetableSerializer

class AdminList(generics.ListCreateAPIView):
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer


