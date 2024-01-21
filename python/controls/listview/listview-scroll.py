from time import sleep

import flet
from flet import ListView, Page, Text


def main(page: Page):
    page.title = "Auto-scrolling ListView"

    lv = ListView(
        expand=1,
        spacing=10,
        padding=20,
        auto_scroll=True,
        # horizontal=False as  Column, to work properly set .expand=1/True, or .height
        # horizontal=True  as  Row,    to work properly set .expand=1/True, or .width
    )

    count = 1

    for i in range(0, 60):
        lv.controls.append(Text(f"Line {count}"))
        count += 1

    page.add(lv)

    for i in range(0, 10):
        sleep(1)
        lv.controls.append(Text(f"Line {count} with sleep 1 sec"))
        count += 1
        page.update()


flet.app(target=main)
