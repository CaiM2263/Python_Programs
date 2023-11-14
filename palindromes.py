#A program that determines if a string or an integer is a palindrome
def palin_check(str1):
  str1=str1.replace(" ", "")
  str1=str1.replace(" ","")
  str1=str1.replace(",","")
  str1=str1.replace(":","")
  str1=str1.lower()
  first=str1
  str1=str1[::-1]
  if str1==first:
    print("This is a palindrome.")
  else:
    print("This is not a palindrome.")

palin_check("race a car")


def palin_check2(int1):
  first=int1
  if int1<0:
    print("This is not a palindrome.")
    return int1
  else:
    int1=str(int1)
    int1=int1[::-1]
    int1=int(int1)
    if int1==first:
      print("This is a palindrome.")
    else:
      print("This is not a palindrome.")
palin_check2(121)
