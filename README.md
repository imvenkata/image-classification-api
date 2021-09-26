# image-classification-api
 
## User Guide
Serving image classfication model thorugh API.

## Installation
Used fastapi, tensorflow mainly to create this project. You can use requirements.txt to install appropriate package version. First, create a virtual environment before installing any packages.

pip install -r requirements.txt


## How to run the app
After installing necessary packages, use the following command to run the app from project root directory-

uvicorn main:app 
And visit http://localhost:5000/docs from your browser. You will be able to see swagger. From there you can upload an image through predict endpoint and then you will get a json response.