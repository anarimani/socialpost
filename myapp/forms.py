from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
