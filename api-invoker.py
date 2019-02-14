import argparse
import requests

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--swagger", required=True,
	help="api swagger json file")
args = vars(ap.parse_args())

login_data = {
  'action': 'login',
  'username': 'admin',
  'password': 'admin'
}

login_resp = requests.post('http://localhost:9763/publisher/site/blocks/user/login/ajax/login.jag', data=login_data)

print(login_resp)
print(login_resp.text)


url = 'http://localhost:9763/publisher/site/blocks/item-add/ajax/add.jag'


swagger = open(args["swagger"])

swagger_str = swagger.read().replace('\n', '')

data = {
  'action': 'addAPI',
  'name': 'PhoneApi',
  'context': '/phonesample',
  'version': '1.0.0',
  'visibility': 'public',
  'thumbUrl': '',
  'description': 'Verify a phone number',
  'tags': 'phone,mobile,multimedia',
  'endpointType': 'nonsecured',
  'tiersCollection': 'Gold,Bronze',
  'http_checked': 'http',
  'https_checked': 'https',
  'swagger': swagger_str,
  'endpoint_config' : '{"production_endpoints":{"url":"http://ws.cdyne.com/phoneverify/phoneverify.asmx","config":null},"endpoint_type":"http"}'
}


r = requests.post(url, data=data, cookies=login_resp.cookies)

print(r)
print(r.text)
