import requests 
import json
import os

def get_temporary_credentials():
    f = open(os.environ["HOME"] + "/auth", "r")
    auth = json.loads(f.read())
    headers = {'Authorization': 'Bearer ' + auth["id_token"]}
    url = auth["api_url"]+"/api/environments/temporary-credentials"
    return requests.get(url=url, headers=headers).json()
