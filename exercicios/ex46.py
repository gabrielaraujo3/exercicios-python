from time import sleep
import emoji
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(emoji.emojize(":fireworks: :fireworks: :fireworks: :fireworks:", use_aliases=True))
