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


#from question.models import Questions,Answers
#from django.contrib.models import User
#usr=User.objects.get(id=1)
#Questions.objects.create(title="django",description="django architecture?",user=usr)
#usr.questions_set.create(title="angular",description="angular architecture?")
#usr.questions_set.create(title="java",description="java architecture?")
#Questions.objects.filter(user=usr)
#qs=usr.questions_set.all()
#ques=Questions.object.get(id=3)
#usr=User.Objects.get(id=2)
#ques.answers_set.create(answer="architecture is here",user=usr)
#usr=User.Objects.get(id=2)

#ques.answers_set.all()


#ques=Questions.objects.get(id=3)
#ques.answers_set.creata(answer="structure based",user=usr)