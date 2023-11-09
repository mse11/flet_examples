import flet
from flet import Container, ElevatedButton, Page, Row, colors, padding


def main(page: Page):
    page.title = "Containers with different padding"

    c1 = Container(
        content=ElevatedButton("container_1"),
        bgcolor=colors.AMBER,
        padding=padding.all(10),
        width=150,
        height=150,
    )

    c2 = Container(
        content=ElevatedButton("container_2"),
        bgcolor=colors.AMBER,
        padding=padding.all(20),
        width=150,
        height=150,
    )

    c3 = Container(
        content=ElevatedButton("container_3"),
        bgcolor=colors.AMBER,
        padding=padding.symmetric(horizontal=10),
        width=150,
        height=150,
    )

    c4 = Container(
        content=ElevatedButton("container_4"),
        bgcolor=colors.AMBER,
        padding=padding.only(left=10),
        width=150,
        height=150,
    )

    c_separator = Container(
        bgcolor=colors.BLACK,
        width=10,
        height=150,
    )

    r = Row(
        [
            c_separator,
            c1,
            c_separator,
            c2,
            c_separator,
            c3,
            c_separator,
            c4,
            c_separator,
        ],
        spacing=0,
    )

    page.add(
        Container(
            content=r,
            bgcolor=colors.RED,
        )
    )


flet.app(target=main)
