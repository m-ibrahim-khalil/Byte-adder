from input_handler import InputHandler
from logic_gates import LogicGate


class App():
    """The class exposed all user level functionalities.
    The class initialize the Byte-adder app accourding to the user choice.
    """

    def __init__(self, isBinary=False, isSigned=False) -> None:
        """Initialize App object according to user choice

        Args:
            isBinary (bool, optional): If user choose to add two binary numbers 
                        isBinary will be True otherwise False. Defaults to False.
            isSigned (bool, optional): If user choose to handle negative integers 
                        isSign will be True otherwise False. Defaults to False.
        """
        self.isBinary = isBinary
        self.isSigned = isSigned
        self.inputObject = InputHandler(self.isSigned, self.isBinary)
        self.logicGate = LogicGate(isSigned)

    def add(self) -> None:
        """The function generate byte-adder result and display the result.
        """
        num1, num2, = self.inputObject.userInput()
        sum = self.logicGate.binary_adder(num1, num2)
        print(
            f"{self.binToInt(num1)}({num1}) + {self.binToInt(num2)}({num2}) = {self.binToInt(sum)}({sum})")

    def binToInt(self, number) -> str:
        if self.isSigned:
            val = int(number[1:], 2)
            return '-' + str(val) if number[0] == '1' else str(val)
        return str(int(number, 2))


if __name__ == "__main__":
    print(
        f"\n\tWelcome to BYTE-ADDER😍. Please Enter your choice [a-e]:\n\t\t ✔ a)Add two binary unsigned numbers\n\t\t ✔ b)Add two Decimal unsigned numbers\n\t\t ✔ c)Add two binary signed numbers\n\t\t ✔ d)Add two decimal signed numbers\n\t\t ✔ e)Exit from the program\n")
    while(True):
        choice = input().strip()
        if choice == 'a':
            app = App(isBinary=True)
            app.add()
        elif choice == 'b':
            app = App()
            app.add()
        elif choice == 'c':
            app = App(isBinary=True, isSigned=True)
            app.add()
        elif choice == 'd':
            app = App(isSigned=True)
            app.add()
        elif choice == 'e':
            print("Thanks for using me..😍")
            break
        else:
            print(
                "Invalid input 😖. Please Look up the options carefully😵.\n\nPlease Enter your choice [a-e]:\n\t\t ✔ a)Add two binary unsigned numbers\n\t\t ✔ b)Add two Decimal unsigned numbers\n\t\t ✔ c)Add two binary signed numbers\n\t\t ✔ d)Add two decimal signed numbers\n\t\t ✔ e)Exit from the program\n ")
