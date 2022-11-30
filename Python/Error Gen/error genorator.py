import colorama
from colorama import Fore

def geterror(id):
  erroredit = ""
  errorfile = open("Error.txt", "r")
  errors = errorfile.readlines()
  errr = ""
  error = ""
  xx = -1
  for err in errors:
    x = 0  
    errr = ""
    for letter in err:   
      if x < 3:
        errr = errr + letter
      x = x + 1
    xx = xx +1
    if int(errr) == id:
      error = errors[xx]
  x = 0
  for letter in error:
    if letter != ":":
      if x > 2:
        erroredit = erroredit + letter
      x = x + 1
  return Fore.RED+erroredit

      
def adderror(id, erroradd, overwrite=False):
  def yn ():
    overwritein = input("There is already an error with this id, do you want to overwrite it? (y/n)")
    if overwritein == "y":
      return True
    else:
      if overwritein == "n":
        return False
      else:
        print("Invalid response")
        yn()


  def writetoline(write, line):
    fileR = open("Error.txt", "r")
    filelines = fileR.readlines()
    filelines[line] = write+"\n"
    fileW = open("Error.txt", "w")
    fileW.writelines(filelines)
    
        
    
  errorfileread = open("Error.txt", "r")
  errors = errorfileread.readlines()
  errorfileadd = open("Error.txt", "a")
  errorcount = -1
  sameid = False
  for error in errors:
    ltrcount = 0
    currenterrorid = ""
    for letter in error:
      if ltrcount < 3:
        currenterrorid = currenterrorid + letter
      ltrcount = ltrcount + 1
    errorcount = errorcount + 1
    if int(currenterrorid) == id:
      sameid = True
      h = ""
      h = str(id)+":"+str(erroradd)+"\n"
      #nnoice
      if overwrite == False:
        
        overwriteyn = yn()
        if overwriteyn == True:

          writetoline(h, int(errorcount))
        else:
          if overwriteyn == False:
            print("cancelling")
      else:
          writetoline(h, int(errorcount))
  if sameid == False:
    h = ""
    h = str(id)+":"+str(erroradd)+"\n"
    errorfileadd.write(h)



#print(Fore.RED + 'This text is red in color')
    
print(Fore.RED+"Some example errors:\n")
error = 404
h = geterror(error)
print(Fore.RED+"    Error "+str(error)+", "+h)
hh = geterror(401)
print(Fore.RED+"    Error "+str(401)+", "+hh)
hhh = geterror(502)
print(Fore.RED+"    Error "+str(502)+", "+hhh)
hhhh = geterror(503)
print(Fore.RED+"    Error "+str(503)+", "+hhhh)
hhhhh = geterror(314)
print(Fore.RED+"    Error "+str(314)+", "+hhhhh)
hhhhhh = geterror(000)
print(Fore.RED+"    Error 000"+", "+hhhhhh)
#adderror(id, "error details")

