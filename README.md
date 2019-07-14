# CRUD
1. 앱 생성

```bash
python manage.py startapp appname
```
2. settings.py의 INSTALLED_APPS에 추가
```python
INSTALLED_APPS = [
    //생략
    'appname.apps.AppnameConfig',
]
```
3. models.py에서 모델 생성
```python
from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
```       
4. project 생성 후 migrate 해 주기
```bash
python manage.py makemigrations
python manage.py migrate
```
5. templates 폴더에 html 파일 만들기, views.py에 함수 만들고 url.py에서 url 연결하기
`home.html`
```html
{% extends 'base.html' %}

{% block content %}

{% for blog in blogs.all %}
<h1>제목: {{blog.title}}</h1>
<p>날짜: {{blog.pub_date|date:"Y-m-d"}}</p>
<p>내용: {{blog.summary}} <a href="{% url 'detail' blog.id %}">...more</a></p>
<br><hr>

{% endfor %}

{% endblock %}
```
`views.py`
```python
from django.shortcuts import render
from .models import Appname

def home(request):
    blogs = Appname.objects
    return render(request, 'appname/home.html', {'blogs': blogs})
```
`urls.py`
```python
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
]
```
1. static 폴더와 templates 폴더 만들기
```bash
python manage.py collectstatic
```

3. settings.py에 static 폴더와 templates 폴더 설정하기
static 파일 한 곳에 모아 주는 명령어

```python
//TEMPLATES 안에
'DIRS': ['project/templates'],
```

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio', 'static') //portfolio는 static 파일의 경로
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

4. SUPERUSER 만들기
```bash
python manage.py createsuperuser
```

## Create

가상환경 실행
project와 app 생성

#### Model

class명은 대문자

#### render & redirect

- render: 요청이 들어오면 html 파일을 보여 줌
- redirect: 요청이 들어오면 url로 보냄




#### detail

1. **n 번째 블로그 객체** 요청 -> n 번 객체 내용 띄우기

   =>pk

2. url 설계
   - **사이트/blog/객체 번호(n)**

=>path converter

3.  없는 객체 요청 시 **404 에러** 띄우기

    =>get_object_or_404

    ##### path-converter

         <int:blog_id> 같은 것
            - int: blog/정수 형태로 디자인
            - blog_id: detail 함수로 넘기는 인자
         계층적 url 필요할 경우에 사용
         <type:name>과 같은 모양

    ##### pk(primary key)

         객체들의 이름표, 구분자, 데이터의 대표 값
         어떤 값을 데이터의 대표 값으로 삼을지는 정의하기 나름이다! 
         모델에서 찍어 낸 수많은 객체들을 구분할 수 있는 **데이터구분자**

    ##### get_object_or_404

         get_object_or_404(클래스, 검색 조건(몇 번 데이터, pk))





# input type=hidden


UI가 눈에 보이지는 않지만 서버로 데이터 전송할 때 사용

```html
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="http://localhost/hidden.php">
            <input type="text" name="id">
            <input type="hidden" name="hide" value="egoing">
            <input type="submit">
        </form>
    </body>
</html>
```

