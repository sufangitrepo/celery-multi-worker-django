from celery import shared_task


@shared_task(name="first.tasks.t2")
def t2():
    return 2

