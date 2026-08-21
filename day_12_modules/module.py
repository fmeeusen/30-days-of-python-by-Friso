import random
import string
print(string.ascii_letters)
def random_user_id() -> list:
    no_characters = input('Number of characters: ')
    no_ids = input('number of id: ')
    ids = []
    for i in range(int(no_ids)):
        ids.append(''.join(random.choice(string.ascii_letters+string.digits) for _ in range(int(no_characters))))
    return ids

def rgb_color_gen() -> list:
    rgb_colors = []
    for i in range(3):
        rgb_colors.append(random.randint(0,255))
    return rgb_colors

print(random_user_id())
