# accept a character and display whether it is upper case or lower case or not an alphabet.
#-------------------------------------------------------------------------------------------

ch=input("Enter a Character:")
if ch.isupper():
    print("{} is Upper case".format(ch))
elif ch.islower():
    print("{} is Lower case".format(ch))
else:
    print("{} is not an Alphabet".format(ch))