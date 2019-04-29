import jwt
import string, random, time, smtplib, base64
import config as cfg # Config file

def generateCode(email):
	metadataDict = {}
	cfg.tokenMetaData['jti'] = oneTimeNonce()
	cfg.tokenMetaData['issuedFor'] = email
	jwtToken = jwt.encode(cfg.tokenMetaData, cfg.jwtSecret , algorithm='HS256')
	return cfg.baseURL + base64.b64encode(jwtToken)

def sendEmail(code):
	try:
		tokenMetaData = jwt.decode(trimToken(code), cfg.jwtSecret , algorithms=['HS256'])
		recipientEmailAddress = tokenMetaData['issuedFor']
		if cfg.emailMetaData:
			message = 'Subject: {}\n\n{}'.format(cfg.emailMetaData["subject"], cfg.emailMetaData["text"] + str(code))
			server = smtplib.SMTP(cfg.emailMetaData["smtp-server"],cfg.emailMetaData["port"])
			server.ehlo()
			server.starttls()
			server.login(cfg.emailMetaData["username"], cfg.emailMetaData["password"])
			server.sendmail(cfg.emailMetaData["username"], recipientEmailAddress, message)
			server.close()
			return True
	except Exception as e:
		print "Failed to send email. Error ==> " + str(e)
		return False

def validateCode(returnToken,returnEmail=""):
	try:
		tokenMetaData = jwt.decode(trimToken(returnToken), cfg.jwtSecret , algorithms=['HS256'])
		# Validate JWT
		if tokenMetaData["exp"] < int(time.time()):
			print "Failed to validate returning token. Error ==> Token Expired"
			return False
		elif returnEmail != "":
			if tokenMetaData["issuedFor"] != returnEmail:
				print "Failed to validate returning token. Error ==> Code not associated with email address specified"
				return False
			return True
		else:
			return True
	except Exception as e:
		print "Failed to validate returning token. Error ==> " + str(e)
		return False

def oneTimeNonce(size=16, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def trimToken(code):
	returnTokenWithoutURL = code.replace(cfg.baseURL,"")
	return base64.b64decode(returnTokenWithoutURL)