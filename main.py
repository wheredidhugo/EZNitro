import string
import numpy
import requests
import time
import random
from colorama import Fore, Style


class eznitro():
    def main(self):
        print("""
███████ ███████ ███    ██ ██ ████████ ██████   ██████
██         ███  ████   ██ ██    ██    ██   ██ ██    ██
█████     ███   ██ ██  ██ ██    ██    ██████  ██    ██
██       ███    ██  ██ ██ ██    ██    ██   ██ ██    ██
███████ ███████ ██   ████ ██    ██    ██   ██  ██████   by wheredidhugo
        """)

        def askingCodes():
            try:
                return int(input("How much codes do you want to generate? "))
            except ValueError:
                print("Input is not a number, try again.")
                askingCodes()

        codes = askingCodes()

        def nextCodeCheck():
            try:
                nextCodeCheckInt = int(
                    input("Next code check time in seconds (Press Enter for default settings): "))
                return nextCodeCheckInt
            except ValueError:
                return 12.1

        reCheck = nextCodeCheck()

        chars = []
        chars[:0] = string.ascii_letters + string.digits
        valid = []
        invalid = 0

        generatedCodes = numpy.random.choice(
            chars, size=[codes, random.randint(16, 24)])

        for s in generatedCodes:
            code = "".join(x for x in s)
            result = self.checker(code)
            if result == 0:
                valid.append(code)
                print(
                    f"{Fore.GREEN}{len(valid)+invalid}/{codes} | Valid: {len(valid)} | https://discord.gift/{code}{Style.RESET_ALL}")
            elif result == 1:
                invalid += 1
                print(
                    f"{Fore.RED}{len(valid)+invalid}/{codes} | Invalid: {invalid} | https://discord.gift/{code}{Style.RESET_ALL}")
            elif result == 2:
                ratelimit = input(
                    f"{Fore.YELLOW}You are ratelimited, press Ctrl + C to exit or press Enter to continue{Style.RESET_ALL}")
            if len(valid) + invalid != codes:
                time.sleep(reCheck)

        print(f"""
Results:
{Fore.GREEN}Valid: {len(valid)}{Style.RESET_ALL}
{Fore.RED}Invalid: {invalid}{Style.RESET_ALL}
Valid codes: {', '.join(valid)}
        """)

    def checker(self, code):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        responseJSON = response.json()

        if response.status_code == 200:
            if responseJSON["uses"] == responseJSON["max_uses"]:
                return 1
            else:
                with open("Nitro Codes.txt", "w") as file:
                    file.write(code)
                return 0
        elif response.status_code == 404 or response.status_code == 405:
            return 1
        elif response.status_code == 429:
            return 2


if __name__ == "__main__":
    eznitro().main()
