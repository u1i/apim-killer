import requests, uuid, time

url = "https://webhook.site/2bbf4a44-f890-411c-a2b9-cbbe12d4c4a9"
#url = "https://vip:8075/api/portal/v1.3/applications/<id>/extclients"

while True:

	clientid = id = str(uuid.uuid4())
	payload = "{\n\"clientId\": \"" + clientid[0:29]+ "\", \n\"enabled\": true,\n\"createdBy\":  1,\n\"createdOn\": " + str(int(time.time())) + ",\n\"corsOrigins\": [\"*\"]\n}"
	headers = {
	    'Content-Type': "application/json",
	    'User-Agent': "PostmanRuntime/7.18.0",
	    'Accept': "*/*",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "03f75feb-d8c1-410d-b8bd-6d1638f9b646,bf3fe062-ff24-48dd-8941-a03398d44625",
	    'Host': "webhook.site",
	    'Accept-Encoding': "gzip, deflate",
	    'Content-Length': "102",
	    'Connection': "keep-alive",
	    'cache-control': "no-cache"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
