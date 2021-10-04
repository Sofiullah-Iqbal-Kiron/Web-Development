from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    rank = models.IntegerField(default=3)

    def __str__(self) -> str:
        return self.full_name


class Article(models.Model):
    headline = models.CharField(max_length=200)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return self.headline
