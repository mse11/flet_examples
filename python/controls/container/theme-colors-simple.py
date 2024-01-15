import flet as ft
from theme_colors import theme_colors_containers


async def main(page: ft.Page):
    default_color = "blue"

    color_name = ft.TextField(hint_text=default_color, autofocus=True)

    async def btn_click_color_scheme_seed(e):
        # e.control.page.theme PAGE ACCESS VIA CONTROL
        page.theme = ft.Theme(
            color_scheme_seed=default_color if color_name.value == '' else color_name.value,
            #color_scheme=
        )
        # await e.control.page.update_async() PAGE ACCESS VIA CONTROL
        await page.update_async()

    btn_seed = ft.ElevatedButton("Set Theme Color (seed)", on_click=btn_click_color_scheme_seed)


    async def btn_click_change_PRIMARY__PRIMARY_CONTAINER(e):
        # e.control.page.theme PAGE ACCESS VIA CONTROL
        page.theme = ft.Theme(
            #color_scheme_seed=
            color_scheme=ft.ColorScheme(
                primary=ft.colors.GREEN,
                primary_container=ft.colors.GREEN_200
                # ...
            ),
        )
        # await e.control.page.update_async() PAGE ACCESS VIA CONTROL
        await page.update_async()

    btn_primary = ft.ElevatedButton("Set Only PRIMARY & PRIMARY_CONTAINER of default BLUE scheme", on_click=btn_click_change_PRIMARY__PRIMARY_CONTAINER)

    await page.add_async(
        ft.Text('Theme colors: A set of 30 colors based on the Material 3 color system that can be used to configure the color properties of most controls.'),
        ft.Row(controls=theme_colors_containers()),
        color_name,
        btn_seed,
        btn_primary,
    )


ft.app(main)
