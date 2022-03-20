from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,blank = True, null=True)
    title = models.CharField(max_length=250)
    desciption = models.TextField(null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']