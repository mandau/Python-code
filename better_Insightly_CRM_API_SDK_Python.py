#A better way to access Insightly CRM API.
import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint

#e.g. Contact data request
j = requests.get('requests.get('https://api.insight.ly/v2.2/contacts/100000000', auth=HTTPBasicAuth 'Insightly API key goes here', ''))
d = json.loads(j.text)
#get contact info ID
pprint(d['CONTACTINFOS'][0]['CONTACT_INFO_ID'])
#other e.g. pprint(d)
#pprint(d['DATE_CREATED_UTC'])
