"""
Search person using the legacy record linkage API
"""

from lib.oauth_token import get_new_token
import requests

ENDPOINT = 'ENDPOINT'


def search(query, token=None, debug=False, retry=3):
    if token is None:
        token = get_new_token()
    q = query.copy()
    if 'debug' not in q:
        q['debug'] = debug
    res = requests.get(ENDPOINT,
                       headers={'Authorization': 'Bearer {}'.format(token)},
                       params=q
                       )
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 401 and retry > 0:
        print("Retrying API call with fresh token...")
        return search(query, token=None, debug=debug, retry=retry - 1)
    else:
        j = res.json()
        raise ValueError("Invalid API Response. Code `{!r}`, Error `{!r}`, Description `{!r}`"
                         .format(res.status_code, j['error'], j['error_description']))

# Debug = True is not authorized at the moment...
res = search({'full_name': 'Warren Buffett'}, debug=False)
