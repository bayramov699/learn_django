from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "Your Title",
    }))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your Description",
        "class": "new-class two",
        "id": "my-id-for-textarea",
        "rows": "15",
        "cols": "75"
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "Your Title",
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Your Description",
        "class": "new-class two",
        "id": "my-id-for-textarea",
        "rows": "15",
        "cols": "75"
    }))
    price = forms.DecimalField(initial=199.99)
    
