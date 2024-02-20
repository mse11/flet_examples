import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors, Column


def main(page: Page):

    COLUMN_POSITION = 1

    status = []
    def dum_page_state():
        status_info = f">>> ON_route_change <<< page.route '{page.route}'" + \
                      f" <-> page.views '{page.views}' <-> page.views IDs:', {[id(v) for v in page.views]}" + \
                      f" <-> page.views[LAST=={id(page.views[-1])}].controls {page.views[-1].controls}"
        status.append(status_info)

        page.views[-1].controls[COLUMN_POSITION].controls = [Text(s) for s in status]
        page.update()

    page.title = "Routes Example"

    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Flet app")),
                    Column(),  # DEBUG LOGS
                    ElevatedButton("Go to settings", on_click=open_settings),
                ],
            )
        )
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings",
                    [
                        AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                        Column(),  # DEBUG LOGS
                        Text("Settings!", style="bodyMedium"),
                        ElevatedButton(
                            "Go to mail settings", on_click=open_mail_settings
                        ),
                    ],
                )
            )
        if page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings/mail",
                    [
                        AppBar(
                            title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Column(),  # DEBUG LOGS
                        Text("Mail settings!"),
                    ],
                )
            )
        dum_page_state()

    def view_pop(e): # It fires when the user clicks automatic "Back" button in AppBar
        print("View pop:", e)
        status.append(f">>> ON_view_pop <<<  {e}")
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop  # It fires when the user clicks automatic "Back" button in AppBar

    def open_mail_settings(e):
        page.go("/settings/mail")

    def open_settings(e):
        page.go("/settings")

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)
