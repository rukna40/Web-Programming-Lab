from django import forms

class MagazineForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    subtitle = forms.CharField(label='Subtitle', max_length=100)
    image = forms.ImageField(label='Upload Image')
    background_color = forms.CharField(
        label='Background Color',
        initial='#f4f4f4',
        widget=forms.widgets.Input(attrs={'type': 'color'})
    )
    font_size = forms.IntegerField(label='Font Size', initial=36)
    font_color = forms.CharField(
        label='Font Color',
        initial='#ffffff',
        widget=forms.widgets.Input(attrs={'type': 'color'})
    )
