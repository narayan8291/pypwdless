# pypwdless - PasswordLess Authentication In Python

## Introduction
This python library can be used to generate one time JWT codes which can be sent to a user's email address for authentication purposes. The code can later be verified and extended for a native app session (similar to a magic link: https://auth0.com/docs/connections/passwordless/spa-email-link). 

## Available Functions
The python library exposes three functions which can be directly used:

### generateCode(email)
Used to generate a one-time code that can be sent to a user's email. This function returns a JSON web token (https://jwt.io/) in base64 encoded format.

### sendEmail(code)
Used to email the code to a user's email address.

### validateCode(returnToken,returnEmail="")
Used to validate a code. It takes two arguments where **returnEmail** is an optional argument.

## Usage - With pip
This python library has been published to **https://pypi.org** and hence can be installed using pip. 

```pip install pypwdless```

*NOTE: For sendEmail(code) function to work, it needs valid credentials for an SMTP server. This can be configured in **config.py** file installed under site-packages. Example: If virtualenv (venv) is used, the file can be found under {{homepath}}/venv/lib/python2.7/site-packages/pypwdless.*

## Usage - From Source Code
1. Create a python virtualenv. ```virtualenv venv```
2. Do ```source venv/bin/activate```
3. Clone this repo. 
4. Install dependencies (PyJwt) mentioned in requirements.txt. Use pip install -r pypwdless/requirements.txt
5. Start using the functions provided by the code.

*NOTE: For sendEmail(code) function to work, it needs valid credentials for an SMTP server. This can be configured in **config.py** file.*

## Working
1. Generate a code using **generateCode** for an email address. This function will return a code. 
2. This code can be emailed to a user's email address using **sendEmail**. *NOTE: This function requires changes to config.py file which has been discussed previously*. This function will return **True** if successful. If not, it will return **False** with an error statement.
3. Now, the same code can be validated using **validateCode** which returns **True** when validation is successful. If not, it will return **False** and the error statement (expired, invalid token, code not associated with an email address)

## Test Code
```
from pypwdless import pwdless

if __name__ == "__main__":
	code = pwdless.generateCode("<email address>") # Should return the code (base64 encode format)
	print pwdless.sendEmail(code) # Should return True
	print pwdless.validateCode(code) # Should return True
```

## Benefits
- One-time code
- Configurable TTL and code length
- Stateless. Using JWT
- Configurable SMTP server. For emails

## Questions
Reach out to gowrajn@gmail.com or raise an issue/request here.
