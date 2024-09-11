import random
import sys
import os

def generate_random_name(prefix='var'):
    return f"{prefix}_{random.randint(1000, 9999)}"

def create_new_version():
    caesar_func = generate_random_name('caesar_cipher')
    dynamic_func = generate_random_name('dynamic_operation')
    obfuscated_func = generate_random_name('obfuscated_code')
    encryption_func = generate_random_name('advanced_encryption')
    check_func = generate_random_name('check_magic_number')

    new_code = f"""
import random
import sys

def {caesar_func}(data, shift):
    decrypted = []
    for c in data:
        if c.isprintable() and c.isascii():
            decrypted.append(chr(ord(c) - shift))
        else:
            decrypted.append(c)
    return ''.join(decrypted)

def {dynamic_func}(a, b):
    operations = [
        ('addition', lambda x, y: x + y),
        ('subtraction', lambda x, y: x - y),
        ('multiplication', lambda x, y: x * y),
        ('division', lambda x, y: x / y if y != 0 else 'undefined'),
        ('exponentiation', lambda x, y: x ** y)
    ]
    operation_name, operation_func = random.choice(operations)
    return operation_name, operation_func(a, b)

def {obfuscated_func}():
    p = 0b0101
    q = 0b0011
    r = (p ^ q) + (p & q)

    if r % 2 == 0:
        final_result = sum([(p << i) ^ (q >> i) for i in range(4)])
    else:
        final_result = (p + q) % 10

    return final_result

def {encryption_func}(data):
    shift = random.randint(1, 5)
    encrypted = ''.join(chr((ord(c) + shift) % 256) for c in data)
    return encrypted, shift

def {check_func}():
    MAGIC_NUMBER_OCTAL = 0o1234
    calculated_value = (MAGIC_NUMBER_OCTAL * 2 + 5) % 100
    print(f"Magic number (octal): {{MAGIC_NUMBER_OCTAL}}")
    print(f"Calculated value: {{calculated_value}}")
    return calculated_value == 41

def main():
    if not {check_func}():
        print("Invalid runtime conditions. Exiting.")
        sys.exit(1)

    encrypted_message = "Uifsf!jt!b!tfdsfu!nfttbhf!"
    shift = 1
    decrypted_message = {caesar_func}(encrypted_message, shift)
    print(decrypted_message)

    extra_message = "Extra message for encryption!"
    encrypted_extra_message, enc_shift = {encryption_func}(extra_message)
    print(f"Encrypted extra message: {{encrypted_extra_message}} (Shift: {{enc_shift}})")

    print("Simple Program: Dynamic Operation")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation_name, result = {dynamic_func}(num1, num2)
    print(f"The result of {{operation_name}} between {{num1}} and {{num2}} is {{result}}")

    obfuscated_result = {obfuscated_func}()
    print(f"Obfuscated code: {{obfuscated_result}}")

if __name__ == "__main__":
    main()
"""

    file_name = f"polymorphic_{random.randint(1000, 9999)}.py"
    with open(file_name, 'w') as f:
        f.write(new_code)

    print(f"New version: {file_name}")

if __name__ == "__main__":
    create_new_version()
