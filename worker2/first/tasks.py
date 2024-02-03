from celery import shared_task
import pandas as pd
from celer_pract.first.models import Student

@shared_task(name="first.tasks.t2")
def t2():
    return 2

@shared_task(name="first.tasks.write_csv")
def write_csv():
    try:
        st = []
        for student in Student.objects.all():
            st.append({"name":student.name,"age":student.age})
        df = pd.DataFrame(st)
        df.to_csv("f.csv",encoding="utf-8")
        return True
    except Exception as e:
        return e
    
