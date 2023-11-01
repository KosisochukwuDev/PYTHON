variable = "Welcome Home"
print(variable.replace("Welcome","Come" ))
age = 16
pencil = 30
price = 20.00
sentence = "I am {} and I bought {} pencils for {} naira."
print(sentence.format(age, pencil,price))

age = 16
pencil = 30
price = 20.00
sentence = f"I am {age} and I bought {pencil} pencils for {price} naira."
print(sentence)

age = 16
pencil = 30
price = 20.00
sentence = "I bought {1} pencils for {2} naira  and I am {0}."
print(sentence.format(age, pencil, price))

age = str(16)
pencil = str(30)
price = str(20.00)
sentence = "I am " + age+" and I bought "+pencil+" pencils for "+price+" naira."
print(sentence.format(age, pencil,price))