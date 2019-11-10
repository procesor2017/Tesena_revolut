import json
import requests
import parse

###############-Proměnné-#################
grant_type = "refresh_token"
refresh_token = "oa_sand_rwb9tNl10pg2G4zYiSxIN5LlEUc52dvuyRdmCxpLStA"
client_id = "jYRotSFiLchjZK38wN9HuLE3ydBlUnZgyRRYKzyPSO0"
client_assertion_type = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
client_assertion = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqWVJvdFNGaUxjaGpaSzM4d045SHVMRTN5ZEJsVW5aZ3lSUllLenlQU08wIiwiaXNzIjoicmV2b2x1dC1qd3Qtc2FuZGJveC5nbGl0Y2gubWUiLCJhdWQiOiJodHRwczovL3Jldm9sdXQuY29tIn0.Qb9G6DytZKGx0cUPOEd37bis79mWfN-frAm4pnjz64kg00FedvS_pVfJ9mE4kHkepr-B0OwW0carhFkN0xGND74SJUORy1VPbfObjSSVV_04B5yZ7V1uKQ3BRADzOtIt6EfHPCnD5rCoEnJR2cy4sTz7lSjypBy09iCaqUXYuDU"

data = { 'grant_type': grant_type,
         'refresh_token': refresh_token,
         'client_id': client_id,
         'client_assertion_type': client_assertion_type,
         'client_assertion': client_assertion }

api_endpoint = "https://sandbox-b2b.revolut.com/api/1.0/auth/token"
req = requests.post(url = api_endpoint, data = data)
print(req.json())

json_accesspoint = json.loads(req.text)
access_token = json_accesspoint['access_token']

print(access_token)

##################TEST1###################################
print("Start TEST 1")
api_endpoint_tc1 = "https://sandbox-b2b.revolut.com/api/1.0/accounts"
data_tc1_header = {"Authorization": "Bearer " + str(access_token)}
data_tc1_body = {}
req_tc1 = requests.get(url=api_endpoint_tc1, data = data_tc1_body, headers = data_tc1_header)
print(req_tc1.json())


json_result = json.loads(req_tc1.json())
result = json_result['id']
print(result)