import os
import time
import datetime
import requests

FILENAME = 'data.csv'
ITERVAL = 15 * 60

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as f:
        print >>f, 'timestamp,route,time,distance'

while True:
    with open("data.csv", "a") as f:
        result = requests.get("https://www.waze.co.il/RoutingManager/routingRequest?from=x%3A35.06161250398406+y%3A31.79862000996016+bd%3Atrue+s%3A122188+st_id%3A47328&to=x%3A34.84534329036279+y%3A32.06667922798102+bd%3Atrue+s%3A105560+st_id%3A15902&returnJSON=true&returnGeometries=true&returnInstructions=true&timeout=60000&nPaths=3")
        try:
            routes = result.json()['alternatives']
            for route in routes:
                totalTime = sum([res['crossTime'] for res in route['response']['results']])
                distance = sum([res['length'] for res in route['response']['results']])
                name = route['response']['routeName']
                data = '%s,%s,%0.1f,%0.1f' % (
                    datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
                    name.encode('latin1').decode('utf8').encode('utf8'),
                    totalTime / 60.0,
                    distance / 1000.0
                )
                print >>f, data
        except Exception, e:
            print str(e)
    time.sleep(ITERVAL)
