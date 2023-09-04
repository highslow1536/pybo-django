from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   # null=True(null 허용), blank=True(is_valid() 검증때 값 없어도 됨)
    voter = models.ManyToManyField(User, related_name='voter_question')     # some_user.voter_question.all() 과 같이 사용 가능

    def __str__(self):          # 모델에 메서드 추가는 makemigrations와 migrate 수행할 필요x
        return self.subject     # 모델의 속성이 변경되었을 때 makemigrations, migrate 명령 필요


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Question 모델과 연결하기 위해 ForeignKey 사용
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   # null=True(null 허용), blank=True(is_valid() 검증때 값 없어도 됨)
    voter = models.ManyToManyField(User, related_name='voter_answer')   # some_user.voter_answer.all()과 같이 사용 가능
