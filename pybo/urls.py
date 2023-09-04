from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo'   # URL 네임스페이스 사용 위함. 네임스페이스 사용시 'pybo:detail' 과 같이 별칭 사용

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),    # pybo/ 경로에다가 views 파일의 index 함수 매핑, URL 별칭 사용(index)
    path('<int:question_id>/',
         base_views.detail, name='detail'),    # pybo/<int:question_id>/ 경로에 detail 함수 매핑

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),    # 예시) pybo/answer/create/2/
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),
]
