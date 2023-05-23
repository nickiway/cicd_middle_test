from django.shortcuts import render, get_object_or_404
from .models import Category, Image

def gallery_view(request):
    return render(request, 'gallery.html', {
        'categories': Category.objects.all(),
    })

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {
        'image': image
    })