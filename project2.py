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
    outputFile = open(outputFileName, "w")

    for line in inputFile:
        defInString = re.findall(r"\b[def]", line)
        whiteSpace = re.findalll(r"\b\s", line)
        correctFormat = re.findall("def.+[(].+[)][:]", line)

        if defInString and whiteSpace:
            if correctFormat:
                continue
            else:
                

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

if __name__ == "__main__":
    main()