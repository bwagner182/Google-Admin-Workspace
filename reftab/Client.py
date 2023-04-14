import base64
from datetime import datetime
import hashlib
import hmac
import html
import json
import urllib
import urllib.parse
import urllib.request
import email.utils
from urllib.error import URLError, HTTPError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class ReftabClient():
    def __init__(self, publicKey, secretKey):
      self.publicKey = publicKey
      self.secretKey = secretKey
      pass

    def __request(self, method, endpoint, body=None):
        url = 'https://www.reftab.com/api/' + endpoint
        headers = {}
        data = None
        now = email.utils.formatdate(usegmt=True)
        contentMD5 = ''
        contentType = ''
        if body:
          data = json.dumps(body).encode('utf-8')
          contentMD5 = hashlib.md5(data).hexdigest()
          headers['Content-Type'] = 'application/json'
          contentType = 'application/json'
        
        signatureToSign = method + '\n' + contentMD5 + '\n' + contentType + '\n' + now + '\n' + url
        signature = hmac.new(
          key=self.secretKey.encode('utf-8'),
          msg=signatureToSign.encode('utf-8'),
          digestmod=hashlib.sha256
        ).hexdigest()
        signatureToSign = html.unescape(urllib.parse.quote(signatureToSign.encode('utf-8')))
        signature = base64.b64encode(signature.encode('utf-8')).decode('utf-8')
        headers['Authorization'] = 'RT ' + self.publicKey + ':' + signature
        headers['x-rt-date'] = now
        
        try:
          request = urllib.request.Request(url=url, data=data, headers=headers, method=method)
          with urllib.request.urlopen(request) as f:
            if f.getcode() == 200:
              response = json.loads(f.read().decode('utf-8'))
            else:
              return None
        except HTTPError as e:
          print(e)
          print(json.loads(e.read().decode('utf-8')))
        except URLError as e:
          print(e)
        else:
          return response
      
    def get(self, endpoint, id=None):
        if (id):
          endpoint += '/' + id
        return self.__request('GET', endpoint)
        
    def put(self, endpoint, id, body):
        if (id == None):
            raise Exception('id is required')
        endpoint += '/' + id
        return self.__request('PUT', endpoint, body)
        
    def post(self, endpoint, body):
        return self.__request('POST', endpoint, body)
        
    def delete(self, endpoint, id):
        if (id == None):
            raise Exception('id is required')
        endpoint += '/' + id
        return self.__request('DELETE', endpoint, body)
