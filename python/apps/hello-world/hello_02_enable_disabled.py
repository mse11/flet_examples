import flet as ft
import time

# Setting 'visible' to false completely prevents control (and all its children if any) from rendering on a page canvas.
# Hidden controls cannot be focused or selected with a keyboard or mouse and they do not emit any events

# 'disabled' property is mostly used with DATA ENTRY controls like TextField, Dropdown, Checkbox, buttons.
# Can be set also to a parent control and its value will be propagated down to all children recursively.

def main(page: ft.Page):

    t = ft.Text("counter: 0")

    t_11 = ft.Text("1.1")
    t_12 = ft.Text("1.2")
    t_13 = ft.Text("1.3")
    c_1 = ft.Column(controls=[
        t_11,
        t_12,
        t_13
    ])

    t_21 = ft.TextField(value="2.1")
    t_22 = ft.TextField(value="2.2")
    t_23 = ft.TextField(value="2.3")
    c_2 = ft.Column(controls=[
        t_21,
        t_22,
        t_23
    ])

    t_31 = ft.Text("3.1")
    t_32 = ft.Text("3.2")
    t_33 = ft.Text("3.3")
    c_3 = ft.Column(controls=[
        t_31,
        t_32,
        t_33
    ])

    r = ft.Row(controls=[
        c_1,
        c_2,
        c_3,
    ])

    page.add(t, r)
    time.sleep(10)
    for i in range(12):
        t.value = f'counter: {i}'
        if i % 3 == 0:
            c_3.visible = not c_3.visible
            c_2.disabled = not c_2.disabled
            t_12.visible = not t_12.visible
        page.update()
        time.sleep(1)


ft.app(main)
