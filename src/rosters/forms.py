from tabnanny import check
from django import forms


class AddGenreForm(forms.Form):
    name = forms.CharField(
        label='Genre name',
        required=True,
        help_text='Fill in a genre name'
    )
    description = forms.CharField(
        label='Genre description',
        required=False,
        help_text='Fill in a genre description',
        widget=forms.Textarea
    )


class AddAuthorForm(forms.Form):
    name = forms.CharField(
        label='Author name',
        required=True,
        help_text="Fill in Author's name"
    )
    description = forms.CharField(
        label='Author description',
        required=False,
        help_text='Fill in a Author description',
        widget=forms.Textarea
    )


class AddSeriesForm(forms.Form):
    name = forms.CharField(
        label='Series name',
        required=True,
        help_text="Fill in Series name"
    )
    description = forms.CharField(
        label='Series description',
        required=False,
        help_text='Fill in a Series description',
        widget=forms.Textarea
    )


class AddPubl_houseForm(forms.Form):
    name = forms.CharField(
        label='Publ_house name',
        required=True,
        help_text="Fill in Publ_house name"
    )
