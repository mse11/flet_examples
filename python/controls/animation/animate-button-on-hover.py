import flet as ft


def main(page: ft.Page):

    def MSE_EVENT_on_hower(e: ft.ControlEvent):
        identical = 'MSE_GET_BY_ID: ControlEvent.control == page.get_control(e.target)'
        event_str = f"Event( target={e.target} name={e.name} data(HOVER IN/OUT)={e.data})"
        ctrl_event_str = f"ControlEvent(control={e.control} page={e.page})"
        print(f"MSE_EVENT_on_hower:\n >>> {identical}\n >>> {event_str}\n >>> {ctrl_event_str}")

    def animate(e: ft.ControlEvent):
        MSE_EVENT_on_hower(e)
        b1.rotate = 0.1 if e.data == "true" else 0
        page.update()

    b1 = ft.ElevatedButton(
        "Hover me, I'm animated!",
        rotate=0,
        animate_rotation=100,
        on_hover=animate,
        on_click=lambda e: print("Clicked!"),
        on_long_press=lambda e: print("Long pressed!"),
    )

    page.add(b1)


ft.app(target=main)
