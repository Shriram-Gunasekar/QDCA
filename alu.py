class QuantumDot:
    def __init__(self, state=0):
        self.state = state  # 0 or 1

class QDCAALU:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = [QuantumDot(0) for _ in range(len(input1.state))]

    def perform_addition(self):
        carry = QuantumDot(0)
        for i in range(len(self.input1.state)):
            sum_xor = self.input1.state[i] ^ self.input2.state[i] ^ carry.state
            carry_and1 = (not self.input1.state[i]) & self.input2.state[i]
            carry_and2 = self.input1.state[i] & (not self.input2.state[i])
            carry_xor = carry_and1 | carry_and2

            self.output[i].state = sum_xor
            carry.state = carry_xor

    def perform_subtraction(self):
        borrow = QuantumDot(0)
        for i in range(len(self.input1.state)):
            diff_xor = self.input1.state[i] ^ self.input2.state[i] ^ borrow.state
            borrow_and1 = (not self.input1.state[i]) & self.input2.state[i]
            borrow_and2 = self.input1.state[i] & (not self.input2.state[i])
            borrow_xor = borrow_and1 | borrow_and2

            self.output[i].state = diff_xor
            borrow.state = borrow_xor

    def perform_logical_and(self):
        for i in range(len(self.input1.state)):
            self.output[i].state = self.input1.state[i] & self.input2.state[i]

    def perform_logical_or(self):
        for i in range(len(self.input1.state)):
            self.output[i].state = self.input1.state[i] | self.input2.state[i]

    def perform_logical_xor(self):
        for i in range(len(self.input1.state)):
            self.output[i].state = self.input1.state[i] ^ self.input2.state[i]

    def get_output(self):
        return [dot.state for dot in self.output]

# Example usage
input1 = [QuantumDot(1), QuantumDot(0), QuantumDot(1)]  # Binary representation of 5
input2 = [QuantumDot(0), QuantumDot(1), QuantumDot(1)]  # Binary representation of 3

alu = QDCAALU(input1, input2)
alu.perform_addition()
output_addition = alu.get_output()

alu.perform_subtraction()
output_subtraction = alu.get_output()

alu.perform_logical_and()
output_and = alu.get_output()

alu.perform_logical_or()
output_or = alu.get_output()

alu.perform_logical_xor()
output_xor = alu.get_output()

print("Output Addition (Binary):", output_addition)
print("Output Subtraction (Binary):", output_subtraction)
print("Output Logical AND (Binary):", output_and)
print("Output Logical OR (Binary):", output_or)
print("Output Logical XOR (Binary):", output_xor)
