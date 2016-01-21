from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
import logging


@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    logger = logging.getLogger(__name__)
    logger.info("user logged in: %s at %s" % (user, request.META['REMOTE_ADDR']))


@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    logger = logging.getLogger(__name__)
    logger.info("user logged out: %s at %s" % (user, request.META['REMOTE_ADDR']))
    # do machine shut down and other cleanup activities here

# this still would require a cron job to make sure that logged out on browser close can be handled - cron.py
