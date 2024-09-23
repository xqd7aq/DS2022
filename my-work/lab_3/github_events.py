#!/bin/bash/python3

#get packages
import os
import json
import requests

#fetch env variable
GHUSER = os.getenv("GITHUB_USER")
print(GHUSER)

# fetch events for github account
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)
#print(url)

#load data through url
r = json.loads(requests.get(url).text)

#given code
for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)

#printing r 
#print(r)


