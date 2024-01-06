import flet as ft
import flet_fastapi
import uvicorn

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
















# OK http://127.0.0.1:8000
# OK http://127.0.0.1:8000/sub-app/

app = flet_fastapi.FastAPI()
app.mount("/sub-app", flet_fastapi.app(sub_main))
app.mount("/", flet_fastapi.app(root_main))

# RUN FROM CMD LINE:
# uvicorn 0002_flet_app_multiple_under_same_domain:app
# uvicorn 0002_flet_app_multiple_under_same_domain:app  --host=0.0.0.0 --port=5000
# RUN FROM CMD LINE (MAIN):
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
# python3 0002_flet_app_multiple_under_same_domain.py
