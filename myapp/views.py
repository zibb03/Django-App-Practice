from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''
# <li> 태그는 페이지에서 리스트로 표시하도록 함

def index(request):
    article = '''
    <h2>Welcome</h2> 
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    # 9강
    # placeholder - 텍스트 입력 박스에 흐린 글자로 쓰여지게 함
    # <p> 태그는 단락을 나타냄
    # textarea - 여러줄의 텍스트를 입력할 때 이용하는 태그
    # submit 타입 - 제출 버튼
    # form 태그로 감싸야 정보 보낼 수 있음, action은 보내고 싶은 서버의 path 작성

    # 10강
    # <form action = "/create/"> - get 방식이 기본값값
    # <form action="/create/" method="post"> - post 방식으로
    # post로 하면 CSRF 에러 뜨는데, 면제 하는 코드 작성해야 함.
    article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

