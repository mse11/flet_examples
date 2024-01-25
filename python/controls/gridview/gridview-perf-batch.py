import flet as ft

# We are increasing allowed size to 8MB (Default size is 1 MB), which is the maximum size of WebSocket message in bytes
# that can be received by Flet Server rendering the page. Squeezing large messages through WebSocket channel is,
# generally, not a good idea, so use BATCHED_UPDATES aproach to control channel load.
# import os
# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):

    nb_items = 20010
    page.title = f"GRIDVIEW nb_items: {nb_items}"
    page.update()

    gv = ft.GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    page.add(gv)

    for i in range(nb_items):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
        if i % 500 == 0:
            page.update()  # UPDATE_2_partial
    page.update()  # UPDATE_2_rest


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
