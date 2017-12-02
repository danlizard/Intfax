from requests import *
def Parse(target):
	req_url = 'https://mercury.postlight.com/parser?url=' + target
	A = get(req_url, data = {'Content-Type': 'application/json',
    						'x-api-key': 'DhHPB5BInYmKFDRogGjkqCGm8uNK8nwNVHq5kIx9'})
	A = A.text
	return A
x = input()
print(Parse(x))