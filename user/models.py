from django.db import models

# Create your models here.

class Enquiry(models.Model):
  name = models.CharField(max_length=255)
  email =models.EmailField()
  subject=models.CharField(max_length=255)
  message =models.TextField()
  post_on =models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name