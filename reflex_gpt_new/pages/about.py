
import reflex as rx

from reflex_gpt_new import ui


def about_us_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to Reflex About!!"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )