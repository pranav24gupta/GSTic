from django import forms
from .models import sub_category

class PersonForm(forms.ModelForm):
    class Meta:
        model = sub_category
        fields = ('category','sub_cat')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_cat'].queryset = sub_category.objects.none()