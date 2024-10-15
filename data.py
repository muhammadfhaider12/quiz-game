import requests

parameters={
    "amount":10,
    "type":"boolean"
}

req=requests.get("https://opentdb.com/api.php?amount=10&type=boolean",params=parameters)

req.raise_for_status()
data=req.json()
question_data= data['results']

