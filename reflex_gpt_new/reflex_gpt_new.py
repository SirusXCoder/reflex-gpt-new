"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from . import pages



app = rx.App()
app.add_page(pages.about_us_page, route="/about" )
app.add_page(pages.home_page, route="/")
