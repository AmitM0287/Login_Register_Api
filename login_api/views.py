from django.http import JsonResponse
from database.models import UserDetail
from logging_configuration import logging_config

logger = logging_config.get_logger()


def user_login(request):
    """
    This function checks weather the user is Logged In or Not.
    :param request: It's accept a request which include username & password.
    :return: It's return a HttpResponse that the user is Logged In successfully or Not.
    """
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user_detail = UserDetail.objects.get(username=username, password=password)
            if user_detail.username and user_detail.password:
                return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.exception(e)
            return JsonResponse({'status' : 'user does not exist!'})
    else:
        return JsonResponse({'status': 'failed'})
