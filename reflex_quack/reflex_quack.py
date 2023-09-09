"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from typing import List, Dict, Tuple
import secrets


class State(rx.State):
    beginning_hand = ['green_1', 'orange_1'] + ['white_1']*4 + ['white_2']*2 + ['white_3']
    satchel: List[str] = beginning_hand
    pot: List[str]
    show_pot: bool = False
    token_clicked = ''
    pulled = []
    pull_count = 1
    
    @rx.var
    def current_count(self) -> str:
        # Get current count for color
        return self.count_token(self.token_clicked)
    
    @rx.var
    def pull_text(self) -> str:
        return f"Pull {self.pull_count}"
        
    @rx.var
    def orange_1_count(self) -> int:
        return self.count_token('orange_1')
    @rx.var
    def red_1_count(self) -> int:
        return self.count_token('red_1')
    @rx.var
    def red_2_count(self) -> int:
        return self.count_token('red_2')
    @rx.var
    def red_4_count(self) -> int:
        return self.count_token('red_4')
    @rx.var
    def blue_1_count(self) -> int:
        return self.count_token('blue_1')
    @rx.var
    def blue_2_count(self) -> int:
        return self.count_token('blue_2')
    @rx.var
    def blue_4_count(self) -> int:
        return self.count_token('blue_4')
    @rx.var
    def green_1_count(self) -> int:
        return self.count_token('green_1')
    @rx.var
    def green_2_count(self) -> int:
        return self.count_token('green_2')
    @rx.var
    def green_4_count(self) -> int:
        return self.count_token('green_4')
    @rx.var
    def white_1_count(self) -> int:
        return self.count_token('white_1')
    @rx.var
    def white_2_count(self) -> int:
        return self.count_token('white_2')
    @rx.var
    def white_3_count(self) -> int:
        return self.count_token('white_3')
    @rx.var
    def black_1_count(self) -> int:
        return self.count_token('black_1')
    @rx.var
    def yellow_1_count(self) -> int:
        return self.count_token('yellow_1')
    @rx.var
    def yellow_2_count(self) -> int:
        return self.count_token('yellow_2')
    @rx.var
    def yellow_4_count(self) -> int:
        return self.count_token('yellow_4')
    @rx.var
    def purple_1_count(self) -> int:
        return self.count_token('purple_1')
        
    def token_pressed(self, token_name):
        self.token_clicked = token_name
        self.satchel.append(token_name)
        
    def token_removed(self, token_name):
        self.token_clicked = token_name
        if self.count_token(token_name) < 1:
            return
        self.satchel.remove(token_name)
        
    def pull_count_add(self):
        self.pull_count += 1
    def pull_count_sub(self):
        self.pull_count -= 1
        
    def pull_token(self, number):
        self.pulled.clear()
        for _ in range(number):
            if not self.satchel:
                break
            pull = secrets.choice(self.satchel)
            self.satchel.remove(pull)
            self.pulled.append(pull)
            self.pot.append(pull)
            self.show_pot=True if len(self.pot) > 0 else False

    def return_tokens(self):
        for token in self.pot:
            self.satchel.append(token)
        self.pulled = []
        self.pot = []
        self.show_pot = False
            
    def return_token(self, token: str):
        self.pulled.remove(token)
        self.pot.remove(token)
        self.show_pot=True if len(self.pot) > 0 else False
        self.satchel.append(token)

    def count_token(self, token_type):
        return self.satchel.count(token_type)

def drawn_token(token_name: rx.Var[str]) -> rx.Component:
    style = {
        "border-color": "green",
    }
    return rx.vstack(
        rx.image(src=f"{token_name}.png",
                 width="50px", height="auto",),
        rx.badge("Return", variant="subtle", color_scheme="blue", cursor="pointer",
                 on_click=lambda: State.return_token(token_name)),
    )

def pull_list() -> rx.Component:
    return rx.hstack(
        rx.foreach(
            State.pulled,
            lambda token: drawn_token(token),
        ),
    )

def pot_token(token: rx.Var[str]) -> rx.Component:
    return rx.image(src=f"{token}.png",
                 width="40px", height="auto",)
def pot_list() -> rx.Component:
    pot_style = {
        'backgroundColor': '#e5e5e5',
        "borderRadius": '5px',
        "padding": '10px',
        'fontSize': '1em',
        'fontWeight': 'bold',
        'minHeight': '400px',
    }
    return rx.vstack(
        rx.container(
            rx.center(rx.text("Pot")),
            rx.cond(
                State.show_pot,
                rx.center(rx.badge("Reset", variant="subtle", color_scheme="blue", cursor="pointer",
                on_click=lambda: State.return_tokens))
            ),
        ),
        rx.foreach(
            State.pot,
            lambda token: pot_token(token),
        ),
        style=pot_style,
        width='20%',
    )

