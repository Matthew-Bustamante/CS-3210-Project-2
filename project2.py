#Matthew
import re
def copyFile(inputFileName, outputFileName):
    """copies the original content of the input file to
    the output file.

    Parameters:
    - inputFileName (String): name of the inputFile
    - outputFileName (String): name of the outputFile
    """
    # variables to open both the input and output files
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    line = inputFile.readline()
    outputFile.write(line)
    # loop through the file and write each line that is read to the output file
    for line in inputFile:
        outputFile.write(line)

    # closing both files
    inputFile.close()
    outputFile.close()
    

#Matthew
def functionFormater(inputFileName, outputFileName):
    """ This function checks the input file for function headers. If one is found 
     the method will attempt to fix the header if its correct or not in order to cover as many 
      cases as possible. """
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    # outputFile = open(outputFileName, "w")

    # loop through each line in the input file
    for line in inputFile:
        # looking of the keyword def
        defInString = "def" in line or "def " in line

        # looking for a # or a '''
        nonFunctionCharacters = re.search(r"\A#|\A'''", line)

        # if the key word def is present and there are no # or ''' in the beginning
        # we can assume this line is a function header
        if defInString and nonFunctionCharacters == None:
            #-----------ISOLATION FUNCTION NAME & FUNCTION PARAMETERS---------------
            # The function name is usually between the def keyword and the left parathesis.
            # Likewise the function parameters are between the left and right parathesis.
            # By grabbing the indexes of these parts we can accurately isolate the function name and parameters
            # however since we're using this as a guideline if any of these parts are missing we want to add them to the string


            # this is looking for the left parathesis
            leftParathesis = re.search(r"\(", line)

            # if for some reason the left parathesis can't be found or has no index we want to add it in
            # else using the regex span() function we want to get the index of the left parathesis
            if leftParathesis == None:

                # this is saying to subsitute whitespace with a left Parathesis and only do it once
                line = re.sub("\s", " (", line, 1)
                leftParathesis = re.search(r"\(", line).span()
            else:
                leftParathesis = leftParathesis.span()
            
            # this is searching for a right parathesis or a colon or an empty space at the end of the string
            rightParathesis = re.search(r"\)|\:|\s\Z", line)

            # if for some reason the search above can't find anything then we want to add a right parathesis
            # else we want to get the index of the that right parathesis using the regex function span()
            if rightParathesis == None:
                line += ")"
                rightParathesis = re.search(r"\)|\:|\s\Z", line).span()
            else:
                rightParathesis = re.search(r"\)|\:|\s\Z", line).span()

            # this is searching for whitespace in the begining or the the left parathesis
            whiteSpaceInFunc = re.search(r"\s\(|\(", line).span()

            # this is looking for d, e, or f followed by white space in the string 
            defInFunc = re.search(r"[def]\s", line)

            # if for some reason the defInFunc can't find anything because there's no white space after 'def' we want to add it
            # else give us the index of the whitespace using regex's function span()
            if defInFunc == None:
                line = line.replace("def", "def ")
                defInFunc = defInFunc = re.search(r"[def]\s", line).span()
            else: defInFunc = defInFunc = re.search(r"[def]\s", line).span()

            # the span() methods used above returns tuples that contain indexes
            # so by using these indexes we can assume the parameters are between the left and right parathesis
            parameters = line[leftParathesis[1]:rightParathesis[0]]
            
            # by using the indexes of the whitespace after 'def' and the left parathesis or lack there of
            # we can assume the name is between these two indexes
            functionName = line[defInFunc[1]:whiteSpaceInFunc[0]]

            # --------------------------VALIDATING FUNCTION NAME------------------------------

            # special characters, numbers at the beginning and a function named def are invalid function names in python
            # this variable searches for all of these cases and will return an object if one is found
            invalidFunctionName = re.search(r"[!@#$%^&*-+:;,]|\d|\Adef", functionName)
            
            # if the function name is missing or the invalid Function Name is found
            # we want change the name to valid name
            if functionName == "" or invalidFunctionName != None:
                functionName = "defaultName"
            # -------------------------VALIDATING FUNCTION PARAMETERS-------------------------
                
            # we want to check if the parameters are syntatically correct
                
            # here we're looking gathering all of the words between the parathesis and storing them into an array
            numberOfParams = re.findall(r"\w+", parameters)
            
            # if one parameter exists we want to check if its valid
            # else we can assume that there are more than one parameters present
            if len(numberOfParams) == 1:
                # checking for the key word def and removing it if present
                parameters = re.sub(r"\bdef", "", parameters)

                #checking for any commas and removing them if present
                parameters = re.sub(r"\,", "", parameters)

                #checking for any special characters if present and removing them
                parameters = re.sub(r"\@|\!|\@|\#|\$|\%|\^|\&|\*|\-|\+|\:|\;", "", parameters)
                #checking for numbers in the beginining or middle of the strin and removing them
                parameters = re.sub(r"\b\d|\d\B", "", parameters)
                
            else:
                # checking for numbers in the beginning and removing them
                parameters = re.sub(r"\b\d|\d\B", "", parameters)
                # checking for special characters and removing them if present
                parameters = re.sub(r"\@|\!|\@|\#|\$|\%|\^|\&|\*|\-|\+|\:|\;", "", parameters)
                # checking if the key word def is present if so we want to delete it
                parameters = re.sub(r"\bdef", "", parameters)
                # reseting the array to corrected form
                numberOfParams = re.findall(r"\w+", parameters)
                
                # number to keep track of the number of params
                paramNumber = 0

                #checking for duplicating parameters
                for index, name in enumerate(numberOfParams):
                    
                    duplication = 0
                    for nameComparison in numberOfParams:
                        if name == nameComparison:
                            paramNumber += 1
                            duplication += 1
                        # a duplicate is found
                        if duplication > 1:
                            newParameter = numberOfParams[index] + str(paramNumber)
                            numberOfParams[index] = newParameter
                            # parameters = parameters.replace(name, newParameter, 1)
                            parameters = ' '.join(numberOfParams)
                            break
                
                
                # resetting the array
                numberOfParams = re.findall(r"\w+", parameters)

                #transforming the array into a string
                parameters = ' '.join(numberOfParams)

                # replacing the white space in the string with commas
                parameters = re.sub(r"\s", ", ", parameters)
                

            # if there are commas at the end: we want to get rid of them
            parameters = re.sub(r",\Z", "", parameters)
            
            # -------------------------------------FINAL STEP--------------------------------------

            # correcting the incorrect function to the correct format using the function name and parameters
            line = "def " + functionName +"(" + parameters + "):\n"
            outputFile.write(line)
              #print(line)
        else:
            outputFile.write(line)
