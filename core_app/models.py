from django.db import models
from users_app.models import UserAccount
from django.utils.text import slugify
from helper.models import DateTimeModelMixin


# Create your models here.
class Questions(DateTimeModelMixin):
    id                  =   models.AutoField(primary_key=True)
    question_title      =   models.CharField(max_length=128, unique=True)
    question_slug       =   models.CharField(max_length=256, editable=False, unique=True)
    asked_by            =   models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='questions')

    def save(self, *args, **kwargs):
        self.question_slug = slugify(self.question_title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.question_title


class Answers(DateTimeModelMixin):
    id                  =   models.AutoField(primary_key=True)
    question            =   models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
    answer_detail       =   models.TextField()
    answer_by           =   models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='user_answers')
    # likes               =   models.IntegerField(default=0)
    # dislikes            =   models.IntegerField(default=0)
    liked_by            =   models.ManyToManyField(UserAccount, related_name='liked_answers', blank=True, null=True)
    disliked_by         =   models.ManyToManyField(UserAccount, related_name='disliked_answers', blank=True, null=True)

    class Meta:
        unique_together = ('question', 'answer_by')

# class AnswerResponse(models.Model):
#     id                  =   models.AutoField(primary_key=True)
#     answer              =   models.OneToOneField(Answers, on_delete=models.CASCADE, related_name='responses')
#     liked_users         =   models.JSONField(default=list)
#     dis_liked_users     =   models.JSONField(default=list)

