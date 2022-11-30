
import random
import time
import enchant
result = ""


def restart():
    print("\nRestarting...")
    time.sleep(1)
    print("\n\n\n")
    start()

def prestart():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("PLEASE NOTE:\n")
    print("This code will not work with names!")
    time.sleep(3)
    print("This code will also fail at decoding encryped messages with invalid words, like typos, slang, acronyms or just gibberish.")
    time.sleep(3)
    print("This code also can fail if the message has only one word, it can still work BUT it is less likely to.")
    time.sleep(3)
    print("\nLoading up...")
    time.sleep(1)
    print("Done")
    time.sleep(0.1)
    print("Starting now\n")

      
def start():
    global result
    #global prestart
    #prestart()
    #chkr = enchant.SpellChecker("en_GB")
    dict = enchant.Dict("en_GB")

    def encrypt(key, message):
        global result
        message = message.upper()
        #global message2
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) + key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter

        

    def decrypt(key, message):
        message = message.upper()
        #global result
        global result3
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter
        return result



    answer = input("Do you want to encrypt (1) or decrypt (2) (enter 1 or 2): ")
    if answer == "1":
        message = input("What message would you like to encrypt? ")
        answer2 = input("Would you like to use a certain key, or random? (random/certain) ")
        if answer2 == "random":
            print("generating random...")
            key2 = random.randint(1, 25)
            time.sleep(1)
            encrypt(key2, message)
            encr_words = result.split()
            for x in encr_words:
                result = decrypt(key2, x)
                result = removesym(result)
                if dict.check(result) == True:
                    continue
                else:
                    result = decrypt(key2, x)
                    xx = result
                    #print("WARNING! Invalid word at: '"+xx+"', if more than half of the words are invalid decryption may fail!")
                    #input("enter anything to continue ")
                    #restart()
            encrypt(key2, message)
            print("\nEncrypted message: '"+result+"' with random key: "+str(key2))
            endmaybe = input("enter anything to continue ")
            restart()
        else:
            if answer2 == "certain":
                answer3 = input("What key would you like to use? (enter a number between 1 and 25) ")
                try:
                    answer3 = int(answer3)
                except:
                    print("\nInvalid key, please enter a number between 1 and 25. (restarting)\n")
                    time.sleep(0.5)
                    start()
                print("Using key...\n")
                time.sleep(1)
                encrypt(answer3, message)
                print("Encrypted message: '"+result+"' with specified key "+str(answer3)+"\n")
                endmaybe = input("enter anything to continue ")
                restart()
                
                
            else:
                print("\nInvalid response, please enter random or certain. (restarting)\n")
                time.sleep(0.5)
                start()
            
    else:
        if answer == "2":
            message2 = input("What message would you like to decrypt? ")
            answer4 = input("Do you know the key, or want to try all? (know/all) ")
            if answer4 == "know":
                answer5 = input("What key would you like to use? ")
                try:
                    answer5 = int(answer5)
                except:
                    print("\nInvalid key, please enter a number between 1 and 26. (restarting)\n")
                    time.sleep(0.5)
                    start()
                print("Using key...")
                time.sleep(1)
                result = decrypt(answer5, message2)
                print("\nDecoded message: '"+result+"' with specified cipher "+str(answer5)+"\n")
                endmaybe = input("enter anything to continue ")
                restart()
            
            else:
                if answer4 == "all":
                    print("Warning: If more than 50% of the messages words are invalid (typos, names, unofficial words, acrynomys) the decrypting may fail.")
                    time.sleep(0.5)
                    print("trying all...")
                    time.sleep(1)
                    key3 = 0

                    for x in range(0, 26):
                        amount = 0
                        truewords = 0
                        key3 = key3 + 1
                        result = decrypt(key3, message2)
                        result2 = result.split(" ")
                        if amount == len(result2):
                            break
                        else:
                            for word in result2:
                                word = removesym(word)
                                #try:
                                if dict.check(word) == True:
                                    truewords = truewords + 1
                                    amount = amount + 1
                                    if amount == len(result2):
                                        print("\nDecoded message '"+result.lower()+"' with cipher "+str(x+1)+"\n")
                                        endmaybe = input("enter anything to continue ")
                                        restart()
                                        break
                                    if truewords >= round(len(result2) / 2):
                                        print("\nDecoded message '"+result.lower()+"' with cipher "+str(x+1)+"\n")
                                        endmaybe = input("enter anything to continue ")
                                        restart()
                                        break
                                    continue
                                else:
                                    if truewords >= round(len(result2) / 2):
                                        print("\nDecoded message '"+result.lower()+"' with cipher "+str(x+1)+"\n")
                                        endmaybe = input("enter anything to continue ")
                                        restart()
                                        break
                                    continue
        
                                        
                    print("Message failed to decrypt. Restarting... (Message invalid)")
                    time.sleep(1)
                    print("")
                    start()
                                    
                else:
                    print("\nInvalid response, please enter know or all. (restarting)\n")
                    time.sleep(0.5)
                    start()
                                
                        #else:
                            #print("next key")
                            #key3 = key3 + 1
                    #print(result)
                    #key3 = key3 + 1

        else:
            print("\nInvalid response, please enter 1 or 2. (restarting)\n")
            time.sleep(0.5)
            start()

    #message = input("enter message ")
    #message = message.upper()
    #message2 = message
            

def removesym(word):
    symbols = ["!", "?", ".", ":", ";", "'", "%", "&", "*", "£", "@", "#", "~", "(", ")", "$", ",", ">", "<","/","+","-","_","=","`","¬","¦","[","]","{","}","'","^",'"']
    for sym in symbols:
      word = word.replace(sym, "")
    return word


#prestart()
start()



