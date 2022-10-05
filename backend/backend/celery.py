import os

from celery import Celery

# celery is a async message queue to perform background tasks outside request response cycle

# First, we set a default value for the DJANGO_SETTINGS_MODULE environment variable so that Celery will know how to find the Django project.
# Next, we created a new Celery instance, with the name core, and assigned the value to a variable called app.
# We then loaded the celery configuration values from the settings object from django.conf. We used namespace="CELERY" to prevent clashes with other Django settings.
# All config settings for Celery must be prefixed with CELERY_, in other words.
# Finally, app.autodiscover_tasks() tells Celery to look for Celery tasks from applications defined in settings.INSTALLED_APPS.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
