from django import forms
from django.forms import ModelForm

from .models import server, type_of_server,user, services,application, applicaitonshasservices, overall

class DateInput(forms.DateInput):
    input_type = 'date'

class serverForm(ModelForm):
    class Meta:
        model = server
        fields = '__all__'

class type_of_serverForm(ModelForm):
    class Meta:
        model = type_of_server
        fields = '__all__'
class usersForm(ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class serviceForm(ModelForm):
    class Meta:
        model = services
        fields = '__all__'
        widgets = {
            'date_of_launch': DateInput(),
        }

class applicationsForm(ModelForm):
    class Meta:
        model = application
        fields = '__all__'

class apphasservicesForm(ModelForm):
    class Meta:
        model = applicaitonshasservices
        fields = '__all__'

class overallForm(ModelForm):
    class Meta:
        model = overall
        fields = '__all__'
