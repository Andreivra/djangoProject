from django.db import models


class Trainer(models.Model):
    dep_options = [('bck', 'Backend'), ('frt', 'Frontend'), ('ntw', 'Network')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    department = models.CharField(choices=dep_options, max_length=6)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # auto-now_add salveaza data si ora de creere
    updated_at = models.DateTimeField(auto_now=True)  # auto_now salveaza data ora cand se modifica intrarea

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

