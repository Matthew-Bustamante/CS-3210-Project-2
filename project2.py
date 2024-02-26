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

                # if for some reason the function name is not present we want to give the function a default name
                if functionName == "":
                    functionName = "defaultName"

                # if the parameters are missing commas we want to add them in
                if "," not in parameters:
                    parameters = re.sub(r"\s",", ", parameters)
                    
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
def printCounter():
    """Count the number of time the print keyword is used"""
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
    open('outputFile.txt', 'w').close()

    # copyFile()
    copyFile(inputFile, outputFile)
    functionFormater(inputFile, outputFile)

if __name__ == "__main__":
    main()