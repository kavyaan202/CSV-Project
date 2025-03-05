from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_project.settings')

app = Celery('csv_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
