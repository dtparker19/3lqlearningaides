# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flashcards(models.Model):
    pass

class UserFlashcards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcards, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username + " - " + self.flashcard.title
    
class PracticeExam(models.Model):
    pass

class UserPracticeExam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    practice_exam = models.ForeignKey(PracticeExam, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.FloatField()
    def __str__(self):
        return self.user.username + " - " + self.practice_exam.title
    
class PracticeExamQuestion(models.Model):
    PracticeExam_exam = models.ForeignKey(PracticeExam, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()



