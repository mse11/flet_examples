import flet as ft

# We are increasing allowed size to 8MB (Default size is 1 MB), which is the maximum size of WebSocket message in bytes
# that can be received by Flet Server rendering the page. Squeezing large messages through WebSocket channel is,
# generally, not a good idea, so use BATCHED_UPDATES aproach to control channel load.
# import os
# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):

    nb_items = 20000
    page.title = f"ROW nb_items: {nb_items}"
    page.update()

    r = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(r)

    for i in range(nb_items):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
