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
def functionFormater():
    """check for the def keyword and check if the function 
    header is correct if not fix it"""
    pass

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
    # copyFile(inputFile, outputFile)

    #count the number of times the print keyword is used in the output file
    print_count = printCounter(inputFile)
    print("The numebr of times key word print is used: ", print_count)

    # indentFormatter()
    indentFormatter(inputFile, outputFile)

if __name__ == "__main__":
    main()
