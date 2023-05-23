from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from .models import Image


class GalleryViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('main')

    def test_gallery_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertContains(response, 'Categories')

    def test_gallery_view_categories(self):
        Image.objects.create(title='Test Image 1', image='image1.jpg', category='Category 1')
        Image.objects.create(title='Test Image 2', image='image2.jpg', category='Category 2')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['categories'],
            ['<Image: Category 1>', '<Image: Category 2>'],
            ordered=False
        )


class ImageDetailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.image = Image.objects.create(title='Test Image', image='test.jpg')
        self.url = reverse('image_detail', kwargs={'id': self.image.id})

    def test_image_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
        self.assertContains(response, self.image.title)
        self.assertContains(response, self.image.image.url)