from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from ..models import Course
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.debug("In index")
    # this is a sample service to get started
    active_courses = Course.objects.filter(status='ACTIVE')
    logger.debug(active_courses)
    #template = loader.get_template('courses/index.html')
    #context = {
    #    'active_courses': active_courses,
    #}
    #return HttpResponse(template.render(context, request))
    context = {'active_courses': active_courses}
    return render(request, 'vital/index.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'vital/course_detail.html', {'course': course})

def course_faculty(request, course_id):
    return HttpResponse("You are looking at faculty of course %s." % course_id)

def register_for_course(request, course_id):
    return HttpResponse("You are registering for course %s." % course_id)