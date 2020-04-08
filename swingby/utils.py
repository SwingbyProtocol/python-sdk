import requests

def default_send_get(endpoint, query={}, json=True):
    """
    Sends a get request
    """
    r = requests.get(url=endpoint, params=query)
    if r.status_code is 429:
        raise Exception("GET {} failed with status code {} - Err: rate limit exception".format(endpoint, r.status_code))
    if r.status_code < 200 or r.status_code > 299:
        raise Exception("GET {} failed with status code {} - Err: {}".format(endpoint, r.status_code, r.text))
    if json:
        return r.json()
    return r.text

def default_send_post(endpoint, query={}, body={}):
    """
    Sends a post request in application/json format
    """
    r = requests.post(endpoint, params=query, json=body)
    res = r.json()
    if r.status_code is 429:
        raise Exception("GET {} failed with status code {} - Err: rate limit exception".format(endpoint, r.status_code))
    if r.status_code < 200 or r.status_code > 299:
        raise Exception("GET {} failed with status code {} - Err: {}".format(endpoint, r.status_code, res.get('message', 'unknown')))
    return res
