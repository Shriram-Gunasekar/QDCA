class QDCAMultiplier:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.product = [QuantumDot(0) for _ in range(len(input1.state) + len(input2.state))]

    def perform_multiplication(self):
        # Perform multiplication using QDCA principles
        for i in range(len(self.input1.state)):
            for j in range(len(self.input2.state)):
                self.product[i + j].state ^= self.input1.state[i] & self.input2.state[j]

    def get_product_output(self):
        return [dot.state for dot in self.product]

# Example usage
input1 = [QuantumDot(1), QuantumDot(0), QuantumDot(1)]  # Binary representation of 5
input2 = [QuantumDot(1), QuantumDot(1)]  # Binary representation of 3

multiplier = QDCAMultiplier(input1, input2)
multiplier.perform_multiplication()

product_output = multiplier.get_product_output()
product_decimal = int("".join(str(bit) for bit in product_output), 2)

print("Product Output (Binary):", product_output)
print("Product Output (Decimal):", product_decimal)
