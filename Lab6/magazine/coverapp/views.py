from django.shortcuts import render
from .forms import MagazineForm

def magazine_cover(request):
    title_text = ''
    subtitle_text = ''
    font_size = 36
    font_color = '#ffffff'
    background_color = '#f4f4f4'  # Default background color
    image = None

    if request.method == 'POST':
        form = MagazineForm(request.POST, request.FILES)
        if form.is_valid():
            title_text = form.cleaned_data['title']
            subtitle_text = form.cleaned_data['subtitle']
            font_size = form.cleaned_data['font_size']
            font_color = form.cleaned_data['font_color']
            background_color = form.cleaned_data.get('background_color', '#f4f4f4')
            image = form.cleaned_data['image']

            return render(request, 'cover.html', {
                'title_text': title_text,
                'subtitle_text': subtitle_text,
                'font_size': font_size,
                'font_color': font_color,
                'background_color': background_color,
                'image': image,
            })
    else:
        form = MagazineForm()

    return render(request, 'cover.html', {'form': form})
