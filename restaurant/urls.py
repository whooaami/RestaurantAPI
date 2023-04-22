from django.urls import path
from . import views
from menu.views import CurrentDayMenu, MenuUpload


urlpatterns = [
    path('restaurant/', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/menu/', CurrentDayMenu.as_view()),
    path('restaurant/<int:pk>/menus/', MenuUpload.as_view()),
]
