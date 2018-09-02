'''
Created on 2018. 9. 2.

@author: KGITBANK403-21
'''
from django.shortcuts import get_object_or_404, render
from blog.models import Post
def detail(request, post_id):
    obj = get_object_or_404(Post,pk=post_id)
    return render(request,"blog/detail.html",{'post':obj})

def searchP(request):
    #<input type= "text"name="query"/>
    #GET요청으로 온 데이터에서 name속성이 'query'인 데이터 춫출
    #name속성이 'query'인 속성이 없으면 기본값''반환
    q = request.GET.get('query','')
    t = request.GET.get('type','0')
    #'0' : 제목 검색
    if t=='0':
        #Post.objects.filter(조건) : 특정 조건을 만족하는 Post 객체 추출
        #filter,exclude,get 함수 사용시 : 모델클래스에 정의한 변수명__명령어=값
        #contains : 우변값에 해당하는 문자열이 해당 객체의 변수에 저장되있는지 확인 
        list = Post.objects.filter(headline__contains=q)
        return render(request,'blog/searchP.html',{'list':list})
    #'1' : 내용검색
    elif t=='1':
        list = Post.objects.filter(content__contains=q)
        return render(request, 'blog/searchP.html',{'list':list})