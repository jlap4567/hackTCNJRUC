import json
import requests


def getinfo(location):
    params = dict(
      client_id='0EZFGLHNEGBO3CL5WY4QQK1G0AASQMQU5A3R0EQMUA1FVP15',
      client_secret='KIDTS2WYUFFMWEAKS0VSCTPFWZUTMCOJK1LBIH1VAVVHWRPU',
      v='20180323',
      ll=location,
      query='restaurant',
      #limit=10
      intent = 'checkin'
    )
    url = 'https://api.foursquare.com/v2/venues/search'
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    venues = data['response']['venues']
    outList = []


    for x in venues:
            try:
                outPut = {}
                outPut['name'] = x['name']
                #print('name', x['name'])
                outPut['location'] = x['location']['formattedAddress']
                #print("location",  x['location']['formattedAddress'])
                outPut['type'] = x['categories'][0]['shortName']
                #print("type", x['categories'][0]['shortName'])
                outPut['distance'] = x['location']['distance']
                #print("Distance: ", x['location']['distance'])

                outList.append(outPut)

            except Exception:
                    pass

    return outList

