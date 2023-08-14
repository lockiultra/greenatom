from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Movie, Review
from .forms import ReviewForm
from .utils import *

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'movies/index.html', {'title': 'Main page'})

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'

    
class MovieView(View):
    def get(self, request, pk):
        reviews = Review.objects.filter(movie_id=pk)
        return render(request, 'movies/movie.html', {'title': 'Movie page', 'movie': Movie.objects.get(pk=pk), 'reviews': reviews})

class AddReviewView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return render(request, 'movies/add_review.html', {'title': 'Add review page', 'form': ReviewForm(), 'movie': movie})
    
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form.cleaned_data['movie'] = movie
            form.cleaned_data['status'] = get_review_status(form.cleaned_data['content'])
            form.cleaned_data['rating'] = get_review_rating(form.cleaned_data['content'])
            Review.objects.create(**form.cleaned_data)
        return redirect('movie_detail', pk)