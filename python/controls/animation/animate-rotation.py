import flet as ft


def main(page: ft.Page):

    def MSE_EVENT_on_animation_end(e: ft.ControlEvent):
        identical = 'MSE_GET_BY_ID: ControlEvent.control == page.get_control(e.target)'
        event_str = f"Event( target={e.target} name={e.name} data(MSE_EVENT_TYPE_OF_ANIMATION)={e.data})"
        ctrl_event_str = f"ControlEvent(control={e.control} page={e.page})"
        print(f"MSE_EVENT_on_animation_end:\n >>> {identical}\n >>> {event_str}\n >>> {ctrl_event_str}")

    c1 = ft.Container(
        width=140,
        height=100,
        left=200,
        top=100,
        bgcolor="red",
        border_radius=5,
        rotate=1,
        animate_rotation=1000,
        on_animation_end=MSE_EVENT_on_animation_end,
    )

    c2 = ft.Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=ft.transform.Rotate(-1, alignment=ft.alignment.center_left),
        animate_rotation=ft.animation.Animation(duration=300),
        on_animation_end=MSE_EVENT_on_animation_end
    )

    def animate(e):
        c1.rotate += 1
        c2.rotate.angle -= 1
        page.update()

    page.add(
        ft.Stack([c1, c2], width=600, height=600),
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.app(target=main)
