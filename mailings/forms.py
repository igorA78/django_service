from django import forms

from mailings.models import Mailing, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control fs-5'
            if isinstance(field.widget, forms.widgets.Textarea):
                field.widget.attrs['rows'] = 3


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ['owner']


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = [
            'mailing',
            # 'comment',
        ]
