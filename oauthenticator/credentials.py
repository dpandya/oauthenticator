import requests 
import json
import os

def get_temporary_credentials():
    f = open(os.environ["HOME"] + "/auth", "r")
    auth = json.loads(f.read())
    headers = {'Authorization': 'Bearer ' + auth["id_token"]}
    url = auth["api_url"]+"/api/environments/temporary-credentials"
    auth = requests.post(url=url, headers=headers, data={}).json()

    if bool(auth) == False:
        raise Exception('No authorization found. Check your Survey access.')
        return
    
    os.environ['AWS_ACCESS_KEY_ID'] = auth['Credentials']['AccessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = auth['Credentials']['SecretAccessKey']
    os.environ['AWS_SESSION_TOKEN'] = auth['Credentials']['SessionToken']

    return True