from app import app
from flask import request, Response
import requests,os

try:
    DST=os.environ['DST']
except:
    DST='http://eatinghealthyis.fun'

@app.route('/',methods=['GET','POST'])
def _proxy(*args, **kwargs):
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, DST),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response

