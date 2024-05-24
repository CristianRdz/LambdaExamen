import json



def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "nombre_completo": "Cristian Rodriguez Rodriguez",
            "grado": "9",
            "grupo": "C",
        }),
    }
