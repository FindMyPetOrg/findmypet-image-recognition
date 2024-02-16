# from keras.applications.inception_v3 import InceptionV3
# model = InceptionV3(weights='imagenet')
# model.save("model.h5")

import json
import numpy as np
import requests
from PIL import Image
import io
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input, decode_predictions

model = load_model("model.h5")
def processLambdaRequest(event):

    if event['httpMethod'] != 'POST':
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid HTTP method"})}

    if not event.get('body'):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid body (empty)"})}

    body = json.loads(event['body'])

    return body


def handler(event, context):
    body = processLambdaRequest(event)
    if body is None:
        return {"statusCode": 400, "body": json.dumps("Invalid request")}

    try:
        url_img = body.get('URL_img')
        if not url_img:
            return {"statusCode": 400, "body": json.dumps("URL_img is required")}
        response = requests.get(url_img)
        with Image.open(io.BytesIO(response.content)) as img:
            img = img.convert("RGB")
            img = img.resize((299, 299))
            img = np.array(img)
            img = preprocess_input(img)

            predictions = model.predict(np.expand_dims(img, axis=0))
            decoded_predictions = decode_predictions(predictions, top=1)[0]

            class_name = decoded_predictions[0][1]
            probability = float(decoded_predictions[0][2])

        return {
            "statusCode": 200,
            "body": json.dumps({"class_name": class_name, "probability": probability})
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(str(e))}