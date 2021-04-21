from django.test import TestCase

# Create your tests here.
import http.client

conn = http.client.HTTPSConnection("niccko.eu.auth0.com")

payload = "{\"client_id\":\"1HMADso9HSSPGdogl9UtzLKzMhpgPKdS\",\"client_secret\":\"hLXsiaQNKPHs2ZOFHMdmjDymqrao36Tnb0pEc7TCtx5foupl2GzTUZ4pGiVHwG8C\",\"audience\":\"https://scholarship/api/sport\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))