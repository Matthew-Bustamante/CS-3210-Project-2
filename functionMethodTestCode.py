import re

txt = "def "


# looking for characters d, e, f in the beginngin or end of string in case of white space in the beginning
defInString = re.findall(r"\b[def]", txt)
#looking for white space at the beginning of the line
whiteSpace = re.findall(r"\b\s", txt)

# this is suppose to be the correct format of the function header
correctFormat = re.findall("def.+\S[(].+[)][:]", txt)

# if a line contains d, e, f and has whitespace in the beginng we want to check it because it could be a function header
# else we can assume the line is not a function header and we would write this line to the output file
if defInString and whiteSpace:
    print("Yes, there is at least one match!")
  # we want to check if the line that has the function header is in the correct format we defined above if so we will write this line to the output file
    if correctFormat:
        print("Correct")
    # else we want to fix it and write the corrected version to the output file
    else:
         print("incorrect")
  
  
         # variables that contain the indexes of the first parathesis
         parathesisOne = re.search(r"\(", txt)

         # if for some reason the first parathesis is not persent then we want to add it 
         # else give us the index of the first parathesis
         if parathesisOne == None:
             txt = re.sub("\s" , " (", txt, 1)
             parathesisOne = re.search(r"\(", txt).span()
         else: parathesisOne = parathesisOne.span()

         # if for some reason the second parathesis is not found then we an to add it at the end of the string
         # else give us the index of the second parathesis
         parathesisTwo = re.search(r"\)|\:|\s\Z", txt)
         if parathesisTwo == None:
             txt += ")"
             parathesisTwo = re.search(r"\)|\:|\s\Z", txt).span()
         else:
             parathesisTwo = parathesisTwo.span()
        # looking for whitespace in before the parathesis for the name
         whiteSpaceInFunc = re.search(r"\s\(|\(", txt).span()
        # looking for d e or f followed by whitespace for the name
         defInFunc = re.search(r"[def]\s", txt).span()
         
         # using the location of the first and second parathesis we can assume the parameters are between them
         parameters = txt[parathesisOne[1]:parathesisTwo[0]]
         # using the location of the def and the first parathesis we can assume the name is between them
         functionName = txt[defInFunc[1]:whiteSpaceInFunc[0]]

         # if for some reason the name is an empty string we want to give a default name
         if functionName == "":
             functionName = "default"
         # correcting our the incorrect function header to the correct format
         # using the name and parameters gathered from the string
         txt = "def " + functionName + "(" + parameters + "):"
         print(txt)

else:
    print("No match")
