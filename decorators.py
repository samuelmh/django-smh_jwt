from django.http import JsonResponse
from smh_jwt.models import IdToken


def jwt_required(func):
    def inner(request, *args, **kwargs):
        error = False
        try: 
            token = IdToken.decode_from_request(request)          
        except:
            error = JsonResponse({'error': 'Wrong Id Token.'})
        if error:
            retval = error
        else:        
            request.jwt = token
            retval = func(request, *args, **kwargs)
        return(retval)
    return inner
