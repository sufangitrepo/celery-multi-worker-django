from celery import Celery

app = Celery("celeryworker")
app.config_from_object("celeryconfig")
app.conf.imports = ("first.tasks",)
app.autodiscover_tasks()