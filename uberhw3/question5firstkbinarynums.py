def generate_binary_numbers(k):
    binary_numbers = ["0", "1"]
    
    for i in range(2, k):
        binary_numbers.append(binary_numbers[i - 2] + "0")
        binary_numbers.append(binary_numbers[i - 2] + "1")

    return binary_numbers[:k]