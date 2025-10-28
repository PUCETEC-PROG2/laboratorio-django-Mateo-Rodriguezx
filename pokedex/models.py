from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name =models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)

    def __str__(self):
        return self.name