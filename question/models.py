from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):

    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images",null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answers(models.Model) :
    question= models.ForeignKey(Questions,on_delete=models.CASCADE)    
    answer= models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name="upvote")

    def __str__(self):
        return self.answer



