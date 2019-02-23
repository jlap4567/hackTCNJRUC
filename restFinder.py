import json
import requests


url = 'https://api.foursquare.com/v2/venues/search'

params = dict(
  client_id='0EZFGLHNEGBO3CL5WY4QQK1G0AASQMQU5A3R0EQMUA1FVP15',
  client_secret='KIDTS2WYUFFMWEAKS0VSCTPFWZUTMCOJK1LBIH1VAVVHWRPU',
  v='20180323',
  ll='40.7243,-74.0018',
  #query='coffee',
  #limit=10
  intent = 'checkin'
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
#print(data)

#for x in data['response']['venues']:
#	print(x['name'])
#	print(x['location'])
venues = data['response']['venues']
#for x in venues:
#	y = x['location']
#	print(y['address'])
#location = venues[0]
#print(location)
#for location in venues:
item = venues[0]
#for item in venues:
	#print(item)
#	for location in item['location']:
#		print(location)
location = item['location']
address = location['address']




#for x in venues:
#	if 'address' in x['location'].keys():
#		print(x['location']['address'])
#		print(x['name'])
#		print(x['id'])
#		print('\n')
for x in venues:
	print(x['name'])
	try:
		print("location",  x['location']['formattedAddress'])
	except Exception:
		pass
	print("type", x['categories'][0]['shortName'])
	print("Distance: ", x['location']['distance'])
	print('\n')
