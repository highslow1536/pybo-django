import markdown
from django import template
from django.utils.safestring import mark_safe
import bleach
from bleach.linkifier import LinkifyFilter

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


# 해당 필터 사용시 xss 취약점 존재. {{ content|escape|mark }} 로 사용하면 html 태그는 걸러줄 수 있지만, 링크에 javascript: 넣으면 뚫림.
# 따라서 mark 필터 말고 django-markup 라이브러리의 필터 사용 권장.  (예시) {{ content|apply_markup:"markdown" }}
# pip install django-markup[all_filter_dependencies]    # (https://github.com/bartTC/django-markup 참고)
# django-markup 라이브러리 내부적으로는 bleach 라이브러리의 clean 함수를 이용하여 동작
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]   # 마크다운 확장 기능, nl2br: 줄바꿈문자 -> <br> , fenced_code: 소스코드 표현 위해 필요
    return mark_safe(markdown.markdown(value, extensions=extensions))
