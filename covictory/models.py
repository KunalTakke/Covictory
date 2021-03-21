from django.db import models

# Create your models here.

class contactform(models.Model):
    contactfrom_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=100, default="")
    mobile_number = models.IntegerField(default=9999999999)
    email_id = models.EmailField(default='')
    sub = models.CharField(max_length = 500)


    def __str__(self):
        return self.first_name