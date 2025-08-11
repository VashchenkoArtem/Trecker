from django import forms


class ReviewForm(forms.Form):
    message = forms.CharField(label = "Коментар", widget = forms.Textarea(attrs = {
        "class": "message-field"
        }))
    