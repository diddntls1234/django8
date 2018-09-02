from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView


#제네릭뷰 : 장고에서 제공하는 여러가지 기능을 하는 뷰클래스
#class 뷰이름(제네릭뷰):
#ListView : 특정 객체의 목록을 다루는 기능을 가진 제네릭뷰
from django.views.generic.list import ListView 
import blog
from pip._vendor.requests.api import post
#render(request,'blog/index.html',{obj':obj})
class index(ListView):
    #template_name : html파일의 경로를 문자열로 저장 변수
    template_name = 'blog/index.html'
    #model : 어떤 모델클래스이 객체를 리스트업할 건지 명시하는 변수
    model= Post
    #context_object_name : 템플릿에서 사용할 객체 리스트를 저장한 변수 명 
    context_object_name = 'list'
    #paginate_by : 한 페이지에 몇개의 객체가 보여질지 설정하는 변수
    paginate_by = 5

def detail(request,post_id):
    obj = get_object_or_404(Post,pk=post_id)
    return render(request, "blog/detail.html", {'post':obj})


