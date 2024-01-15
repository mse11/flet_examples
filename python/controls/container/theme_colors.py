import flet as ft

# name = "Theme colors"


def theme_colors_container_group(start=None, end=None):
    class Color:
        def __init__(self, display_name, name, is_dark=False):
            self.name = name
            self.display_name = display_name
            self.is_dark = is_dark

    theme_colors = [
        Color("PRIMARY", "primary"),
        Color("ON_PRIMARY", "onprimary"),
        Color("PRIMARY_CONTAINER", "primarycontainer"),
        Color("ON_PRIMARY_CONTAINER", "onprimarycontainer", True),
        Color("SECONDARY", "secondary"),
        Color("ON_SECONDARY", "onsecondary"),
        Color("SECONDARY_CONTAINER", "secondarycontainer"),
        Color("ON_SECONDARY_CONTAINER", "onsecondarycontainer", True),
        Color("TERTIARY", "tertiary"),
        Color("ON_TERTIARY", "ontertiary"),
        Color("TERTIARY_CONTAINER", "tertiarycontainer"),
        Color("ON_TERTIARY_CONTAINER", "ontertiarycontainer", True),
        Color("ERROR", "error"),
        Color("ON_ERROR", "onerror"),
        Color("ERROR_CONTAINER", "errorcontainer"),
        Color("ON_ERROR_CONTAINER", "onerrorcontainer", True),
        Color("OUTLINE", "outline"),
        Color("OUTLINE_VARIANT", "outlinevariant", True),
        Color("BACKGROUND", "background"),
        Color("ON_BACKGROUND", "onbackground", True),
        Color("SURFACE", "surface"),
        Color("ON_SURFACE", "onsurface", True),
        Color("SURFACE_TINT", "surfacetint"),
        Color("SURFACE_VARIANT", "surfacevariant"),
        Color("ON_SURFACE_VARIANT", "onsurfacevariant", True),
        Color("INVERSE_SURFACE", "inversesurface", True),
        Color("ON_INVERSE_SURFACE", "oninversesurface"),
        Color("INVERSE_PRIMARY", "inverseprimary"),
        Color("SHADOW", "shadow", True),
        Color("SCRIM", "scrim", True),
    ]

    async def copy_to_clipboard(e):
        await e.control.page.set_clipboard_async(f"ft.colors.{e.control.content.value}")
        await e.control.page.show_snack_bar_async(
            ft.SnackBar(
                ft.Text(f"Copied to clipboard: ft.colors.{e.control.content.value}"),
                open=True,
            )
        )

    theme_colors_column = ft.Column(spacing=0)

    theme_colors_column.controls = []

    for color in theme_colors[start: end]:
        if color.is_dark:
            text_color = ft.colors.SURFACE
        else:
            text_color = ft.colors.ON_SURFACE

        theme_colors_column.controls.append(
            ft.Container(
                height=30,
                bgcolor=color.name,
                content=ft.Text(color.display_name, color=text_color),
                alignment=ft.alignment.center,
                on_click=copy_to_clipboard,
            )
        )

    return ft.Container(border_radius=10, expand=True, content=theme_colors_column)


def theme_colors_containers(start_color_idx=0, step=4, end_color_idx=30):
    containers = []

    for idx in range(start_color_idx, end_color_idx, step):
        containers.append(theme_colors_container_group(idx, idx + step))
    return containers


if __name__ == "__main__":
    async def main(page: ft.Page):
        await page.add_async(
            ft.Text('Theme colors: A set of 30 colors based on the Material 3 color system that can be used to configure the color properties of most controls.'),
            ft.Row(controls=theme_colors_containers())
        )
    ft.app(main)
