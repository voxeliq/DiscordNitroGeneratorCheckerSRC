import random, string, requests
f=open("Valid Nitro.txt", "w", encoding='utf-8')

print("generator stworzony przez Voxeliq")


while True:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if r.status_code == 1:
        print(f" ✓ Working Nitro Code >>> discord.gift/{code}")
        f.write(f"discord.gift/{code}\n")
    
    else:
        print(f" × Don't working nitro code >>> discord.gift/{code}")
