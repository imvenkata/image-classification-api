import uvicorn
from fastapi import FastAPI, File, UploadFile
from src.model import imageClassifier
import tensorflow as tf
from starlette.responses import RedirectResponse

app_desc = """<h2>Try this app by uploading any image with `predict/image`</h2>
<h2>Image classification api based on DenseNet121 pre-trained model</h2>
<br>by Venkata Suresh"""

app = FastAPI(title='Image classification API', description=app_desc)

@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

@app.post("/api/predict/")
async def predict_image(file: bytes = File(...)):
    cl = imageClassifier()
    image = cl.read_image(file)
    image = cl.preprocess(image)
    prediction = cl.predict(image)
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, port=5000, debug=True)

#uvicorn main:app   