import flet
from flet import Container, ElevatedButton, Page, Row, alignment, colors


def main(page: Page):
    page.title = "Containers with different alignments"

    c1a = Container(
        content=ElevatedButton("Center"),
        bgcolor=colors.AMBER,
        # padding=15,
        alignment=alignment.center,
        width=150,
        height=150,
    )

    c1b = Container(
        content=ElevatedButton("Center b"),
        bgcolor=colors.AMBER,
        padding=15,
        alignment=alignment.center,
        width=150,
        height=150,
    )

    c2a = Container(
        content=ElevatedButton("Top left"),
        bgcolor=colors.AMBER,
        # padding=15,
        alignment=alignment.top_left,
        width=150,
        height=150,
    )

    c2b = Container(
        content=ElevatedButton("Top left b"),
        bgcolor=colors.AMBER,
        padding=15,
        alignment=alignment.top_left,
        width=150,
        height=150,
    )

    c3a = Container(
        content=ElevatedButton("-0.5, -0.5"),
        bgcolor=colors.AMBER,
        # padding=15,
        alignment=alignment.Alignment(-0.5, -0.5),
        width=150,
        height=150,
    )

    c3b = Container(
        content=ElevatedButton("-0.5, -0.5 b"),
        bgcolor=colors.AMBER,
        padding=15,
        alignment=alignment.Alignment(-0.5, -0.5),
        width=150,
        height=150,
    )

    r = Row([c1a, c1b, c2a, c2b, c3a, c3b])
    page.add(r)


flet.app(target=main)
