# accept a character and display whether it is upper case or lower case or not an alphabet.
#-------------------------------------------------------------------------------------------

ch=input("enter a character:")
if ch.isupper():
    print("{} is upper case".format(ch))
elif ch.islower():
    print("{} is lower case".format(ch))
else:
    print("{} is not an alphabit".format(ch))