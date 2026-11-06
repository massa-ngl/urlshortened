from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL
from .forms import URLForm
from django.db.models import F

# Create your views here.
def home(request):
    form = URLForm(request.POST or None)
    shortened_obj = None

    if request.method == 'POST' and form.is_valid():
        # Check if URL already exists or create new
        original_url = form.cleaned_data['original_url']
        shortened_obj, created = ShortenedURL.objects.get_or_create(original_url=original_url)
        form = URLForm()    # reset form

    return render(request, 'analytics_url/index.html', {
        'form': form,
        'shortened_obj': shortened_obj
    })

def redirect_url(request, short_code):
    url_instance = get_object_or_404(ShortenedURL, short_code=short_code)

    # Atmoically increment click counter to handle concurrent traffic safely
    ShortenedURL.objects.filter(id=url_instance.id).update(clicks=F('clicks') + 1)

    return redirect(url_instance.original_url)

def stats_view(request, short_code):
    url_instance = get_object_or_404(ShortenedURL, short_code=short_code)
    return render(request, 'analytics_url/stats.html', {
        'url_instance': url_instance
    })