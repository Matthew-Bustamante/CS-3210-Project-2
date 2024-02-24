import re

txt = "def myFunc(self):"


# looking for characters d, e, f in the beginngin or end of string in case of white space in the beginning
defInString = re.findall(r"\b[def]", txt)

#looking for white space at the beginning of the line
whiteSpace = re.findall(r"\b\s", txt)

# this is suppose to be the correct format of the function header
correctFormat = re.findall("def.+[(].+[)][:]", txt)

#if a line contains d, e, f and has whitespace in the beginng we want to check it because it has to be a function header
if defInString and whiteSpace:
    print("Yes, there is at least one match!")
  # we want to check if the line has the correct function header if so its correct and we can move on
    if correctFormat:
        print("Correct")
    # else we want to split the string and fix it
    else:
         print("incorrect")
  
  
         splitString = re.split("\s", txt, maxsplit=1)
         print(splitString)

# if a line doesn't contain d,e,f or whitespace in the beginning its not a function header
else:
    print("No match")
