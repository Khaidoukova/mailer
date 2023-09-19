from django import forms

from mailsender.models import Mailing, Client


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('name', 'start_time', 'stop_time', 'frequency', 'status', 'client')


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'name', 'comment')

class ManagerUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('is_active')

