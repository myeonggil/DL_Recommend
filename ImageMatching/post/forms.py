from django import forms
from .models import Comment, Post, Learning_Result


class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False)
    """content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.\n#태그명 을 통해서 검색 태그를 등록할 수 있습니다.', }))"""

    class Meta:
        model = Post
        # fields = ['photo', 'content']
        fields = ['photo']

class ResultForm(forms.ModelForm):
    result_img = forms.ImageField(label='', required=False)
    class Meta:
        model = Learning_Result
        fields = ['result_img']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '70px',
        'placeholder': '댓글 달기...',
        'maxlength': '40', }))

    class Meta:
        model = Comment
        fields = ['content']
