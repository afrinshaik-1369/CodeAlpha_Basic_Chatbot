import random

R_EATING ="I dont like eating anything because I'm a bot obviously!"
def unknown():
    response = ['could you please re-phrase that?',
                "...",
                "sound about right",
                "what does that mean?"][random.randrange(4)]
    return response