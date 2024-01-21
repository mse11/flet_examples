import flet as ft


# There are 2 ways to define color property value in Flet: hex value and named colors.
# 1. Hex value
#   a) #rrggbb (0xeeggbb)                     WITHOUT aa (opacity) == ff (not transparent).
#   b) #aarrggbb (0xaarrggbb)                 WITH    aa (opacity)
#   c) ft.colors.with_opacity(0.5, '#rrggbb') (opacity - between 0.0 (completely transparent) and 1.0 (not transparent))
# 2. Named colors
#   - Material Design theme colors https://m3.material.io/styles/color/roles/color-roles
#   - colors palettes https://m2.material.io/design/color/the-color-system.html#color-usage-and-palettes
#   a) string
#   b) flet.colors module
#       - b.1) see NAMED_PALETTE_COLORS https://flet-controls-gallery.fly.dev/colors/colorpalettes
#       - b.2) see NAMED_THEME_COLORS   https://flet-controls-gallery.fly.dev/colors/themecolors
#   c) ft.colors.with_opacity(0.5, flet.colors.XXX) (opacity - 0.0 (completely transparent) and 1.0 (not transparent))

def main(page: ft.Page):
    page.add(ft.Text("HEX  : '#000000'"                       , color='#000000'))
    page.add(ft.Text("HEX  : '#40000000'"                     , color='#40000000'))
    page.add(ft.Text("HEX  : with_opacity(0.5, '#000000')"    , color=ft.colors.with_opacity(0.5, '#000000')))
    page.add(ft.Text("named: 'red'"                           , color='red'))
    page.add(ft.Text("named: 'red,0.5'"                       , color='red,0.5'))
    page.add(ft.Text("named: ft.colors.RED"                   , color=ft.colors.RED))
    page.add(ft.Text("named: ft.colors.RED_200"               , color=ft.colors.RED_200))
    page.add(ft.Text("named: ft.colors.PRIMARY"               , color=ft.colors.PRIMARY))
    page.add(ft.Text("named: ft.colors.TERTIARY"              , color=ft.colors.TERTIARY))
    page.add(ft.Text("named: with_opacity(0.5, ft.colors.RED)", color=ft.colors.with_opacity(0.5, ft.colors.RED)))

ft.app(main)
