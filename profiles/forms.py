from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """sldvnhsl"""
    
    class Meta:
        model = Profile
        exclude = ('user',)

    


# class ProfileUpdateForm():
    

    

        # self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if field != 'default_country':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = ('border-black '
        #                                                 'rounded-0 '
        #                                                 'profile-form-input')
        #     self.fields[field].label = False