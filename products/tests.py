from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Product, Category

User = get_user_model()

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Electronics')
        self.product_data = {
            'name': 'Smartphone',
            'price': '499.99',
            'description': 'A high-end smartphone.',
            'category': self.category.id
        }

    def test_create_product(self):
        url = reverse('product-create')
        response = self.client.post(url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Smartphone')

    def test_list_products(self):
        Product.objects.create(name='Laptop', price=999.99, description='Powerful laptop', category=self.category)
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_product_by_name(self):
        Product.objects.create(name='Laptop', price=999.99, description='Powerful laptop', category=self.category)
        Product.objects.create(name='Phone', price=499.99, description='Some phone', category=self.category)
        url = reverse('product-list') + '?search=Laptop'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Laptop')

    def test_filter_product_by_category(self):
        cat2 = Category.objects.create(name='Books')
        Product.objects.create(name='Laptop', price=999.99, description='Powerful laptop', category=self.category)
        Product.objects.create(name='Novel', price=19.99, description='A great book', category=cat2)
        url = reverse('product-list') + '?category=Electronics'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Laptop')

    def test_update_product(self):
        product = Product.objects.create(name='Laptop', price=999.99, description='Powerful laptop', category=self.category)
        url = reverse('product-detail', kwargs={'pk': product.pk})
        update_data = {'name': 'Gaming Laptop', 'price': '1200.00', 'description': 'Updated description'}
        response = self.client.patch(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, 'Gaming Laptop')

    def test_delete_product(self):
        product = Product.objects.create(name='Laptop', price=999.99, description='Powerful laptop', category=self.category)
        url = reverse('product-detail', kwargs={'pk': product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
