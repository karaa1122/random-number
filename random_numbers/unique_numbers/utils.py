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
    "Here’s a number that’s about as exciting as watching paint dry.",
    "A truly groundbreaking achievement. Give yourself a pat on the back.",
    "Another number, because why not waste a few more seconds of your life?",
    "This is the pinnacle of human achievement… or not.",
    "Behold! A number that will totally change your life. (Spoiler: it won’t.)",
    "A life-altering number, assuming your life is already pretty boring.",
    "Another step closer to absolutely nothing of significance.",
    "You’ve unlocked… a number. I’m sure the world is so grateful.",
    "Your quest for uniqueness has led to… this. Well done?",
    "This number is as unique as the way you waste your time.",
    "You’ve done it! You’ve achieved the impossible: mediocrity.",
    "A special number, for a not-so-special occasion.",
    "Don’t get too excited. It’s just a number, not a lottery win.",
    "Celebrate! You’re now the proud owner of a meaningless integer.",
    "Your persistence has been rewarded with… a number. Wow.",
    "Here’s your number. Try not to get emotional about it.",
    "Brace yourself, this number is going to blow your mind. Or not.",
    "You’ve reached peak productivity: clicking for a random number.",
    "This number is so unique, even your dog wouldn’t care.",
    "Another unique number for your collection of things that don’t matter."
]

def generate_unique_number_and_message():
    while True:
        number = random.randint(1, 10**12)
        if not UniqueNumbers.objects.filter(number=number).exists():
            UniqueNumbers.objects.create(number=number)
            message = random.choice(SARCASTIC_MESSAGES)
            return number, message
