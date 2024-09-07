"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

filename = f"{config.app_name}/{config.app_name}.py"
projects_url = "DUMMY_URL"
projects_url = "DUMMY_URL"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.fragment(
        
        pc.hstack(
            pc.color_mode_button(pc.color_mode_icon(), float="right"),
            pc.link(
                "My Projects!",
                href=projects_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": pc.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            pc.link(
                "My Blog!",
                href=projects_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": pc.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
        # spacing="20em",
        ),
        pc.vstack(
            pc.heading("NICHOLAS TEAGUE", 
                       font_size="8em",
                       _hover={
                            "background_clip":"text",
                            "background_image":pc.color_mode_cond(
                                light="linear-gradient(96.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                                dark="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            ),
                            "font_weight":"bold",
                       },
            ),
            spacing="1.5em",
            padding_top="20%",
        )
        
        
        # pc.vstack(
        #     pc.heading("Welcome to Pynecone!", font_size="2em"),
        #     pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
        #     pc.link(
        #         "Check out our docs!",
        #         href=docs_url,
        #         border="0.1em solid",
        #         padding="0.5em",
        #         border_radius="0.5em",
        #         _hover={
        #             "color": pc.color_mode_cond(
        #                 light="rgb(107,99,246)",
        #                 dark="rgb(179, 175, 255)",
        #             )
        #         },
        #     ),
        #     spacing="1.5em",
        #     font_size="2em",
        #     padding_top="10%",
        # ),
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
