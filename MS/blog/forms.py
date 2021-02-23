from django import forms
# from .models import Comment


class EmailPostForm(forms.Form):
    Отправитель = forms.CharField(max_length=25)
    Адрес_отправителя = forms.EmailField()
    Кому = forms.EmailField()
    Комментарии = forms.CharField(required=False,
                               widget=forms.Textarea)


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')