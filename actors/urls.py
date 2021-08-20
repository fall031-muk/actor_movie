from django.urls import path
from django.urls.resolvers import URLPattern

from actors.views import ActorsView, MoviesView

urlpatterns = [
    path('', ActorsView.as_view()),
    path('/movies', MoviesView.as_view()),
]
