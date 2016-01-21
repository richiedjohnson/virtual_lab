from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


@login_required(login_url='/vital/login/')
def advising_courses(request):
    logger.debug("In registered courses")
    ########## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    return render(request, 'vital/course_detail.html', {'virtual_machines': virtual_machines})
