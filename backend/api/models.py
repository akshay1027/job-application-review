from django.db import models
import uuid


class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(unique=True, null=True)
    selected = models.CharField(max_length=4, default="False")
    collegeName = models.CharField(max_length=300, null=False, blank=False)
    skills = models.ManyToManyField(SkillTag, related_name="skill", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    jobId = models.CharField(max_length=100, null=False, blank=False)
    resume = models.ImageField(blank=True, null=True)
