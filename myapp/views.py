from django.shortcuts import render

# Create your views here.

# Import necessary classes
from django.http import HttpResponse
from .models import Topic, Course, Student, Order


def home(request):
    """
    default homepage for 127.0.0.1:8000, users can select the landing web-page
    """
    content = "<h1> Welcome! </h1> " \
              "<p> Please select the pages: </p> " \
              "<ul> " \
              "<li> <a href={}> Courses </a></li> " \
              "<li> <a href={}> About </a></li> " \
              "</ul>".format('myapp/', 'myapp/about/')
    return HttpResponse(content)


# Create your views here.
def index0(request):
    """
    the index page of myapp
    """
    # for displaying topics
    top_list = Topic.objects.all().order_by('id')[:10]
    data = {
        'top_list': top_list,
    }
    return render(request, 'myapp/index0.html', data)


# about page
def about(request):
    """
    the about page of myapp
    """
    text = 'This is an E-learning Website!Search our Topics to find all available Courses.'
    data = {
        'text': text,
    }
    return render(request, 'myapp/about.html', data)


# detail page
def detail(request, top_no):
    """
    the detail page of myapp
    """
    topic = Topic.objects.all().filter(id=top_no)
    courses = Course.objects.all().filter(topic_id=top_no)
    data = {
        'topic': topic,
        'courses': courses,
    }
    return render(request, 'myapp/detail.html', data)


def index(request):
    """
       the index page of myapp
       """
    # for displaying topics
    top_list = Topic.objects.all().order_by('id')[:10]
    data = {
        'top_list': top_list,
    }

    return render(request, 'myapp/index.html', data)
