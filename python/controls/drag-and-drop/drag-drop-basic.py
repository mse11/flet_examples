import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example"

    def drag_accept(e: ft.DragTargetAcceptEvent):
        # get draggable control by its ID (source == Draggable)
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control (destination == DragTarget)
        e.control.content.content.value = "1"
        # reset border
        e.control.content.border = None
        page.update()

    def drag_will_accept(e: ft.ControlEvent):
        # black border when it's allowed to drop and red when it's not
        e.control.content.border = ft.border.all(
            2, ft.colors.RED if e.data == "true" else ft.colors.RED
        )
        e.control.update()

    def drag_leave(e: ft.ControlEvent):
        e.control.content.border = None
        e.control.update()

    def build_row(group_src, group_dst, when_dragging=False, feedback=False, drop_time=False):

        is_same: bool   = group_src == group_dst
        acc_or_rej: str = 'accepted,' if is_same else 'reject,'
        drop: str       = ' drop_time,' if drop_time else ''
        dragging: str   = ' content_when_dragging,' if when_dragging else ''
        feedback: str   = ' content_feedback,' if feedback else ''

        row = ft.Row(
            [
                ft.Draggable(
                    group=group_src,
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.GREEN_200 if is_same else ft.colors.RED_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(  # by default SAME AS .content
                        width=50,
                        height=50,
                        bgcolor=ft.colors.GREY,
                        border_radius=5,
                    ) if when_dragging else None,
                    content_feedback=ft.Text(  # by default SAME AS .content with 50% opacity
                        'drag ...',
                    ) if feedback else None,
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group=group_dst,
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.GREEN if is_same else ft.colors.RED,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept if drop_time else None,
                    on_leave=drag_leave if drop_time else None,
                ),
                ft.Container(width=100),
                ft.Text(f"{acc_or_rej}{drop}{dragging}{feedback}")
            ]
        )
        return row

    page.add(
        build_row("numberMATCH_x", "numberMATCH_y"),
        build_row("numberMATCH_1a", "numberMATCH_1a"),
        build_row("numberMATCH_1b", "numberMATCH_1b", drop_time=True),
        build_row("numberMATCH_2", "numberMATCH_2", when_dragging=True),
        build_row("numberMATCH_3", "numberMATCH_3", feedback=True),
        build_row("numberMATCH_4", "numberMATCH_4", drop_time=True, when_dragging=True, feedback=True),
    )


ft.app(target=main)
