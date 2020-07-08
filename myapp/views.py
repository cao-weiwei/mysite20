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
def index(request):
    """
    the index page of myapp
    """
    # for displaying topics
    top_list = Topic.objects.all().order_by('id')[:10]
    data = {
        'top_list': top_list,
    }
    return render(request, 'myapp/index0.html', data)
    # response = HttpResponse()
    # heading1 = '<h2>' + 'List of topics: ' + '</h2>'
    # response.write(heading1)
    # for topic in top_list:
    #     para = '<p>' + str(topic.id) + ': ' + str(topic) + "<li> <a href='"+str(topic.id)+"'/ > Detail </a></li> " + '</p>'
    #     response.write(para)
    #
    # # for displaying courses
    # course_list = Course.objects.all().order_by('price').reverse()[:5]
    # heading1 = '<h2>' + 'List of courses: ' + '</h2>'
    # response.write(heading1)
    # for course in course_list:
    #     if course.for_everyone:
    #         para = '<p> {}: {}, {}. This Course is For Everyone!</p>'.format(course.id, course.name, course.price)
    #     else:
    #         para = '<p> {}: {}, {}. This Course is Not For Everyone!</p>'.format(course.id, course.name, course.price)
    #     response.write(para)
    #
    # return response


# about page
def about(request):
    """
    the about page of myapp
    """
    response = HttpResponse()
    heading1 = '<h2>' + 'This is an E-learning Website!Search our Topics to find all available Courses.' + '</h2>'
    response.write(heading1)
    return response


# detail page
def detail(request, top_no):
    """
    the detail page of myapp
    """
    response = HttpResponse()
    heading1 = '<h2>' + 'This is detail information for topic ' + top_no + '</h2>'
    response.write(heading1)
    topic = Topic.objects.get(id=top_no)
    print(topic.name)
    para = '<p>' + 'topic number = ' + str(top_no) + '<br>' + str(topic) + '<p>'
    response.write(para)

    course = Course.objects.all().filter(topic=topic)
    str0 = ""
    for cour in course:
        str0 = str0 + str(cour) + '<br>'
    para0 = '<p>' + 'Course information: <br>' + str0 + '<p>'
    response.write(para0)
    return response
