def decimal_to_binary(num):
    if num == 0:
        return "0"
    
    sign = ""
    if num < 0:
        sign = "-"
        num = abs(num)
    
    integer_part = int(num)
    fractional_part = num - integer_part
    
    binary_integer = []
    if integer_part > 0:
        temp = integer_part
        print(f"  整数部分转换 ({integer_part} → 二进制):")
        while temp > 0:
            remainder = temp % 2
            binary_integer.append(str(remainder))
            print(f"    {temp} ÷ 2 = {temp // 2} ... 余数 {remainder}")
            temp = temp // 2
        binary_integer.reverse()
    else:
        binary_integer = ["0"]
    
    binary_fractional = []
    if fractional_part > 0:
        temp = fractional_part
        print(f"  小数部分转换 ({fractional_part:.6f} → 二进制):")
        precision = 20
        count = 0
        while temp > 0 and count < precision:
            original = temp
            temp *= 2
            integer = int(temp)
            binary_fractional.append(str(integer))
            print(f"    {original:.6f} × 2 = {temp:.6f} ... 整数 {integer}")
            temp -= integer
            count += 1
    
    result = sign + "".join(binary_integer)
    if binary_fractional:
        result += "." + "".join(binary_fractional)
    
    return result


def binary_to_decimal(binary_str):
    if not binary_str:
        return 0
    
    sign = 1
    if binary_str.startswith("-"):
        sign = -1
        binary_str = binary_str[1:]
    
    if "." in binary_str:
        integer_part_str, fractional_part_str = binary_str.split(".", 1)
    else:
        integer_part_str = binary_str
        fractional_part_str = ""
    
    decimal_integer = 0
    if integer_part_str:
        print(f"  整数部分转换 ({integer_part_str} → 十进制):")
        n = len(integer_part_str)
        for i in range(n):
            digit = int(integer_part_str[i])
            exponent = n - 1 - i
            value = digit * (2 ** exponent)
            decimal_integer += value
            print(f"    {digit} × 2^{exponent} = {value}")
        print(f"    整数部分总和: {decimal_integer}")
    
    decimal_fractional = 0
    if fractional_part_str:
        print(f"  小数部分转换 ({fractional_part_str} → 十进制):")
        n = len(fractional_part_str)
        for i in range(n):
            digit = int(fractional_part_str[i])
            exponent = -(i + 1)
            value = digit * (2 ** exponent)
            decimal_fractional += value
            print(f"    {digit} × 2^{exponent} = {value}")
        print(f"    小数部分总和: {decimal_fractional:.6f}")
    
    return sign * (decimal_integer + decimal_fractional)


def binary_to_octal(binary_str):
    if "." in binary_str:
        integer_part, fractional_part = binary_str.split(".", 1)
    else:
        integer_part = binary_str
        fractional_part = ""
    
    print(f"  二进制整数部分分组 ({integer_part}):")
    pad_length = (3 - len(integer_part) % 3) % 3
    padded_integer = "0" * pad_length + integer_part
    print(f"    补零后: {padded_integer}")
    
    octal_integer = []
    for i in range(0, len(padded_integer), 3):
        group = padded_integer[i:i+3]
        octal_digit = str(int(group, 2))
        octal_integer.append(octal_digit)
        print(f"    分组 {group} → 八进制 {octal_digit}")
    
    octal_fractional = []
    if fractional_part:
        print(f"  二进制小数部分分组 ({fractional_part}):")
        pad_length = (3 - len(fractional_part) % 3) % 3
        padded_fractional = fractional_part + "0" * pad_length
        print(f"    补零后: {padded_fractional}")
        
        for i in range(0, len(padded_fractional), 3):
            group = padded_fractional[i:i+3]
            octal_digit = str(int(group, 2))
            octal_fractional.append(octal_digit)
            print(f"    分组 {group} → 八进制 {octal_digit}")
    
    result = "".join(octal_integer)
    if octal_fractional:
        result += "." + "".join(octal_fractional)
    
    return result


def binary_to_hex(binary_str):
    hex_chars = "0123456789ABCDEF"
    if "." in binary_str:
        integer_part, fractional_part = binary_str.split(".", 1)
    else:
        integer_part = binary_str
        fractional_part = ""
    
    print(f"  二进制整数部分分组 ({integer_part}):")
    pad_length = (4 - len(integer_part) % 4) % 4
    padded_integer = "0" * pad_length + integer_part
    print(f"    补零后: {padded_integer}")
    
    hex_integer = []
    for i in range(0, len(padded_integer), 4):
        group = padded_integer[i:i+4]
        hex_digit = hex_chars[int(group, 2)]
        hex_integer.append(hex_digit)
        print(f"    分组 {group} → 十六进制 {hex_digit}")
    
    hex_fractional = []
    if fractional_part:
        print(f"  二进制小数部分分组 ({fractional_part}):")
        pad_length = (4 - len(fractional_part) % 4) % 4
        padded_fractional = fractional_part + "0" * pad_length
        print(f"    补零后: {padded_fractional}")
        
        for i in range(0, len(padded_fractional), 4):
            group = padded_fractional[i:i+4]
            hex_digit = hex_chars[int(group, 2)]
            hex_fractional.append(hex_digit)
            print(f"    分组 {group} → 十六进制 {hex_digit}")
    
    result = "".join(hex_integer)
    if hex_fractional:
        result += "." + "".join(hex_fractional)
    
    return result


