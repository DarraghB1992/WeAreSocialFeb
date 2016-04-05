from django.db import models



# Create your models here.
class Contact(models.Model):
    class Meta:
        app_label = 'ModelTest_App'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return "Yo! It's " + self.first_name
