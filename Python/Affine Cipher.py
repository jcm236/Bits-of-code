import enchant

dict = enchant.Dict("en_GB")

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decrypt(keyA, keyB, message):
    decrypted_message = ""
    for letter in message:
        if letter in ALPH:
            ii = 0
            for i in range(0, 26):
                if (((keyA * i) - 1) / 26) == int((((keyA * i) - 1) / 26)):
                    ii = i
                    break
            decrypted_ltr = i * (ALPH.index(letter) - keyB) % 26
            decrypted_message += ALPH[decrypted_ltr]
        else:
            decrypted_message += letter
    return decrypted_message


validwords = []
message = input("enter message ")
for keya in range(0, 26):
    for keyb in range(0, 26):
        validwords = 0
        h = decrypt(keya, keyb, message)
        #print("keya: "+str(keya)+". keyb: "+str(keyb)+". message: "+h)
        words = h.split(" ")
        for word in words:
            if len(word) >= 3:
                if dict.check(word) == True:
                    #validwords.append(word+". key 1: "+str(keya)+". key 2: "+str(keyb)+".")
                    #print("key 1: "+str(keya)+". key 2: "+str(keyb)+"."+"found word: "+word+". Message: "+str(words))
                    validwords += 1
                    if validwords >= (len(words) / 2):
                        print("key 1: " + str(keya) + ". key 2: " + str(keyb) +
                              "." + "found word: " + word + ". Decrypted Message: " +
                              str(words))
                    else:
                        continue
            else:
                continue
