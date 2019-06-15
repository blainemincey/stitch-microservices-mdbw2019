#!/usr/bin/env python3

import requests
import json
import time
from timeit import default_timer as timer

####
# Start script
####
start = timer()
print("============================")
print("     POST New User          ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():

    # sample_mflix.movies has unique index on email
    # if use today's Month and Day as birthday, trigger will fire
    user_document = {
        "name": "Blaine Mincey",
        "email": "blaine@here.there",
        "password": "securepassword",
        "birthdate": "1971-06-14"
    }

    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "webhooks.mongodb-stitch.com",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    data = json.dumps(user_document).encode("utf-8")

    response = requests.request("POST", URL, data=data, headers=headers)

    print(response.text)

####
# Constants
####
URL = "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/microservices-application-pkgif/service/myHttpService/incoming_webhook/postNewUserWebhook"

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
