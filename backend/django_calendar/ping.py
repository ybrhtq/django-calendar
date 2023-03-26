from rest_framework.status import HTTP_200_OK
from django.http import HttpResponse


def ping_view(request):
    return HttpResponse("OK", status=HTTP_200_OK)
