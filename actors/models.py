from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('FRANCE', 'França'),
    ('GERMANY', 'Alemnaha'),
    ('UK', 'Inglaterra'),
    ('IT', 'Italia'),
    ('ES', 'Espanha'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField( max_length=50, choices=NATIONALITY_CHOICES, blank=True, null=True )
    
    def __str__(self):
        return self.name
