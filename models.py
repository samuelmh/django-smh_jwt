#from django.db import models

from django.conf import settings

import datetime
import jwt

class IdToken():
    
    @classmethod
    def encode_from_user(cls,user):
        retval = {'error':'Account dissabled.'}
        if user is not None and user.is_active:
            claims = {'username': user.username}
            retval = {'jwt': cls.encode(claims)}
        return(retval)      
            
    
    @staticmethod
    def encode(payload):
        now = int(datetime.datetime.utcnow().strftime("%s"))
        payload.update({
            'exp': now+(settings.JWT_DURATION*60), #EXPiration time
            'nbf': now, #Not BeFore time
            'iat': now  #Issued AT  time
        })
        return(jwt.encode(payload=payload,key=settings.JWT_KEY))
        
      
    @staticmethod  
    def decode(token):
        return(jwt.decode(
            jwt=token,
            key=settings.JWT_KEY,
            leeway = settings.JWT_LEEWAY
        ))
    
    
    @classmethod
    def decode_from_request(cls, request):
        return(cls.decode(request.META['HTTP_AUTHORIZATION']))