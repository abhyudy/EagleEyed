from django.db import models
# Create your models here.
class studentForm(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    phoneNo=models.CharField(max_length=13)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
     
class teacherForm(models.Model):
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name