# Haimei
def indentFormatter(inputFileName, outputFileName):
    """
    check if a colon is being used if so check he indent
    and if its wrong fix it
    Assume a line starts with multi spaces or tabs
    If the space number is larger 3 than a multiple of 4, we assume it is caused by typo of a 4-space
    """
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    indentLevel = 0
    indentSpaceNum = 4
    forceIndent = False
    for line in inputFile:
        if re.match(r"^(?:[\s\t]*\r?\n|[\s\t]*#.*)$", line):
            outputFile.write(line)
            continue
        # check if the line is indented correctly, i.e., check if the line starts with the correct number of spaces accurately
        if forceIndent:
            forceIndent = False
            if re.match(r"^[\ ]*", line).end() != indentLevel * indentSpaceNum or re.match(r"^[\t]*", line).end() != indentLevel:
                line = " " * (indentLevel * indentSpaceNum) + line.lstrip()
        else:
            if line[0] == " ":
                # If the space number is larger 3 than a multiple of 4, we assume it is caused by typo of a 4-space
                currIndentLevel = (re.match(r"^[\ ]*", line).end() + 1 ) // indentSpaceNum
            elif line[0] == "\t":
                currIndentLevel = re.match(r"^[\t]*", line).end()
            else:
                currIndentLevel = 0
            if currIndentLevel < indentLevel:
                indentLevel = currIndentLevel
            line = " " * (indentLevel * indentSpaceNum) + line.lstrip()

        # check if the line ends with a colon
        if line.rstrip().endswith(":"):
            indentLevel += 1
            forceIndent = True
        outputFile.write(line)

    # close the files
    inputFile.close()
    outputFile.close()

# Christina
def printCounter(outputFileName):
    """Count the number of time the print keyword is used

    Parameters:
    outputFileName (String) : name of the output 
    """
    # Open the output file for reading
    with open(outputFileName, "r") as outputFile:
        file_content =outputFile.read()
        #using regular expresssion to find all the occurance of the print() method
        #making sure not to count the 'print' word in the string
        print_count = len(re.findall(r'\bprint\s*\(', file_content))
        # return the number of times of print method occured
        return print_count
    pass
# Haimei
def outputFile():
    """Output The New File to the output file"""
    pass

def main():
    """Main Function"""
    #variables to keep track of the input and output file names
    inputFile = "testPythonFile.txt"
    outputFile = "outputFile.txt"

    #Test Code to clear outputFile
    # no need if we are using the w mode to open the file
    # open('outputFile.txt', 'w').close()

    # copyFile()

    #copyFile(inputFile, outputFile)
    functionFormater(inputFile, outputFile)

    # copyFile(inputFile, outputFile)


    #count the number of times the print keyword is used in the output file
    print_count = printCounter(inputFile)
    print("The numebr of times key word print is used: ", print_count)

    # indentFormatter()
    indentFormatter(inputFile, outputFile)

if __name__ == "__main__":
    main()
