from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount(
    "/",
    StaticFiles(
        directory="/home/msestrie/MSE/MSEprojects/PYTHON/flet/sdk/python/mseapp/build/web", # path to SPA
        html=True
    ),
    name="static"
)

# RUN FROM CMD LINE:
# uvicorn 0001_pure_SPA_static_content:app
# uvicorn 0001_pure_SPA_static_content:app  --host=0.0.0.0 --port=5000
# RUN FROM IDE:
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
