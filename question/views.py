from django.shortcuts import render
from question.serializers import UserSerializer,QuestionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from question.models import Questions
from rest_framework import authentication,permissions

class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class QuestionView(ModelViewSet):
    serializer_class= QuestionSerializer
    queryset=Questions.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
