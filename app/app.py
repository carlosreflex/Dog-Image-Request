import reflex as rx
from app.states.state import State
from app.components.image_card import image_card


def index() -> rx.Component:
    """The main page of the app."""
    return rx.el.main(
        rx.el.div(
            image_card(), class_name="min-h-screen flex items-center justify-center p-4"
        ),
        class_name="bg-gray-50 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Dog Image Viewer")