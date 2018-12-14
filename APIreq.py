from django.http import JsonResponse
import requests
from socket import error as SocketError
import time

payload={'username': 'Thefinsol', 'password':'t43f!n501','grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501'}

r= requests.post('https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token', json=payload)
print(r)
print(r.text)

