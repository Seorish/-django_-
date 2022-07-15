from dataclasses import field
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값을
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
                            # CharField 보다 더 넓은 범위 텍스트수용할 때
# 하나하나 객체를 생성해서 입력 값 담아둬야함

class BlogModelForm(forms.ModelForm):
                    # ModelForm을 상속받은 class
# form의 존재부터가 model 기반으로 만들어졌기에 간편하게 form 설계 가능  
    class Meta:
        model = Blog
        # 어떤 model을 기반으로 자동으로 form을 생성할 건지 작성
        # fields = '__all__'
        # Blog 클래스 안에 있는 title, body 모두 입력받을 수 있음
        fields = ['title','body']
        # 특정 데이터만 입력받을 때