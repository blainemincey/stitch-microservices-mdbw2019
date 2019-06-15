#!/usr/bin/env python3

import requests
import json
import time
from timeit import default_timer as timer
import sys

####
# Start script
####
start = timer()
print("============================")
print("     GET User by Email      ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():

    req = requests.get(URL + '?email=' + EMAIL)

    if req.ok:
        json_response = json.loads(req.content)
        print(json.dumps(json_response, indent=4, sort_keys=True))
    else:
        print('Invalid response! ' + req.content)
        sys.exit('Exiting!')

####
# Constants
####
URL = "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/microservices-application-pkgif/service/myHttpService/incoming_webhook/getUserByEmailWebhook"
EMAIL = "sean_bean@gameofthron.es"

####
# Main
####
if __name__ == '__main__':
    main()

####
# Indicate end of script
####
end = timer()
print("\nEnding " + time.asctime())
print('====================================================')
print('Total Time Elapsed (in seconds): ' + str(end - start))
print('====================================================')

