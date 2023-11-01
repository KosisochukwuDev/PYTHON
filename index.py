email = "user@example.com"
print(email[5:])
long_string = "abcdefghijklmnopqrstuvwxyz"
print(long_string[0:4])
print(long_string[23:])
print(long_string[16])
# to convert all the characters individually in a list using unpack(*) method.
print([*long_string])
sentence = "This is a sample sentence."
extraction = sentence.split(' ')
print(extraction[3])
print(extraction[4])
data = ("Name: John, Age: 30, City: New York")
extraction = data.split(' ')
print(extraction[1], extraction[3], extraction[5])
numbers = "1234567890"
print(numbers[1], numbers[3], numbers[5], numbers[7], numbers[9])




