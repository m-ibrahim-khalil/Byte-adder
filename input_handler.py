
class InputHandler():
    """Take valid inputs from user
    """

    def __init__(self, isSign=False, isBinary=False) -> None:

        self.isBinary = isBinary
        self.isSign = isSign
        self.max = 127 if isSign else 255
        self.min = -127 if isSign else 0
        self.inputs = []

    def userInput(self) -> list:
        """take user inputs
        """
        iter = 0
        print(f"I am a Byte-Adder! Please Enter two Binary/Decimal number..")
        while True:
            x1 = input(
                f"Enter your {'2nd' if iter%2 else '1st'} number: ").strip()
            if self.is_valid(x1):
                iter += 1
                if self.isBinary:
                    self.inputs.append('0'*(8-len(x1))+x1)
                else:
                    self.inputs.append(self.convertBinary(x1))

            if iter == 2:
                break
        return self.inputs

    def is_valid(self, number: str) -> bool:
        """checking the input is either binary or decimals

        Args:
            number (str): user-input

        Returns:
            bool: return True if it is a valid number
        """
        decimals = ['0', '1', '3', '2', '4', '5', '6', '7', '8', '9']
        binaries = ['0', '1']
        isValid = True

        if self.isBinary:
            if len(number) > 8:
                isValid = False
                print("Your binary number has more than 8 bit!\nPlease try again.")
            else:
                for digit in number:
                    # print(digit, type(digit))
                    if digit not in binaries:
                        isValid = False
                        print(
                            f"Your input {number} is not valid number! \nPlease Try again.")
                        break
        else:
            if self.isSign and number[0] == '-':
                number = number[1:]
            for digit in number:
                if digit not in decimals:
                    isValid = False
                    print(
                        f"Your input {number} is not valid number! \nPlease Try again.")
                    break
            number = int(number)
            if number < self.min or number > self.max:
                isValid = False
                print(
                    f"Your input {number} is out of range [{self.min}, {self.max}]! \nPlease Try again.")

        return isValid

    def convertBinary(self, number) -> str:
        temp = bin(int(number))
        signbit = '1' if number[0] == '-' else '0'
        temp = temp[3:] if number[0] == '-' else temp[2:]
        n = 8-len(temp) - 1
        return signbit+'0'*n+temp
