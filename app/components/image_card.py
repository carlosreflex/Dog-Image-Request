import reflex as rx
from app.states.state import State


def image_card() -> rx.Component:
    """A card to display the dog image."""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "A Random Dog",
                class_name="text-4xl font-bold text-gray-800 tracking-tight",
            ),
            rx.el.p(
                "Isn't it cute? This is a randomly generated image of a dog.",
                class_name="text-lg text-gray-600 mt-2",
            ),
            class_name="p-6",
        ),
        rx.el.div(
            rx.image(
                src=State.image_url,
                alt="A cute dog",
                class_name="w-full h-auto object-cover",
            ),
            class_name="rounded-b-2xl overflow-hidden",
        ),
        class_name="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden max-w-lg w-full",
    )