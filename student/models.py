from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    gender_options = [('male', 'Male'), ('female', 'Female')]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options, max_length=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # auto-now_add salveaza data si ora de creere
    updated_at = models.DateTimeField(auto_now=True)  # auto_now salveaza data ora cand se modifica intrarea

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
