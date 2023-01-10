import json
import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def demand(request):
    return render(request, "demand.html")


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def last_vacancies(request):
    request_result = requests.get("https://api.hh.ru/vacancies?text=DevOps&per_page=10")
    last_at_hh = json.loads(request_result.text)
    return render(request, "last_vacancies.html", context=last_at_hh)
