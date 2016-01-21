from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Course, Registered_Courses, Virtual_Machines
from ..forms import Course_Registration_Form
from ..utils import audit
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@login_required(login_url='/vital/login/')
def index(request):
    logger.debug("In index")
    user = request.user
    if not user.is_faculty and not user.is_admin:
        return redirect('/vital/courses/registered')  # change here to home page
    elif user.is_faculty:
        logger.debug('user is a faculty')
        return redirect('/vital/courses/registered')  # change here to home page
    else:
        logger.debug('user is admin')


@login_required(login_url='/vital/login/')
def registered_courses(request):
    logger.debug("In registered courses")
    reg_courses = Registered_Courses.objects.filter(user_id=request.user.id)
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
def course_detail(request, course_id):
    logger.debug("in course detail")
    virtual_machines = Virtual_Machines.objects.filter(course_id=course_id)
    return render(request, 'vital/course_detail.html', {'virtual_machines': virtual_machines})


@login_required(login_url='/vital/login/')
def unregister_from_course(request, course_id):
    logger.debug("in course unregister")
    user = request.user
    reg_courses = Registered_Courses.objects.filter(course_id=course_id, user_id=user.id)
    course_to_remove = reg_courses[0]
    audit(request, course_to_remove, 'User '+str(user.id)+' unregistered from course -'+str(course_id))
    course_to_remove.delete()
    course = Course.objects.get(pk=course_id)
    course.students_registered -= 1
    course.save()
    return redirect('/vital/courses/registered/')


def dummy_console(request):
    return render(request, 'vital/dummy.html')


@login_required(login_url='/vital/login/')
def register_for_course(request):
    logger.debug("in register for course")
    error_message = ''
    if request.method == 'POST':
        form = Course_Registration_Form(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['course_registration_code']+"<>"+str(request.user.id)+"<>"+
                         str(request.user.is_faculty))
            try:
                course = Course.objects.get(registration_code=form.cleaned_data['course_registration_code'])
                user = request.user
                values = Registered_Courses.objects.filter(course_id=course.id, user_id=user.id)
                if len(Registered_Courses.objects.filter(course_id=course.id, user_id=user.id)) > 0:
                        error_message = 'You have already registered for this course'
                else:
                    if course.has_free_slots():
                        registered_course = Registered_Courses(course_id=course.id, user_id=user.id)
                        registered_course.save()
                        course.students_registered += 1
                        course.save()
                        audit(request, registered_course, 'User '+str(user.id)+' registered for new course -'+str(course.id))
                        # PLACE TO DO CREATING VMS FOR USER FOR THE COURSE
                        return redirect('/vital/courses/registered/')
                    else:
                        error_message = 'The course has reached its maximum student capacity.'
            except Course.DoesNotExist:
                error_message = 'Invalid registration code. Check again.'
    else:
        form = Course_Registration_Form()
    return render(request, 'vital/course_register.html', {'form': form, 'error_message': error_message})