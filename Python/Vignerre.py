ALPH = "abcdefghijklmnopqrstuvwxyz"


def decrypt(message, keyword):
  message = message.lower()
  if len(message) >= 0:
    
    while True:
      if len(keyword) >= len(message):
        break
      else:
        keyword += keyword
    result = ""
    lettercount = -1
    for letter in message:
      if letter in ALPH:
        lettercount = lettercount + 1
        key = ALPH.find(keyword[lettercount])
        letter_index = (ALPH.find(letter) - key) % len(ALPH)
        result = result + ALPH[int(letter_index)]
      else:
        result = result + letter
  return result


def encrypt(message, keyword):
  if len(message) >= 0:
    
    while True:
      if len(keyword) >= len(message):
        break
      else:
        keyword += keyword
    result = ""
    lettercount = -1
    for letter in message:
      if letter in ALPH:
        lettercount = lettercount + 1
        key = ALPH.find(keyword[lettercount])
        letter_index = (ALPH.find(letter) + key) % len(ALPH)
        result = result + ALPH[int(letter_index)]
      else:
        result = result + letter
  return result


def start():
  mode = input("encrypt (1) or decrypt (2)? ")
  if mode == "1":
    keyword = input("enter keyword for encrypting ")
    keyword.replace(" ", "")
    message = input("enter message to encrypt ")
    print("encrypted "+message+" with keyword "+keyword+"."+" Encrypted text: "+encrypt(message, keyword))
    input("enter anything to continue ")
    start()
  else:
    if mode == "2":
      keyword = input("enter keyword for decrypting ")
      keyword.replace(" ","")
      message = input("enter message to decrypt ")
      print("decrypted "+message+" with keyword "+keyword+"."+" Decrypted text: "+decrypt(message, keyword))
      input("enter anything to continue ")
      start()
    else:
      print("invalid input, please enter 1 or 2")
      input("enter anything to continue ")
      start()
