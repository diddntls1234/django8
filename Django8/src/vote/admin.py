from django.contrib import admin
from .models import Question, Choice #models안에있는 Qeustion,Choice 추가 
#from .models import * #models.py 내에 있는 클래스, 함수를 전부추가\

#목록화면에 id, question_text, pub_date가 보이더록 설정
class QuestionAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'question']
    list_display = ('id','choice_text','votes','question')
    
    
class ChoiceAdmin(admin.ModelAdmin): 
    list_display = ('id','choice_text','votes','pub_date')
    # Register your models here.
#Question 모델클래스를 관리자사이트에서 접근할 수 있도록 설정
admin.site.register(Question)
admin.site.register(Choice)