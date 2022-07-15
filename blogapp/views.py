import re
from urllib import request
from django.shortcuts import render,redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    posts =  Blog.objects.all()
    # 날짜 기준으로 정렬된 오름차순(date) 
    # 내림차순은 (.date)
    #posts = Blog.objects.filter().order_by('.date')
    # 내가 가져오고싶은 것만 필터링해서 가져온다
    return render(request, 'index.html', {'posts':posts})


def home(request):
    return render(request, 'index.html')

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request,"new.html")
    # new.html에서 생성버튼 누르면 create로 이동

# 블로그 글을 저장해주는 함수
def create(request):
    
    if(request.method == "POST"):
        # 만약 POST 전송이라면
        post = Blog()
        # Blog 객체 생성
        post.title = request.POST["title"]
        # title에는 이 정보를 담고
        post.body = request.POST["body"]
        # body에는 이 정보를 담고
        post.date = timezone.now()
        # date에는 이 정보를 담고
        # timezone import 해주기
        post.save()
        # 저장해라
    return redirect("home")
    # 과정이 끝났다면 home으로 redirect 
    # redirect 도 import 해주기
    # admin 사이트에서 객체 추가 확인


# django form을 이용해서 입력값을 받는 함수
#  GET 요청과 (= 입력을 받을 수 있는 html을 갖다줘! 전달)
#  POST 요청 (= 입력한 내용을 DB에 저장해줘!, form에서 입력한 내용을 처리)
#  둘 다 처리가 가능한 함수

def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        # POST 요청 시
        form = BlogForm(request.POST)
        if form.is_valid():
            # .is_valid() -> 유효성 검사
            # form 안에 입력한 값이 유효하다면
            post = Blog()
            post.title = form.cleaned_data['title']
            # form 으로 검증받은 데이터 -> .cleanded_data
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home') 
    else: # GET 요청
        # 입력을 받을 수 있는 html을 갖다줘!
        form = BlogForm()
    return render(request, 'form_create.html', {'form' : form}) 
   
    # render()의 세번째 인자로 views.py 내의 데이터를 html에 넘길 수 O
    # 단, 딕셔너리 자료형으로 넘겨줘야 함


def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            # model form은 form 자체가 save 메소드 가지고 있기 때문에
            # form.save()만 해도 저장됨
            return redirect('home')
    
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})