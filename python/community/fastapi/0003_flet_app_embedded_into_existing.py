import flet as ft
import flet_fastapi

async def root_main(page: ft.Page):
    await page.add_async(ft.Text("This is root app!"))

    counter = ft.Text("0", size=50, data=0)

    async def add_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        await counter.update_async()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_click
    )
    await page.add_async(
        ft.Container(counter, alignment=ft.alignment.center, expand=True)
    )


async def sub_main(page: ft.Page):
    await page.add_async(ft.Text("This is sub app!"))


async def sub_main(page: ft.Page):
    await page.add_async(ft.Text("This is sub app!"))


from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()


# OK http://127.0.0.1:8000/root-app/ WITHOUT SLASH == NOT FOUND
# OK http://127.0.0.1:8000/sub-app/ WITHOUT SLASH == NOT FOUND
# OK http://127.0.0.1:8000
app = FastAPI(lifespan=lifespan)
app.mount("/sub-app", flet_fastapi.app(sub_main))
app.mount("/root-app", flet_fastapi.app(root_main))

app.mount(
    "/",
    StaticFiles(
        directory="/home/msestrie/MSE/MSEprojects/PYTHON/flet/sdk/python/mseapp/build/web",
        html=True
    ),
    name="static"
)

# RUN FROM CMD LINE:
# uvicorn 0003_flet_app_embedded_into_existing:app
# uvicorn 0003_flet_app_embedded_into_existing:app  --host=0.0.0.0 --port=5000
# RUN FROM CMD LINE (MAIN):
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
# python3 0003_flet_app_embedded_into_existing.py
