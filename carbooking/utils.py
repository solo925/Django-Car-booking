# payments/daraja_utils.py

import requests
from requests.auth import HTTPBasicAuth
from django.utils import timezone
import base64
from .daraja_config import CONSUMER_KEY, CONSUMER_SECRET, LIPA_NA_MPESA_ONLINE_SHORTCODE, LIPA_NA_MPESA_ONLINE_PASSKEY

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    json_response = response.json()
    return json_response['access_token']

def lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc, callback_url):
    access_token = get_access_token()
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{LIPA_NA_MPESA_ONLINE_SHORTCODE}{LIPA_NA_MPESA_ONLINE_PASSKEY}{timestamp}".encode()).decode('utf-8')
    payload = {
        "BusinessShortCode":"174379",    
        "Password": "MTc0Mzc5YmZiMjc5TliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
        "Timestamp":"20160216165627",    
        "CheckoutRequestID": "ws_CO_260520211133524545", 
        "TransactionType": "CustomerPayBillOnline",
        # "Amount": amount,
        # "PartyA": +254702970055,
        # "PartyB": LIPA_NA_MPESA_ONLINE_SHORTCODE,
        # "PhoneNumber": ,
        # "CallBackURL": callback_url,
         "AccountReference": "carbooking",
        # "TransactionDesc": transaction_desc
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
