from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=500, widget=forms.Textarea, required=True)
