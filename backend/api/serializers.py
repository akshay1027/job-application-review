from dataclasses import fields
from rest_framework import serializers

from .models import Application, SkillTag


class ApplicationSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Application
        # fields = ["name", "id", "selected", "skills", "email", "collegeName"]
        fields = '__all__'

    def get_resume(self, obj):
        try:
            pic = obj.resume.url
        except:
            pic = None
        return pic