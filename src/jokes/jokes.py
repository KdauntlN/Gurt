import random

jokes = [
    ("Did you hear about the player who told the witch her house was destroyed?", "*In turn, she destroyed him!*"),
    ("Did you hear about the player who blew himself up with TNT?", "*I'm sure you can guess what happened!*"),
    ("Did you hear about the player who thought he could fly in survival mode?", "*He couldn't!*"),
    ("Did you hear about the player that walked in on two creepers?", "*He was destroyed!*"),
    ("Did you hear about the player that tried to farm in the Nether?", "*He was destroyed!*"),
    ("Did you hear about the player who tried to put a saddle on a creeper?", "*He went boom!*"),
    ("Did you hear about the player who was pushed into the ravine when the water fell on him?", "*He went splash!*")
]

def pick_joke() -> tuple[str, str]:
    picked_joke = jokes[random.randint(0, 6)]
    return (picked_joke[0], picked_joke[1])