
from django.forms.models import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        models = Post 
        fields = ['type','headline','content']
        #exclude = ['pub_date','author']
        
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        #사용자가 글 종류를 선택하지 않았을때의 기본값
        self.fields['type'].empty_label = None
        self.fields['type'].label = "글종류"