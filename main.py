print("Welcome to Python Play, an almost totally useless program (from the users point of view)...")

def getUserName():
  username = input("What's your name?\n")
  if username == "":
    username = input("No but really, TELL ME your name!\n")
  print("Hi " + username + ", great to meet you!")
  return username

username = getUserName()
print("Your username is " + str(len(username)) + " characters")
print("Your username is {} characters".format(len(username)))