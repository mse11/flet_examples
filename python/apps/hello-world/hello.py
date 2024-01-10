import flet as ft


# Controls (aka widgets) are just regular Python classes
# Page is the top-most control. 
# Nesting controls into each other could be represented as a tree with Page as a root.
def main(page: ft.Page):
    page.add(ft.Text("Hello, world!"))  # it's a shortcut for page.controls.append(t) and then page.update()


ft.app(main)
