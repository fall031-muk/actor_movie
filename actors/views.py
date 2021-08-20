from django import views
from django.db import models
from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from actors.models import Actor, Movie


class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)

        Actor.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            data_of_birth=data['birthday'],
        )
        return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            title_list = []
            results.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "title": title_list,
                }
            )
            titles = actor.movies.all()
            for title in titles:
                title_list.append(
                    {
                        "title": title.title
                    }
                )
        return JsonResponse({'results': results}, status=200)


class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)

        Movie.objects.create(
            title=data['title'],
            release_date=data['release_date'],
            running_time=data['running_time'],
        )
        return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actor_list = []
            results.append(
                {
                    "title": movie.title,
                    "running_time": movie.running_time,
                    "actor_name": actor_list
                }
            )
            actors = movie.actors.all()
            for actor in actors:
                actor_list.append(
                    {
                        "actor": actor.first_name
                    }
                )
        return JsonResponse({'results': results}, status=200)
