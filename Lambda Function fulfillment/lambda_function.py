import requests

def generate_response(meaning="No meaning found for this word",fulfillmenState="Failed"):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillmenState,
            "message": {
                "contentType": "PlainText",
                "content": meaning
            }
        }
    }

def lambda_handler(event, context):
    word = event['currentIntent']['slots']['word']
    CONTENT_TYPE = "application/json"
    APP_ID = "53d9170b"
    APP_KEY = "3b0578d43f4dc0d436133f7ad03ca3df"
    head = {"Content-Type":CONTENT_TYPE,"app_id":APP_ID,"app_key":APP_KEY}
    r = requests.get("https://od-api.oxforddictionaries.com:443/api/v2/entries/en/"+word, headers = head)
    if r.status_code == 404 :
        return generate_response()
    else:
        data = r.json()
        meaning = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        return generate_response(word+" : "+meaning,"Fulfilled")