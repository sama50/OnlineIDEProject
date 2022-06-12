from django.db import models
from django.contrib.auth.models import User

class problem(models.Model):
    title =models.CharField(max_length=800)
    details = models.TextField()
    saveDate = models.DateField(auto_now=True)
    sudoCode = models.FileField(upload_to="file")
    funCall = models.FileField(upload_to="file")
    input1 = models.FileField(upload_to="file")
    input2 = models.FileField(upload_to="file")
    input3 = models.FileField(upload_to="file")
    output1 = models.FileField(upload_to="file")
    output2 = models.FileField(upload_to="file")
    output3 = models.FileField(upload_to="file")

    def __str__(self):
        return self.title
    
    

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userimag = models.ImageField(upload_to ='UserProfileuploads/', blank=True,null=True)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    collegeName = models.CharField(max_length=300)

class ListOfProblem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
