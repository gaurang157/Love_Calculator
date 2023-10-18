print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

c_n = name1 + name2
l_n = c_n.lower()
t = l_n.count("t")
r = l_n.count("r")
u = l_n.count("u")
e = l_n.count("e")

f_d = t + r + u + e

l = l_n.count("l")
o = l_n.count("o")
v = l_n.count("v")
e = l_n.count("e")

l_d = l + o + v + e

ls = int(str(f_d) + str(l_d))

if ls < 10 or ls > 90:
  print(f"Your score is {ls}, you go together like coke and mentos.")
elif ls > 40 and ls <= 50:
  print(f"Your score is {ls}, you are alright together.")
else:
  print(f"Your score is {ls}.")