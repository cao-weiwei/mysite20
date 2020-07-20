from django.shortcuts import render
# Create your views here.

# Import necessary classes
from django.http import HttpResponse
# from pandas.tests.extension import decimal

from .forms import *
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
    cours = Course.objects.all().filter(topic_id=top_no)
    data = {
        'topic': topic,
        'cour': cours,
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
        'your_name': "UWindsor",
    }

    return render(request, 'myapp/index.html', data)


def courses(request):
    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist})


def place_order(request):
    text = "You can place an order here."
    msg = ''
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_status = 1
            if order.levels <= order.course.stages:
                stu = order.student
                course = order.course
                level = order.levels
                price = course.discount()
                print(price)
                order.save()
                msg = 'Your course has been ordered successfully.'
                return render(request, 'myapp/order_response.html',
                              {'msg': msg, 'student': stu, 'course': course, 'level': level, 'price': price})
            else:
                msg = 'You exceeded the number of levels for this course.'
                return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist, 'text': text})


def course_detail(request, cour_id):

    if request.method == 'POST':  # show interests in the current course
        form = InterestForm(request.POST)

        print(form)
        # print(form.interested)
        if form.is_valid():
            course = Course.objects.get(id=cour_id)
            # course = form.save(commit=False)
            course.interested += 1
            # print(course.id)
            course.save()
            top_list = Topic.objects.all().order_by('id')[:10]
            data = {
                'top_list': top_list,
                'your_name': "UWindsor",
            }
            return render(request, 'myapp/index.html', data)

    else:
        course = Course.objects.filter(id=cour_id)
        form = InterestForm()
        # form.interested = '1'
        data = {'form': form, 'course': course, 'course_id': cour_id}
        return render(request, 'myapp/course_detail.html', data)
