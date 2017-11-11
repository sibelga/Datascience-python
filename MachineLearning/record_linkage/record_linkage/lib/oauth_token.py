"""Get OAuth token from UAA"""
import requests
import configparser


def get_new_token(config_file='credentials.ini'):
    cfg = configparser.ConfigParser()
    cfg.read(config_file)
    username = cfg.get('default', 'username')
    password = cfg.get('default', 'password')
    url = "https://{}:{}@identity-cs.cmxpreprod.com/uaa/oauth/token?grant_type=client_credentials".format(username, password)

    res = requests.post(url=url,
                        headers={'accept': 'application/json'})
    if res.status_code == 200:
        return res.json()['access_token']
    else:
        j = res.json()
        raise ValueError("Failed to retrieve token, response code {}, error {}, error description"
                         .format(res.status_code, j['error'], j['error_description']))


