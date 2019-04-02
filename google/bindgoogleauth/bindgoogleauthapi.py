from django.shortcuts import render,HttpResponse
from django_google_auth2.google.bindgoogleauth.bindgoogleauth import bind_google_auth
import json


def bind_google_auth_api(request):

    body = json.loads(request.body)

    data= bind_google_auth(body["user"])

    status = data["success"]

    if not status:
        return HttpResponse(data["data"])

    return render(request, 'google.html', {"qr_code": data["data"]})