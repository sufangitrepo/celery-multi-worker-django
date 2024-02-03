from typing import Any
from django.core.management.base import BaseCommand
from first.models import Student
import faker
import random

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = faker.Faker()
        for i in range(0, 1000):
            Student.objects.create(name=fake.name(), age=random.randint(20,50))
        return super().handle(*args, **options)