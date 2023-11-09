import flet as ft


def main(page: ft.Page):
    image = ft.Image(src="https://picsum.photos/100/200?2")
    page.add(
        ft.Row(
            [
                image,
                ft.ShaderMask(
                    image,
                    blend_mode=ft.BlendMode.DST_IN,
                    shader=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.BLACK, ft.colors.TRANSPARENT],
                        stops=[0.5, 1.0],
                    ),
                    border_radius=10,
                ),
            ]
        )
    )


ft.app(target=main)
