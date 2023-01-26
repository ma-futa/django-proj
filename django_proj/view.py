
from http.client import HTTPResponse


def welcome(request):
    return HTTPResponse("Welcome!")