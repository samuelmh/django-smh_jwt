django-smh_jwt
==============

## Description
Django app to manage (issue, decode, etc) JSON WEB TOKENS (JWT).



## Deploy
Clone the project under the name **smh_jwt**
```
$ git clone https://github.com/samuelmh/django-smh_jwt.git smh_jwt
```

Set up the preferences in **settings.py**
```
#
### JWT MODULE
#
JWT_KEY = <str> #Key to encrypt the tokens EJ: SECRET_KEY  
JWT_DURATION = <int>  #Minutes id_token last EJ:60
JWT_LEEWAY = <int>    #Minutes id_token slack EJ:5
```

### Dependencies
- jwt - JSON Web Token implementation (Python)



## Functionality

### views.py

- id_token()
    - **DESCRIPTION**: get an identification JWT from the credentials.
    - **METHOD**: POST
    - **PARAMS**: JSON data
        - username: string, name of a registered user.
        - password: string, password of the registered user.
    - **EXAMPLE**: how to get a JWT from credentials.
```
$ curl -X POST -H "Content-Type: application/json" -d '{"username":"<username>","password":"<password>"}'  http://<id_token view>
```

- id_token_session()
    - **DESCRIPTION**: get an identification JWT from an active session. Useful for web apps.
    - **METHOD**: GET
    - **PARAMS**: None
    
- TODO
    - get refresh token
    - id_token from refresh token



### decorators.py

- jwt_required()
    - **DESCRIPTION**: requires an identification JWT in the HTTP Header `Authorization`. If the validation is correct, the decyphered info of the token will be available as a dictionary in the `request` object passed to the view. For example, `request.jwt['username']` will contain the username the token was issued for.
    - **EXAMPLE**: how to decorate an API Class based view.
    ``` 
    from django.utils.decorators import method_decorator
    from django.views.decorators.csrf import csrf_exempt
    from smh_jwt.decorators import jwt_required

    class MyClass(View):
        
        @method_decorator(csrf_exempt)
        @method_decorator(jwt_required)
        def dispatch(self, *args, **kwargs):
            return super(self.__class__, self).dispatch(*args, **kwargs)
    ```
    - **EXAMPLE**: how to call a jwt_required decorated view.
    ```
    curl -X GET http://<jwt_required view> -H 'Authorization:<JWT>'
    ```

   