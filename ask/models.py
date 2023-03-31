from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=20, blank=False,
                             db_index=True, null=False)
    text = models.TextField(max_length=300, blank=False, null=False)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    deleted_at = models.DateTimeField(null=True)


class Answer(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False)
    reply = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(
        Question, blank=False, null=False, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    deleted_at = models.DateTimeField(null=True)
