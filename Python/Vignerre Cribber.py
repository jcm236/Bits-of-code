ALPH = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, keyword):
  if len(message) >= 0:
    
    for letter in message:
      keyword = keyword + keyword
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

message = input("enter message to check for cribs in: ")
keywords = input("enter potential keywords to check: ")
crib = input("enter crib to check for: ")
for keyword in keywords:
    for i in range(0, 6):
        temp = ""
        for ii in range(0, i):
            temp += "a"
        temp += crib
        temp2 = encrypt(temp, keyword)
        temp3 = temp2[i:len(temp2)]
        if temp3 in message.lower():
                print(keyword)
        else:
            print("CRIB NOT FOUND: "+"encrypted crib with keyword: "+keyword+". spacing (mimicking being in the middle of a message): "+str(i)+".")