def octal_to_binary(octal_str):
    octal_to_bin = {
        "0": "000", "1": "001", "2": "010", "3": "011",
        "4": "100", "5": "101", "6": "110", "7": "111"
    }
    
    if "." in octal_str:
        integer_part, fractional_part = octal_str.split(".", 1)
    else:
        integer_part = octal_str
        fractional_part = ""
    
    print(f"  八进制整数部分转换 ({integer_part}):")
    binary_integer = []
    for digit in integer_part:
        binary = octal_to_bin[digit]
        binary_integer.append(binary)
        print(f"    {digit} → {binary}")
    
    binary_fractional = []
    if fractional_part:
        print(f"  八进制小数部分转换 ({fractional_part}):")
        for digit in fractional_part:
            binary = octal_to_bin[digit]
            binary_fractional.append(binary)
            print(f"    {digit} → {binary}")
    
    result = "".join(binary_integer).lstrip("0") or "0"
    if binary_fractional:
        result += "." + "".join(binary_fractional).rstrip("0")
    
    return result


def hex_to_binary(hex_str):
    hex_to_bin = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111",
        "a": "1010", "b": "1011", "c": "1100", "d": "1101",
        "e": "1110", "f": "1111"
    }
    
    if "." in hex_str:
        integer_part, fractional_part = hex_str.split(".", 1)
    else:
        integer_part = hex_str
        fractional_part = ""
    
    print(f"  十六进制整数部分转换 ({integer_part}):")
    binary_integer = []
    for digit in integer_part:
        binary = hex_to_bin[digit]
        binary_integer.append(binary)
        print(f"    {digit} → {binary}")
    
    binary_fractional = []
    if fractional_part:
        print(f"  十六进制小数部分转换 ({fractional_part}):")
        for digit in fractional_part:
            binary = hex_to_bin[digit]
            binary_fractional.append(binary)
            print(f"    {digit} → {binary}")
    
    result = "".join(binary_integer).lstrip("0") or "0"
    if binary_fractional:
        result += "." + "".join(binary_fractional).rstrip("0")
    
    return result


def unicode_utf8_analysis(text):
    print(f"  字符 | Unicode编号 | UTF-8编码")
    print(f"  {'-'*40}")
    for char in text:
        unicode_code = ord(char)
        utf8_bytes = char.encode('utf-8')
        utf8_hex = " ".join(f"{b:02X}" for b in utf8_bytes)
        print(f"  '{char}' | U+{unicode_code:04X} | {utf8_hex}")


def main():
    print("=" * 70)
    print("【题目1】十进制转二进制")
    print("=" * 70)
    
    decimal_tests = [57, 128, 12.5, 7.198, 3972, 1.35, 1000]
    for num in decimal_tests:
        print(f"\n{'='*50}")
        print(f"【十进制】{num}")
        binary = decimal_to_binary(num)
        print(f"【二进制】{binary}")
    
    print("\n" + "=" * 70)
    print("【题目2】二进制转十进制")
    print("=" * 70)
    
    binary_tests = ["11010", "110", "11.101", "0.1011", "111.11", "111111"]
    for binary_str in binary_tests:
        print(f"\n{'='*50}")
        print(f"【二进制】{binary_str}")
        decimal = binary_to_decimal(binary_str)
        print(f"【十进制】{decimal}")
    
    print("\n" + "=" * 70)
    print("【题目3】二进制转八进制和十六进制")
    print("=" * 70)
    
    binary_to_convert = ["101110101", "1101100.11"]
    for binary_str in binary_to_convert:
        print(f"\n{'='*50}")
        print(f"【二进制】{binary_str}")
        octal = binary_to_octal(binary_str)
        print(f"【八进制】{octal}")
        hex_str = binary_to_hex(binary_str)
        print(f"【十六进制】{hex_str}")
    
    print("\n" + "=" * 70)
    print("【题目3】八进制转二进制")
    print("=" * 70)
    
    octal_to_convert = ["3756", "415.213"]
    for octal_str in octal_to_convert:
        print(f"\n{'='*50}")
        print(f"【八进制】{octal_str}")
        binary = octal_to_binary(octal_str)
        print(f"【二进制】{binary}")
    
    print("\n" + "=" * 70)
    print("【题目3】十六进制转二进制")
    print("=" * 70)
    
    hex_to_convert = ["C6F0", "5AB.4D"]
    for hex_str in hex_to_convert:
        print(f"\n{'='*50}")
        print(f"【十六进制】{hex_str}")
        binary = hex_to_binary(hex_str)
        print(f"【二进制】{binary}")
    
    print("\n" + "=" * 70)
    print("【题目4】Unicode编号和UTF-8编码")
    print("=" * 70)
    
    text = "Python语言基础与人工智能应用"
    print(f"\n【字符串】{text}")
    unicode_utf8_analysis(text)


if __name__ == "__main__":
    main()