import flet as ft

# We are increasing allowed size to 8MB (Default size is 1 MB), which is the maximum size of WebSocket message in bytes
# that can be received by Flet Server rendering the page. Squeezing large messages through WebSocket channel is,
# generally, not a good idea, so use BATCHED_UPDATES aproach to control channel load.
# import os
# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    
    nb_items = 20010
    page.title = f"LISTVIEW nb_items: {nb_items}"
    # page.update()
    
    lv = ft.ListView(expand=True, spacing=10)
    page.add(lv)  # UPDATE_1

    for i in range(nb_items):
        lv.controls.append(ft.Text(f"Line {i}"))
        if i % 500 == 0:
            page.update()  # UPDATE_2_partial
    page.update()  # UPDATE_2_rest


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
