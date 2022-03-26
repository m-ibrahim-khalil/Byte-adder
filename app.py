from input_handler import InputHandler


class App():
    """The class exposed all user level functionalities
    """

    def __init__(self, isBinary=False, isSigned=False) -> None:
        self.isBinary = isBinary
        self.isSigned = isSigned
        self.inputObject = InputHandler(self.isSigned, self.isBinary)

    def add(self):
        num1, num2, = self.inputObject.userInput()
        print(num1, num2)


if __name__ == "__main__":
    print(
        f"Welcome to BYTE-ADDER! Please Enter your choice [a-e]:\n\t\t a)Add two binary unsigned numbers\n\t\t b)Add two Decimal unsigned numbers\n\t\t c)Add two binary signed numbers\n\t\t d)Add two decimal signed numbers\n\t\t e)Exit from the program\n")
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
            print("Invalid input. ")
