from django.db import models

# Create your models here.


class Question(models.Model):
    pub_date = models.DateTimeField('date_published')
    question_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
