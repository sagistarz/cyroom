# from .models import Comment
# from django import forms


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']

#         widgets = {
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#         }

from django import forms
from .models import Comment, Answer

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '2',
                   'placeholder': 'Write some comments...',
                   'value': 'none',
                   'class': 'form-control mt-1 mb-3',
                   }
        ))

    class Meta:
        model = Comment
        fields = ['content']

class AnswerForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Write your answer...',
                   'value': 'none',
                   'class': 'form-control mt-1 mb-3',
                   }
        ))
    snippet = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Add code...',
                   'value': 'none',
                   'class': 'form-control mt-1 mb-3',
                   }
        ))

    class Meta:
        model = Answer
        fields = ['content', 'snippet']