def index() -> rx.Component:
    badge_style = {
        "position":"absolute",
        "left":"61px",
        "top":"-5px",
        }
    remove_style = {
        "position":"absolute",
        "left":"2px",
        "top":"-5px",
        "padding": "0px 6px",
    }
    row_style = {
        "margin": '2px 0',
        "padding": '10px 5px',
        "backgroundColor": '#e5e5e5',
        "width": '100%',
        "borderRadius": '5px',
    }
    
    
    return rx.fragment(
        rx.hstack(
            pot_list(),
            rx.vstack(
                rx.hstack(
                    rx.button(State.pull_text,
                            variant="solid", color_scheme="teal", font_size="1em", size="lg",
                            on_click=State.pull_token(State.pull_count),
                            ),
                    rx.vstack(
                        rx.button(rx.icon(tag="add"),
                                font_size="0.25em", color_scheme="gray", size='xs',
                                on_click=State.pull_count_add,
                                ),
                        rx.button(rx.icon(tag="minus"),
                                font_size="0.25em", color_scheme="gray", size='xs',
                                on_click=State.pull_count_sub,
                                ),
                        spacing="0",
                    ),
                ),
                pull_list(),
                # Orange
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("orange_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="orange_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("orange_1"),
                            ),
                        rx.badge(State.orange_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Red
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("red_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="red_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("red_1"),
                            ),
                        rx.badge(State.red_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("red_2"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="red_2.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("red_2"),
                            ),
                        rx.badge(State.red_2_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("red_4"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="red_4.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("red_4"),
                            ),
                        rx.badge(State.red_4_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Blue Row
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("blue_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="blue_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("blue_1"),
                            ),
                        rx.badge(State.blue_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("blue_2"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="blue_2.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("blue_2"),
                            ),
                        rx.badge(State.blue_2_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("blue_4"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="blue_4.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("blue_4"),
                            ),
                        rx.badge(State.blue_4_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Green
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("green_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="green_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("green_1"),
                            ),
                        rx.badge(State.green_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("green_2"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="green_2.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("green_2"),
                            ),
                        rx.badge(State.green_2_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("green_4"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="green_4.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("green_4"),
                            ),
                        rx.badge(State.green_4_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # White
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("white_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="white_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("white_1"),
                            ),
                        rx.badge(State.white_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("white_2"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="white_2.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("white_2"),
                            ),
                        rx.badge(State.white_2_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("white_3"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="white_3.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("white_3"),
                            ),
                        rx.badge(State.white_3_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Black
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("black_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="black_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("black_1"),
                            ),
                        rx.badge(State.black_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Yellow
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("yellow_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="yellow_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("yellow_1"),
                            ),
                        rx.badge(State.yellow_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("yellow_2"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="yellow_2.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("yellow_2"),
                            ),
                        rx.badge(State.yellow_2_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("yellow_4"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="yellow_4.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("yellow_4"),
                            ),
                        rx.badge(State.yellow_4_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                # Purple
                rx.hstack(
                    rx.container(
                        rx.badge("-", variant="solid", color_scheme="gray",
                                on_click=State.token_removed("purple_1"), cursor="pointer",
                                style=remove_style),
                        rx.image(src="purple_1.png",
                            width="50px", height="auto",
                            on_click=State.token_pressed("purple_1"),
                            ),
                        rx.badge(State.purple_1_count, variant="solid", color_scheme="green",
                                style=badge_style),
                        style={"position":"relative"},
                    ),
                    style=row_style,
                ),
                padding_top="10%",
            ),
            justify='center',
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

#####  
# Tried to get a more streamlined method to create rows, but had trouble
# making dynamic computed variables...
#####

## In State:
    # color_val: Dict[str, List[str]] = {
    #     'orange': ['1'],
    #     'red': ['1','2','4'],
    #     'blue': ['1','2','4'],
    #     'green': ['1','2','4'],
    #     'white': ['1','2','3'],
    #     'black': ['1'],
    #     'yellow': ['1','2','4'],
    #     'purple': ['1'],
    # }
    # color_counts = {
    #     'orange_1': '0',
    #     'red_1': '0',
    #     'red_2': '0',
    #     'red_4': '0',
    #     'blue_1': '0',
    #     'blue_2': '0',
    #     'blue_4': '0',
    #     'green_1': '0',
    #     'green_2': '0',
    #     'green_4': '0',
    #     'white_1': '0',
    #     'white_2': '0',
    #     'white_3': '0',
    #     'black_1': '0',
    #     'yellow_1': '0',
    #     'yellow_2': '0',
    #     'yellow_4': '0',
    #     'purple_1': '0',
    # }
# End In State


# color_funcs = {
#     'orange_1': State.orange_1_count,
#     'red_1':    State.red_1_count,
#     'red_2':    State.red_2_count,
#     'red_4':    State.red_4_count,
#     'blue_1':   State.blue_1_count,
#     'blue_2':   State.blue_2_count,
#     'blue_4':   State.blue_4_count,
#     'green_1':  State.green_1_count,
#     'green_2':  State.green_2_count,
#     'green_4':  State.green_4_count,
#     'white_1':  State.white_1_count,
#     'white_2':  State.white_2_count,
#     'white_3':  State.white_3_count,
#     'black_1':  State.black_1_count,
#     'yellow_1': State.yellow_1_count,
#     'yellow_2': State.yellow_2_count,
#     'yellow_4': State.yellow_4_count,
#     'purple_1': State.purple_1_count,
# }

# def token_badge(name: str) -> rx.Component:
#     if not name in color_funcs.keys():
#         return rx.box()
#     return rx.badge(color_funcs.get(name), variant="solid", color_scheme="green",
#             style=badge_style)

# def token(name: rx.Var[str]) -> rx.Component:
#     # return rx.text(name)
#     if not name in color_funcs.keys():
#         return rx.box(f'{name in color_funcs.keys()}')
#     return rx.container(
#         rx.badge("-", variant="solid", color_scheme="gray",
#             on_click=State.token_removed(name), cursor="pointer",
#             style=remove_style),
#         rx.image(src=f"{name}.png",
#             width="50px", height="auto",
#             on_click=State.token_pressed(name),
#             ),
#         token_badge(name),
#         style={"position":"relative"},
#     )

# def token_row(color: str) -> rx.Component:
#     return rx.hstack(
#         rx.foreach(
#             State.color_val[color],
#             # State.oranges,
#             # lambda val: token(f"{color}_{val}"),
#             lambda val: rx.text(f"{color_funcs}")
#         ),
#     )