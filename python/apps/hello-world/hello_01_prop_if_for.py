import flet as ft
import time


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)  # Some controls are "container" controls (like Page) which could contain other controls.

    do_more_work = False  # !!! 2. PLEASE TO True !!!
    if do_more_work:
        for i in range(5):
            t.value = f"Step {i}"
            page.update()
            time.sleep(2)
    else:
        # page.update()  # !!! 1. PLEASE UNCOMMENT THIS LINE !!!
        pass

ft.app(target=main)
