# Lambda Image Classification Service

This project hosts an AWS Lambda function that provides an image classification service using the InceptionV3 model trained on ImageNet dataset. The service is exposed through an API endpoint, where users can send an image URL, and the service will return the predicted class and the associated probability of the image belonging to that class.

## Model Overview

InceptionV3 is a deep convolutional neural network model that is trained on the ImageNet dataset, which contains over a million images across 1000 different classes. This model is used for the purpose of image classification and can recognize a wide range of objects and concepts.

## Getting Started

To get this service running, you'll need to deploy it to AWS Lambda. Here are the steps to follow:

### Deployment

1. **Clone the repository:**

```bash
git clone git clone https://github.com/FindMyPetOrg/findmypet-image-recognition.git
cd findmypet-image-recognition
```

2. **Install Python Dependencies**: Install the required Python libraries specified in your `requirements.txt` to ensure your environment matches the project's needs.

```bash
pip install -r requirements.txt
```
3. **Install Node.js Dependencies**: Make sure Node.js and npm are installed. Then, install the Serverless framework and other necessary Node.js packages defined in `package.json`.

```bash
npm install
```

4. **Run Locally Using Serverless Offline**: To test the function locally on your machine, use Serverless Offline, which simulates AWS Lambda and API Gateway locally.

```bash
serverless offline
```

This command starts a local server. You can now send POST requests to `http://localhost:3000/predict` with the JSON payload containing the `URL_img` key.

Example request:
```json
{
  "URL_img": "http://example.com/image.jpg"
}
```

