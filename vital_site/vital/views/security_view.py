from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from ..forms import Registration_form
from ..models import VLAB_User
import logging

logger = logging.getLogger(__name__)

def register(request):
    logger.debug("in register")
    if request.method == 'POST':
        form = Registration_form(request.POST)
        form.clean()
        if form.is_valid():
            user = form.save(commit=False)
            logger.debug(user)
            try:
                user_from_databse = VLAB_User.objects.get(email=user.email)
                return render(request, 'vital/userreg.html',{'error_message' : 'User already registered'})
            except VLAB_User.DoesNotExist:
                user.save()
                return HttpResponseRedirect("/testapp/users")
    else:
        form = Registration_form()

    return render(request, 'vital/userreg.html', {'form': form})