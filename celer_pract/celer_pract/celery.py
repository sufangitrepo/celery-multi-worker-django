import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celer_pract.settings')

app = Celery('celery_pract')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routes = {
  "first.tasks.t1":{"queue": "queue1"},
  "first.tasks.t2":{"queue": "queue2"},
  "first.tasks.write_csv":{"queue": "queue1"}

}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)