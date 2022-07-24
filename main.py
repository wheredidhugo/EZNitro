import string
import numpy
import requests

class eznitro():
    def main(self):
        def askingCodes():
            try:
                return int(input("How much codes do you want to generate? "))
            except ValueError:
                print("Input is not a number, try again.")
                askingCodes()

        codes = askingCodes()

        chars = []
        chars[:0] = string.ascii_letters + string.digits
        valid = 0
        invalid = 0

        generatedCodes = numpy.random.choice(chars, size=[codes, 23])

        for s in generatedCodes:
            code = "".join(x for x in s)
            result = self.checker(code)
            if result = 0:
                valid += 1
                print(f"{valid+invalid}/{codes} | Valid: {valid} | https://discord.gift/{code}")
            elif result = 1:
                invalid += 1
                print(f"{valid+invalid}/{codes} | Invalid: {invalid} | https://discord.gift/{code}")
            elif result = 2:


    def checker(self, code):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            return 0
        elif response.status_code == 404:
            return 1
        elif response.status_code == 429:
            return 2


if __name__ == "__main__":
    eznitro().main()