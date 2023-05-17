from django import forms

class MerchantUploadForm(forms.Form):
    file = forms.FileField(required=True)