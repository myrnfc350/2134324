import requests
import os


CONFIG_ID = os.environ['CONFIG_ID']
CONFIG_KEY = os.environ['CONFIG_KEY']

# Tenant configuration: defaults to 'common' (multi-tenant) when unset or blank.
# A single-tenant app must set this to its tenant ID (GUID) or domain,
# for example contoso.onmicrosoft.com
TENANT_ID = (os.environ.get('TENANT_ID') or '').strip() or 'common'


def gettoken(refresh_token: str) -> dict:
    '''Return a dict containing refresh_token and access_token'''
    
    url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CONFIG_ID,
        'client_secret': CONFIG_KEY,
        'redirect_uri': 'http://localhost:53682/'
    }
    
    return requests.post(url=url, data=data, headers=headers).json()
    

if __name__ == "__main__":
    with open('refresh.txt', 'r') as f:
        token = gettoken(f.read())
    
    with open('refresh.txt', 'w') as f:
        f.write(token['refresh_token'])
