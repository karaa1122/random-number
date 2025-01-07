import random
from .models import UniqueNumbers

SARCASTIC_MESSAGES = [
    "Wow, another number. Your life must be thrilling!",
    "Here's a number. Don't spend it all in one place!",
    "Bet you’ll frame this one and hang it on your wall.",
    "Congrats, this is as unique as it gets… just like everyone else.",
    "A one-of-a-kind number for your zero-of-a-kind personality!",
    "Here’s your rare number. We’re totally impressed. Not.",
    "Unique? Sure. Valuable? Eh, not so much.",
    "This number is yours forever. Aren’t you special?",
    "You clicked a button. Groundbreaking stuff.",
    "Keep going; maybe you’ll find meaning in this. Or not.",
]

def generate_unique_number_and_message():
    while True:
        number = random.randint(1, 10**12)
        if not UniqueNumbers.objects.filter(number=number).exists():
            UniqueNumbers.objects.create(number=number)
            message = random.choice(SARCASTIC_MESSAGES)
            return number, message
