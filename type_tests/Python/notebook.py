import logging
import sys
from datetime import date

def get_info():
    user = user_info.get_user_info_for_current_platform()
    mitt_team = user.current_team
    min_bruker = user.short_email

class User():
    def __init__(self, short_name, id, name, owner):
        self.short_name = short_name
        self.id = id
        self.name = name
        self.owner = owner

def display_info(variabler: list):
    col_widths = [30, 10, 20, 50]

    header = "{:<{}} | {:<{}} | {:<{}} | {:<{}}".format(
        "Kortnavn",
        col_widths[0],
        "Id",
        col_widths[1],
        "Eier team",
        col_widths[2],
        "Navn",
        col_widths[3],
    )
    print(header)
    print("-" * len(header))

    for variabel in variabler:
        print(
            "{:<{}} | {:<{}} | {:<{}} | {:<{}}".format(
                variabel.short_name,
                col_widths[0],
                variabel.id,
                col_widths[1],
                variabel.owner["team"],
                col_widths[2],
                variabel.name["nb"],
                col_widths[3],
            )
        )