from django import forms
from .models import Toileting, Feeding
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
  
POO_COLOURS_CHOICES = [
    ('brown', 'Brown'),
    ('yellow', 'Yellow'),
    ('orange', 'Red'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ToiletingForm(forms.ModelForm):

    class Meta:
        model = Toileting
        fields = ('pee','pee_scale','poo','poo_scale','poo_colour','toilet_time','notes')

        widgets = {
            'pee': forms.CheckboxInput(),
            'pee_scale':forms.NumberInput(),
            'poo': forms.CheckboxInput(),
            'poo_scale':forms.NumberInput(),
            'poo_colour' : forms.Select(choices=POO_COLOURS_CHOICES),
            'toilet_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }

class FeedingForm(forms.ModelForm):

    class Meta:
        model = Feeding
        fields = ('right_boob_first','right_boob_time','left_boob_first','left_boob_time','feed_time','notes')

        widgets = {
            'right_boob_first': forms.CheckboxInput(),
            'right_boob_time':forms.NumberInput(),
            'left_boob_first': forms.CheckboxInput(),
            'left_boob_time':forms.NumberInput(),
            'feed_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }

