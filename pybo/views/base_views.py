from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    page = request.GET.get('page', '1')     # 페이지
    kw = request.GET.get('kw', '')      # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(       # 0filter 함수에서 __(언더바 두개)를 이용하여 모델 하위 속성에 접근 가능
            Q(subject__icontains=kw) |      # 제목 검색. contains 대신 icontains 사용하면 대소문자 구분x
            Q(content__icontains=kw) |      # 내용 검색
            Q(answer__content__icontains=kw) |      # 답변 내용 검색
            Q(author__username__icontains=kw) |     # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)    # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 없는 데이터 요청 시 500 대신 404 페이지 출력하기 위해 get_object_or_404 사용
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
