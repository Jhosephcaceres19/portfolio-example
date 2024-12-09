import reflex as rx

class State(rx.State):
    """The app state."""
    ...

def round_button():
    return rx.button(
        "Click Me", 
        border_radius="15px", 
        font_size="18px", 
        background="red",
        class_name="px-4 py-2 text-white hover:bg-red-600 transition-transform transform hover:scale-105"
    )

def image():
    return rx.image(
        src="https://res.cloudinary.com/dcyr5qkhg/image/upload/v1724176942/JHOSEPH_u3n1pb.jpg",
        class_name="rounded-xl w-full sm:w-1/3 max-w-sm mx-auto shadow-lg hover:shadow-xl transition-shadow lg:max-w-md"
    )

def text_content():
    return rx.text(
        "Hello, my name is Jhoseph Caceres. I am a web developer based in Bolivia, Cochabamba, with experience through projects and university subjects. My goal is to challenge myself in a new environment to learn, develop, improve my skills through different projects, and contribute to the company with my abilities.",
        class_name="text-sm sm:text-lg p-4 text-pretty text-justify leading-relaxed lg:text-xl lg:leading-loose lg:pr-8"
    )

def nav_bar():
    return rx.container(
        rx.flex(
            rx.text(
                "About Me", 
                class_name="bg-purple-500 rounded-xl p-2 w-40 text-white text-center hover:bg-purple-600 cursor-pointer transition-colors"
            ),
            rx.text(
                "Portfolio", 
                class_name="bg-purple-500 rounded-xl p-2 w-40 text-white text-center hover:bg-purple-600 cursor-pointer transition-colors"
            ),
            rx.text(
                "Contact", 
                class_name="bg-purple-500 rounded-xl p-2 w-40 text-white text-center hover:bg-purple-600 cursor-pointer transition-colors"
            ),
            class_name="justify-around gap-4 lg:gap-8 py-2"
        ),
        class_name="bg-sky-600 rounded-b-xl lg:py-4"
    )

def contact():
    return rx.container(
        rx.text(
            "Contact", 
            class_name="bg-sky-600 rounded-xl p-2 w-40 text-white text-center hover:bg-purple-600 cursor-pointer transition-colors"
        ),
    )

def content_contact():
    return rx.container(
        rx.flex(
            rx.flex(
                rx.icon("phone", class_name="text-blue-500 animate-pulse"),
                rx.text("63882178", class_name="text-blue-400"),
                class_name="gap-2 items-center"
            ),
            rx.flex(
                rx.icon("linkedin", class_name="text-blue-700"),
                rx.link("LinkedIn", href="https://www.linkedin.com/in/jos%C3%A9-caceres-aramayo-9b7548268/", target="_blank", class_name="text-blue-400 hover:text-blue-600"),
                class_name="gap-4 items-center"
            ),
            class_name="justify-around w-full lg:gap-8"
        ),
        rx.flex(
            rx.flex(
                rx.icon("github", class_name="text-gray-800"),
                rx.link("GitHub", href="https://github.com/Jhosephcaceres19", target="_blank", class_name="text-blue-400  hover:text-blue-600"),
                class_name="gap-4 items-center"
            ),
            rx.flex(
                rx.icon("globe", class_name="text-green-600"),
                rx.link("Website", href="https://jhosephcaceres.vercel.app/", target="_blank", class_name="text-blue-400  hover:text-blue-600"),
                class_name="gap-4 items-center"
            ),
            class_name="justify-around w-full lg:gap-8"
        ),
        class_name="flex flex-col items-center sm:flex-row gap-6 sm:justify-around w-full lg:flex-wrap lg:gap-10 lg:items-start"
    )


def index() -> rx.Component:
    return rx.container(
        nav_bar(),
        rx.flex(
            image(),
            text_content(),
            class_name="flex flex-col lg:flex-row gap-6 justify-center items-center sm:items-center lg:gap-10 pt-10"
        ),
        contact(),
        rx.flex(
            content_contact(),
            direction="row"
        ),
        rx.color_mode.button(position="bottom-right", class_name="fixed bg-gray-800 text-white p-2 rounded-full shadow-lg hover:bg-gray-700"),
        class_name="p-4 max-w-7xl mx-auto space-y-6 lg:space-y-10"
    )

# Reflex app setup
app = rx.App()
app.add_page(index, route="/", title="Welcome to Jhoseph's Portfolio")
