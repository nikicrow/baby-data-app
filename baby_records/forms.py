from django import forms
from .models import Toileting, BreastFeeding, BottleFeeding, Sleeping, Growth
  
poo_colours_choices = [
    ('brown', 'Brown'),
    ('yellow', 'Yellow'),
    ('orange', 'Orange'),
    ('red', 'Red'),
    ('green', 'Green'),
    ('black', 'Black'),
]

nap_quality_choices = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

boob_choices = [
    ('left', 'Left'),
    ('right', 'Right'),
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
            'poo_colour' : forms.Select(choices=poo_colours_choices),
            'toilet_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }

class BottleFeedingForm(forms.ModelForm):

    class Meta:
        model = BottleFeeding
        fields = ('drinking_ml','drinking_time','feed_time','notes')

        widgets = {
            'drinking_ml':forms.NumberInput(),
            'drinking_time':forms.NumberInput(),
            'feed_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }

class BreastFeedingForm(forms.ModelForm):

    class Meta:
        model = BreastFeeding
        fields = ('which_boob_first','right_boob_time','left_boob_time','feed_time','notes')

        widgets = {
            'which_boob_first': forms.Select(choices=boob_choices),
            'right_boob_time':forms.NumberInput(),
            'left_boob_time':forms.NumberInput(),
            'feed_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }

class SleepingForm(forms.ModelForm):

    class Meta:
        model = Sleeping
        fields = ('nap_length','nap_quality','nap_location','nap_start_time','notes')

        widgets = {
            'nap_length':forms.NumberInput(),
            'nap_quality' : forms.Select(choices=nap_quality_choices),
            'nap_location':forms.TextInput(attrs={'required': False}),
            'nap_start_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }


class GrowthForm(forms.ModelForm):

    class Meta:
        model = Growth
        fields = ('head_circumference','height','weight','measurement_time','notes')

        widgets = {
            'head_circumference':forms.NumberInput(),
            'height':forms.NumberInput(),
            'weight':forms.NumberInput(),
            'measurement_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'notes':forms.TextInput(attrs={'required': False})
        }
