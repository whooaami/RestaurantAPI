from django.urls import path
from . import views

urlpatterns = [
    path('votes/<int:menu_id>/results/', views.VoteResultsAPIView.as_view()),
]
