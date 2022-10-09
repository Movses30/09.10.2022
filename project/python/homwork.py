

import re

def frst_lettr_upper(a):
    
    if not isinstance(a, str):
      raise ValueError("Pleas enter text only in string")
    if re.findall("\A[A-Z]", a):
      if  not re.search("[0-9]",a):
        return True      
    raise Exception ("starts with a capital letter and the rest of the letters consists only of lowercase letters")


def this_string_is_sentence(d):
  #d = "Momdcv cvcce .."
  if not isinstance(d, str):
    raise TypeError("Pleas enter text only in string")
  if re.findall("\A[A-Z]", d)  and re.findall("[.]\Z", d) :
    if re.findall("[\.]", d)!= ["."]:
      raise Exception ("print onli one  dis simbul write -->>(.)")
    else:
      return True
  else:
    raise Exception ("the sentence must begin with a capital letter")
#print(this_string_is_sentence())


def natural_number(nu):
  #nu = "k20"
  if isinstance(nu, int):
    raise TypeError("Pleas enter text only in string")
  if re.search(" ",nu):
    raise Exception ("A natural number cannot contain spaces")
  if re.findall("[-]", nu[0]) or re.findall("[0]", nu[0]) :
    raise Exception ("only pozitive numbr")
  if re.findall("\A[1-9]", nu): 
     return True
  raise Exception ("string is not is number")
  
