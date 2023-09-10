from django.db import models

# Create your models here.
class New(models.Model):
    title=models.CharField(max_length=250)
    date_of_publish=models.DateField(auto_created=True)
    content=models.TextField()
    writer=models.CharField(max_length=250)

    def __str__(self):
        return self.title
