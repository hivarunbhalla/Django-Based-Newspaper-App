from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

    def save(self, commit=True, author=None):
        instance = super().save(commit=False)
        if author:
            instance.author = author
        if commit:
            instance.save()
        return instance