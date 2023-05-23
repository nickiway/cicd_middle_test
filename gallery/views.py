from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Image


class gallery_view(View):
    def get(self, request):
        categories = Image.objects.values('category').distinct()
        return render(request, 'gallery.html', {'categories': categories})

class image_detail(View):
    def get(self, request, id):
        image = Image.objects.get(id=id)
        return render(request, 'image_detail.html', {'image': image})