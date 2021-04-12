# DiscordNitroGeneratorCheckerSRC
import random, string, requests
f=open("Dobre Nitro.txt", "w", encoding='utf-8')

print("made by voxeliq")


while True:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if r.status_code == 1:
        print(f"Działające nitro >>> discord.gift/{code}")
        f.write(f"discord.gift/{code}\n")

    else
        print("Nie działające nitro >>> discord.gift/{code}")
