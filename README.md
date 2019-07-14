# CRUD

~~수정 중~~

#### Create
가상환경 실행
project와 app 생성

#### Model
class명은 대문자


#### path-converter
<int:blog_id> 같은 것
계층적 url 필요할 경우에 사용
<type:name>과 같은 모양

#### pk(primary key)
모델에서 찍어 낸 수많은 객체들을 구분할 수 있는 **구분자**

#### render & redirect
- render: 요청이 들어오면 html 파일을 보여 줌
- redirect: 요청이 들어오면 url로 보냄

#### static

settings.py에 추가
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

static 파일 한 곳에 모아 주는 명령어 입력
```bash
python manage.py collectstatic
```


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

