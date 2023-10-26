import json

# import requests


def lambda_handler(event, context):
    
    print("Evento de mi lambda handler: ",event)

    print("Objeto Contexto: ", context)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello my friends",
        }),
    }
