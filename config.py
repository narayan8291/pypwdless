import time
codeTTL = 10 # Value is always in minutes
baseURL = "" # Example: https://example.com
jwtSecret = "bii23enzlkndas" # Change it to your value
tokenMetaData = {}
tokenMetaData['iat'] = int(time.time())
tokenMetaData['nbf'] = int(time.time())
tokenMetaData['exp'] = int(time.time()) + codeTTL * 60
tokenMetaData['iss'] = baseURL
emailMetaData = {"smtp-server":"smtp.gmail.com","port":587,"username":"","password":"","subject":"One Time Code","text":"One Time Code: "}