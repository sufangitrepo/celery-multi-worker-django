from celery import shared_task
import pandas as pd

@shared_task(name="first.tasks.t1")
def t1():
    return 1



