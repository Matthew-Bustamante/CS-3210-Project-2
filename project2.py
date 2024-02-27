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
    """check for the def keyword and check if the function 
    header is correct if not fix it"""
    inputFile = open(inputFileName, "r")
    # outputFile = open(outputFileName, "w")

    # loop through each line in the input file
    for line in inputFile:
        #defInString = re.findall(r"\A[def]", line)
        #whiteSpace = re.findall(r"\b\s", line)
        defInString = "def" in line or "def " in line

        # The correct form of a function header is a string that has 'def' followed by any string 
        # followed by a left parathesis followed by any string for parameters followed by a right parathesis and colon and a new line
        correctFormat = re.findall("def.+[(].+[)][:]\n", line)

        # if the key word def is found in the line we want to check that line because it could be a function header
        if defInString:
            # if the function header is in our correct form we will write that line to the output file
            # else we can assume its wrong and fix it
            if correctFormat:
                continue
            else:
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
                
                # if the function name is missing or the invalidFunctionName found and invalid character or sequence
                # we want change the name to valid name
                if functionName == "" or invalidFunctionName != None:
                    functionName = "defaultName"
                # -------------------------VALIDATING FUNCTION PARAMETERS-------------------------
                    
                # we want to check if the parameters are syntatically correct
                    
                # we don't want to add comas for one parameters so we're seeing how many parameters there are
                numberOfParams = re.findall(r"\w+", parameters)

                
                # if the commas are missing and there is more than one parameter then 
                # we want to add commas
                if "," not in parameters and len(numberOfParams) > 1:
                    # subsituting white space for commas
                    parameters = re.sub(r"\s",", ", parameters)
                    # getting rid of single commas that may exist
                    parameters = re.sub(r"\B,", "", parameters)
                    #parameters = re.sub(r"\A ", "", parameters)
                    #print (parameterlist)
                # if there is one parameter we want to check it for commas
                if len(numberOfParams) == 1:
                    # removing commas if they exist
                    parameters = re.sub(r"\,", "", parameters)
                else:
                    for index, value in enumerate(numberOfParams):
                        if ', ' not in value:
                            newValue  = value + ','
                            parameters = parameters.replace(value, newValue)
                        if index + 1 == len(numberOfParams):
                            parameters = re.sub(r",\Z", "", parameters)
                # if there are commas at the end: we want to get rid of them
                # we also don't want comas at the end of the parameters
                comasAtTheEndOfParams = re.search(r",\Z", parameters)
                if comasAtTheEndOfParams != None:
                    parameters = re.sub(r",\Z", "", parameters)
                
                # searching the parameters for special charaters which are invalid in Python
                specialCharactersInParams = re.search(r"[!@#$%^&*-+:;]", parameters)

                # if any special symbol is in the parameters we want to get rid of them
                if specialCharactersInParams != None:
                    parameters = re.sub(r"\@|\!|\@|\#|\$|\%|\^|\&|\*|\-|\+|\:|\;", "", parameters)
                # -------------------------------------FINAL STEP--------------------------------------

                # correcting the incorrect function to the correct format using the function name and parameters
                line = "def " + functionName +"(" + parameters + "):\n"
                print(line)
        else:
              continue
              #print(line)

# Haimei
def indentFormatter():
    """check if a colon is being used if so check he indent
    and if its wrong fix it"""
    pass

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
    inputFile = "defTest.txt"
    outputFile = "outputFile.txt"

    #Test Code to clear outputFile
    open('outputFile.txt', 'w').close()

    # copyFile()
    #copyFile(inputFile, outputFile)
    functionFormater(inputFile, outputFile)

    #count the number of times the print keyword is used in the output file
    print_count = printCounter(inputFile)
    print("The numebr of times key word print is used: ", print_count)

if __name__ == "__main__":
    main()