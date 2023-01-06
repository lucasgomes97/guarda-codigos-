import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
num = "0123456789"
symbol = "[]{}#()*;._-!?*&%$#@/"
ans = lower_case + upper_case + num + symbol
length = 9
password = "".join(random.sample(ans,length))
print(password)
