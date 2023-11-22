from rest_framework import serializers
from .import models

class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"

class DegprmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Degreeprogram
        fields = "__all__"

class SemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Semester
        fields = "__all__"

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"

class FacSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = "__all__"

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimetableData
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = "__all__"
