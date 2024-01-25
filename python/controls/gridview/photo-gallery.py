import flet
from flet import GridView, Image, Page, border_radius


def main(page: Page):
    runs_count = 3
    max_extent = 150
    child_aspect_ratio = 1

    page.title = f"GridView Example runs_count={runs_count} max_extent={max_extent} child_aspect_ratio={child_aspect_ratio}"
    page.theme_mode = "dark"
    page.padding = 50
    page.update()

    images = GridView(
        expand=1,
        runs_count=runs_count,
        max_extent=max_extent,
        child_aspect_ratio=child_aspect_ratio,
        spacing=5,
        run_spacing=5,
    )

    page.add(images)

    for i in range(0, 60):
        images.controls.append(
            Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit="none",
                repeat="noRepeat",
                border_radius=border_radius.all(10),
            )
        )
    page.update()


flet.app(target=main)
