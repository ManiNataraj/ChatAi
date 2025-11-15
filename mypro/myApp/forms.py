from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label='Ask me something', max_length=200)
