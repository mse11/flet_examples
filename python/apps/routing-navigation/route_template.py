from _testcapi import _test_structmembersType, test_from_contiguous

import flet
from flet import Page, Text, TemplateRoute


def main(page: Page):

    test_field = Text(color='red', weight="bold")
    def parse_route(e):
        troute = TemplateRoute(page.route)
        if troute.match("/"):
            test_field.value = f"{page.route} => DEFAULT"
        elif troute.match("/books/:id"):
            test_field.value = f"{page.route} => Book view ID: {troute.id}"
        elif troute.match("/account/:account_id/orders/:order_id"):
            test_field.value = f"{page.route} => Account: {troute.account_id} Order:{troute.order_id}"
        else:
            test_field.value = f"{page.route} => Unknown route"
        page.update()

    page.title = "Routes Templates"
    page.on_route_change = parse_route
    page.add(Text(f"TEST_1:     {page.url}/books/10", selectable=True))
    page.add(Text(f"TEST_2:     {page.url}/account/123/orders/456", selectable=True))
    page.add(Text(f"TEST_3:     {page.url}/unknown/route", selectable=True))
    page.add(Text(f"=================================================="))
    page.add(test_field)
    parse_route(None)


flet.app(target=main, view=flet.WEB_BROWSER)
