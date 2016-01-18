from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Course
from ..models import  Registered_Courses
from ..forms import Course_Registration_Form
from ..utils import audit
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@login_required(login_url='/vital/login/')
def index(request):
    logger.debug("In index")
    # this is a sample service to get started
    active_courses = Course.objects.filter(status='ACTIVE')
    logger.debug(active_courses)
    context = {'active_courses': active_courses}
    return render(request, 'vital/index.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'vital/course_detail.html', {'course': course})


@login_required(login_url='/vital/login/')
def registered_courses(request):
    logger.debug("In registered courses")
    reg_courses = request.user.registered_courses_set.all()
    courses = []
    message = ''
    if len(reg_courses) > 0:
        for reg_course in reg_courses:
            if reg_course.course.status=='ACTIVE':
                courses.append(reg_course.course)
    else:
        message = 'You have no registered courses'
    return render(request, 'vital/registered_courses.html', {'courses': courses, 'message':message})


@login_required(login_url='/vital/login/')
def register_for_course(request):
    logger.debug("in activate")
    error_message = ''
    if request.method == 'POST':
        form = Course_Registration_Form(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['course_registration_code']+"<>"+str(request.user.id)+"<>"+
                         str(request.user.is_faculty))
            try:
                course = Course.objects.get(registration_code=form.cleaned_data['course_registration_code'])
                user = request.user
                try:
                    if user.registered_courses_set.get(course_id=course.id):
                        error_message = 'You have already registered for this course'
                except Registered_Courses.DoesNotExist:
                    user.registered_courses_set.create(course_id=course.id)
                    audit(request, user, 'User registered for new course -'+course.id)
                    # PLACE TO DO CREATING VMS FOR USER FOR THE COURSE
                    return redirect('/vital/courses/registered/')
            except Course.DoesNotExist:
                error_message = 'Invalid registration code. Check again.'
    else:
        form = Course_Registration_Form()
    return render(request, 'vital/course_register.html', {'form': form, 'error_message': error_message})