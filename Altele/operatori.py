'''
Operatori:
aritmetici: +, -, *, /, %
de comparare: < >, ==, !=, >=, <=
logici: and, or, !(not)
'''

a = 3
b = 5

# print(a+b) # a+b=? => 5
# print(a == b) # a=b? =>False
# print(a<b and a<4) # True SI True => True
# print(a<b or a<2) # True SAU False => True

# cu mama sau tata sau (bunicul si bunica)
mama = True
tata = False
bunicul = False
bunica = True

print(mama and tata or (bunicul and bunica))