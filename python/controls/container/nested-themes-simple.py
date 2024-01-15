import flet as ft
from theme_colors import theme_colors_containers

def main(page: ft.Page):
    # Yellow page theme with SYSTEM (default) mode
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.YELLOW,
    )

    c_orig = ft.Column(controls=[
        # Page theme
        ft.Container(
            content=ft.ElevatedButton("Page theme button"),
            #bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
        # Inherited theme with primary color overridden
        ft.Container(
            #theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
            content=ft.ElevatedButton("Inherited theme with primary color overridden"),
            #bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
        # "Inherited theme with primary color overridden DARK THEME"
        ft.Container(
            #theme=ft.Theme(color_scheme_seed=ft.colors.PINK),
            #theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Inherited theme with primary color overridden DARK THEME"),
            #bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
    ])

    c_custom = ft.Column(controls=[
        # Page theme
        ft.Container(
            content=ft.ElevatedButton("Page theme button"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
        # Inherited theme with primary color overridden
        ft.Container(
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
            content=ft.ElevatedButton("Inherited theme with primary color overridden"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
        # "Inherited theme with primary color overridden DARK THEME"
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.PINK),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Inherited theme with primary color overridden DARK THEME"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300,
        ),
    ])

    page.add(
        ft.Row(controls=theme_colors_containers()),
        ft.Row(controls=[c_orig, c_custom]),
    )


ft.app(main)
