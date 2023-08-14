from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('movies/', MovieListView.as_view(), name='movies_list'),
    path('movie/<int:pk>', MovieView.as_view(), name='movie_detail'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),
]