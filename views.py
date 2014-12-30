from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import json

from smh_jwt.models import IdToken



@require_http_methods(['POST'])
@csrf_exempt
def id_token(request):
    retval = {'error':'Wrong credentials.'}
    try:
        data = json.loads(request.body)
        user = authenticate(username=data['username'],password=data['password'])
        retval = IdToken.encode_from_user(user)
    except:
        pass
    return(JsonResponse(retval))


@require_http_methods(['GET'])
def id_token_session(request):
    retval = {'error':'Not in session.'}
    user = request.user
    if user.is_authenticated():
        retval = IdToken.encode_from_user(user)
    return(JsonResponse(retval))