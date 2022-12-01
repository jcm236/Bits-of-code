from functions import *
while True:  #loop so the program never ends
  mode = input("would you like to encrypt (1) or decrypt (2)? ")
  if mode == "1" or mode == "encrypt":  #if user has asked for encrypting
    account = input("Are you setting up encryption to yourself (1) or encrypting with someones public keys (2)? ")
    if account == "1":
      values = get_p_q(
      )  #run function to ask user for P, Q, and E (all prime) for RSA encryption (Esentially 'setting up their RSA account')
      p = values[0]
      q = values[1]
      e = values[2]
      N = p * q  #Gets N for RSA encryption with e
    else:
      e = input("enter public encryption key 1 (e): ")
      N = input("enter public encryption key 2 (n): ")
    message = input("enter message ")
    str_q = input(
      "would you like you message to be in ascii char form (not recomended) or simply number form? (enter chr or num) "
    )
    #give the option to return the message in char form instead of number form. (Char form not recomended as it can return special chars like 'vertical tab' and stuff)
    if str_q == "chr":
      h = encrypt(message, e, N)
    else:
      h = encrypt(message, e, N, False)
      h = h.replace("§", " ")
    print("encrypted message: '" + h + "'.")
  else:
    if mode == "2": #if user has asked for decrypting
      message = input("enter message: ")
      d = input("enter private key: ")
      n = input("enter public key 2 (N): ")
      print(decrypt(message, int(d), int(n), False))
    else:
      print("invalid response")
