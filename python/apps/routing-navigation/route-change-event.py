import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text(f"Initial route: {page.route} views: {page.views}"))

    def route_change(e):
        page.add(Text(f"New route: {e.route} views: {page.views}"))

    page.on_route_change = route_change
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)  # default: route_url_strategy="path", 127.0.0.1:port,  127.0.0.1:port/path1
# flet.app(target=main, view=flet.WEB_BROWSER, route_url_strategy="hash")  # 127.0.0.1:port,  127.0.0.1:port/#/path1
