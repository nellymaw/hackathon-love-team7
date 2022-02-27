# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout, Field
from crispy_forms.bootstrap import FormActions
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Reply, Letter



class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)

class LetterForm(forms.ModelForm):
    """
    A class for Letter
    """
    class Meta:
        model = Letter
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        """
        docstring
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        # self.fields['created_on'].label = False
        self.fields['body'].label = False
        # self.fields["has_unseen_reply"].label = False
       
        self.helper.layout = Layout(
            Field(
                "body",
                placeholder="Make this interesting"),
         
                FormActions(
                    Submit(
                        "submit",
                        "Throw your bottle into ocean",
                        css_class="btn btn-secondary"
                        )
                    ),
                )
        
