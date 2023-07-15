from django import forms
from .models import *

class conversationmessageform(forms.ModelForm):
    class Meta:
        model=conversationmessage
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }