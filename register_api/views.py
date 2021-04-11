from django.http import JsonResponse
from database.models import UserDetail
from logging_configuration import logging_config

logger = logging_config.get_logger()


def register_user(request):
    """
    This function accepts needed credentials and registered those into the database.
    :param request: It's accept the request with credentials and save into the database.
    :return: It's return a HttpResponse that the user is registered successfully or Not.
    """
    if request.method == 'POST':
        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            city = request.POST['city']
            username = request.POST['username']
            password = request.POST['password']
            user_detail = UserDetail(firstname=firstname, lastname=lastname, email=email, city=city, username=username,
                                     password=password)
            user_detail.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.exception(e)
            return JsonResponse({'status': 'user not registered!'})
    else:
        return JsonResponse({'status': 'failed'})
