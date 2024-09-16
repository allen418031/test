num_tests = int(input())

for _ in range(num_tests):
    binary_str = input()
    complement = ''.join(['0' if bit == '1' else '1' for bit in binary_str])
    print(complement)
