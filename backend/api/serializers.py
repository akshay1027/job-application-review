from dataclasses import fields
from rest_framework import serializers

from .models import Application, SkillTag


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["name", "id", "selected", "skills", "email", "collegeName"]
