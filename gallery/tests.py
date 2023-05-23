from django.test import TestCase
from .models import Image, Category
from django.urls import reverse

class TestGallery(TestCase):
    def test_gallery_view_success(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    # def test_gallery_view_categories(self):
    #     response = self.client.get(reverse('main'))

    #     category_1 = Category.objects.create(name="category one")
    #     category_2 = Category.objects.create(name="category two")
    #     category_3 = Category.objects.create(name="category three")

    #     categories = response.context['categories']

    #     self.assertEqual(len(categories), 0)
    #     self.assertEqual(set(categories), {category_3, category_2, category_1})

class TestImageDetail(TestCase):
    def test_image_detail_view_success(self):
        category = Category.objects.create(name='category one')
        image = Image.objects.create(title='image1', image='free-icon-github-3291695_HOUsBmM.png', created_date="2023-05-23", age_limit=16)
        image.categories.add(category)

        path = reverse('image_detail', args=[image.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
    
    def test_image_detail_view_image(self):
        category = Category.objects.create(name='category 1')
        image = Image.objects.create(title='image1', image='free-icon-github-3291695_HOUsBmM.png', created_date="2023-05-23", age_limit=16)
        image.categories.add(category)
        
        path = reverse('image_detail', args=[image.id])
        response = self.client.get(path)

        self.assertEqual(response.context["image"], image)