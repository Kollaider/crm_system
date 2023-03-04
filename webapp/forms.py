from django import forms
from webapp.models import Office

# class OfficeForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     address = forms.CharField(label='Address', max_length=1)



class OfficeForm(forms.ModelForm):

    class Meta:
        model = Office
        # fields = '__all__'
        fields = ['name', 'address']
