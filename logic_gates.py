

class LogicGate():
    """This class contains all bit-wise logical bit-wise operation 
    """

    def __init__(self, isSigned=False) -> None:
        """Initilize logic gate

        Args:
            isSigned (bool, optional): if we consider sign bit or not. Defaults to False.
        """
        self.isSigned = isSigned
        self.complement = 0

    def half_adder(self, a, b) -> tuple:
        """It recieve 2 bit and return their bit-wise addition value
        examples:
        0 + 1 = 1 and carry_bit 0
        1 + 1 = 1 and carry_bit 1

        Args:
            a (integer): 0 or 1
            b (integer): 0 or 1

        Returns:
            tuple: 2 binary digits separated by comma
        """
        sum = a ^ b  # XOR gate
        carry_bit = a & b  # AND gate
        return sum, carry_bit

    def full_adder(self, a, b, carry_bit) -> tuple:
        """The function uses 2 half_adder for handling carry_bit
        from previous operation

        Args:
            a (integer): 0 or 1
            b (integer): 0 or 1
            carry_bit (integer):  0 or 1

        Returns:
            tuple: 2 binary digits separated by comma
        """
        sum1, carry_bit1 = self.half_adder(a, carry_bit)
        sum, carry_bit2 = self.half_adder(sum1, b)
        carry_bit = carry_bit1 | carry_bit2
        return sum, carry_bit

    def binary_adder(self, a, b) -> str:
        """It takes two 8-bit binary number and perform bit-wise addition
        on them. It uses full_adder function for the binary addition

        Args:
            a (string): '01110011'
            b (string): '11110011'

        Returns:
            str: result of addition of 2 inputs in binary format
        """
        if self.isSigned:
            if a[0] == '1':
                # print(f"twos complement of a: {a} -> ")
                a = self.twosComplement(a)
                # print(a)
                self.complement += 1
            if b[0] == '1':
                # print(f"twos complement of b: {b} -> ")
                b = self.twosComplement(b)
                # print(b)
                self.complement += 1

        bits_a = self.string_to_bits(a)
        bits_b = self.string_to_bits(b)

        res = []
        carry_bit = 0

        for i in range(len(bits_a)-1, -1, -1):
            sum, carry_bit = self.full_adder(bits_a[i], bits_b[i], carry_bit)
            res.append(sum)
        res.append(carry_bit)

        if self.isSigned:
            print(len(res))
            res = res[:8]

        res.reverse()
        res = ''.join(str(x) for x in res)

        if self.complement > 0:
            sign_bit = res[0]
            print(f"sign bit: {sign_bit}")
            res = self.twosComplement(res)
            res = list(res)
            res[0] = sign_bit
        return ''.join(res)

    def twosComplement(self, number: str) -> str:
        """compute 2's complement to negate a binary number

        Args:
            number (str): a negative binary number 

        Returns:
            str: 2's complement of a negative binary number
        """
        i = len(number)-1
        while(i >= 1):
            if number[i] == '1':
                break
            i -= 1
        if i < 0:
            return number
        j = i-1
        while(j >= 1):
            if number[j] == '1':
                number = list(number)
                number[j] = '0'
                number = ''.join(number)
            else:
                number = list(number)
                number[j] = '1'
                number = ''.join(number)
            j -= 1
        return number

    def string_to_bits(self, a) -> list:
        """it recieve a string and change it type to a list of integers
        example: 
        '11110011' -> [1, 1, 1, 1, 0, 0, 1, 1]

        Args:
            a (string): binary format of user input

        Returns:
            list: a list of integers value
        """
        return [int(x) for x in a]
