from django import forms
from .models import Blog


#class BlogPost(forms.ModelForm):
#    class Meta:
#        model = Blog #model의 Blog를 기반으로 한 입력공간
#        fields = ['title', 'body'] #그 중에서 title과 body를 입력받을 수 있는 공간

class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'), ('3', 'three')])
        