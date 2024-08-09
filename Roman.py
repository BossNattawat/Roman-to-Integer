s = input("Enter a roman number : ").upper()

result = 0

s = s.replace("IV", "IIII").replace("IX", "VIIII")
s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

for i in range(len(s)):
    if s[i] == "I": result += 1
    elif s[i] == "V": result += 5
    elif s[i] == "X": result += 10
    elif s[i] == "L": result += 50
    elif s[i] == "C": result += 100
    elif s[i] == "D": result += 500
    elif s[i] == "M": result += 1000

print(result)