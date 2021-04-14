from flask import request, jsonify
import functools
from passlib.hash import sha256_crypt

'''
SECURE THE USER PASSWORDS
Store the user details in the database
Do not store the password in the database, instead store a cryptographic hash of the password.
Make sure that the password is salted, and that the salt is unique for each user. This helps significantly slows down intruders if they gain access to the usernames and password hashes.
'''
# users = {"Booker": "password",
#          "Annabel": "password",
#          "Steve": "password",
#          "Tawny": "password",
#          "Kasha": "password",
#          "Tameika": "password",
#          "Marie": "password",
#          "Samual": "password",
#          "Cyrus": "password",
#          "Joya": "password"}

# passlib created unique password, no need to manually add salt
users = {"Booker": sha256_crypt.hash("password"),
         "Annabel": sha256_crypt.hash("password"),
         "Tawny": sha256_crypt.hash("password"),
         "Kasha": sha256_crypt.hash("password"),
         "Tameika": sha256_crypt.hash("password"),
         "Marie": sha256_crypt.hash("password"),
         "Samual": sha256_crypt.hash("password"),
         "Cyrus": sha256_crypt.encrypt("password"),
         "Joya": sha256_crypt.hash("password")}



'''
General background:
- 200 for authorized, 401 for unauthorized that states that basic authentication is needed should be returned
- When a browser receives this info, it'll bring up a login dialog
- logging in creates a new request with an Authentication header containing
    username and password
    ^--------- to achieve this: use wrap decorator in functools library
to create an authorization decorator that can be used on any function.
'''

'''
@requires_authorization function flow; 
- define a wrapper to check auth header of an incoming request
    + 1. read auth header by accessing request.authorization
    + 2. check if header was provided: `if not auth or not ok_user_and_password(auth.user, auth.password)`
    + 3. if header was provided passes the details to ok_user_and_password method: `return f(*args, **kwargs)
    + 4. ok_user_and_password method needs to decide whether the user has provided valid crednetials
'''

def ok_user_and_password(username, password):
    """Test whether the supplied username and password match."""
    return users.get(username) == password


def authenticate():
    """ Return a response indicating a failure to authenticate."""
    message = {'message': "Authenticate."}
    resp = jsonify(message) # create a json object

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp


def requires_authorization(f):
    """A python decorator which requires HTTP basic authentication."""
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization  #read auth header
        # check if auth header is provided
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        # if auth header is provided, pass details to ok_user_and_password method
            # https://www.programiz.com/python-programming/args-and-kwargs#:~:text=*args%20and%20**kwargs%20are,to%20take%20variable%20length%20argument.&text=**kwargs%20passes%20variable%20number,a%20dictionary%20can%20be%20performed.
            # *args: non-keyword arg; not sure how many args; take as a LIST 
            # **kwargs: keyword arg; DICTIONARY - handle named arguments that need not defined in advance
        return f(*args, **kwargs) 
    return decorated

