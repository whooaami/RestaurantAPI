import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Restaurant


@pytest.mark.django_db
class TestRestaurantList:

    def test_get_restaurants(self):
        client = APIClient()
        url = reverse('restaurant_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestRestaurantDetail:

    def test_get_restaurant(self):
        client = APIClient()
        restaurant = Restaurant.objects.create(name='Test Restaurant', location='Test Location')
        url = reverse('restaurant_detail', kwargs={'pk': restaurant.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Test Restaurant'

    def test_update_restaurant(self):
        client = APIClient()
        restaurant = Restaurant.objects.create(name='Test Restaurant', location='Test Location')
        url = reverse('restaurant_detail', kwargs={'pk': restaurant.pk})
        data = {'name': 'Updated Restaurant'}
        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert Restaurant.objects.get().name == 'Updated Restaurant'

    def test_delete_restaurant(self):
        client = APIClient()
        restaurant = Restaurant.objects.create(name='Test Restaurant', location='Test Location')
        url = reverse('restaurant_detail', kwargs={'pk': restaurant.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Restaurant.objects.count() == 0
