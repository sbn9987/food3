from django.shortcuts import render, redirect, get_object_or_404
from .models import Add
from django.utils import timezone

# Create your views here.


def index(request):
    adds = Add.objects
    return render(request, 'diary/index.html', {'adds': adds})


def ABOUT(request):
    return render(request, 'diary/ABOUT.html')


def post(request):
    adds = Add.objects
    return render(request, 'diary/post.html', {'adds': adds})


def create(request):
    diary = Add()
    diary.foodName = request.GET['foodName']
    diary.pic = request.GET['pic']
    diary.GPS = request.GET['GPS']
    diary.taste = request.GET['taste']
    diary.date = timezone.datetime.now()
    diary.save()
    return redirect('/')


def food(request):
    return render(request, 'diary/food.html')


def login(request):
    return render(request, 'diary/login.html')

