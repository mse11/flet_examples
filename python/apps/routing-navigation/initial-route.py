import flet
from flet import Page, Text, Column


def main(page: Page):
    status = Column()

    def dum_page_state():
        status_info = f"page.route '{page.route}'" + \
                      f" <-> page.views '{page.views}' <-> page.views IDs:', {[id(v) for v in page.views]}" + \
                      f" <-> page.views[0].controls {page.views[0].controls}"
        status.controls.append(Text(status_info))
        page.update()

    dum_page_state()
    page.add(status)
    page.add(Text(f"A Initial route: {page.route}"))
    page.add(Text("B"))
    page.add(Text("C"))
    dum_page_state()

    # CANNOT POP DEFAULT VIEW
    # page.views.pop() IndexError: list index out of range

flet.app(target=main, view=flet.WEB_BROWSER) # default: route_url_strategy="path", 127.0.0.1:port,  127.0.0.1:port/path1
# flet.app(target=main, view=flet.WEB_BROWSER, route_url_strategy="hash")  # 127.0.0.1:port,  127.0.0.1:port/#/path1
