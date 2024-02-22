#Matthew
def copyFile(inputFileName, outputFileName):
    """copies the original content of the input file to
    the output file."""
    # variables to open both the input and output files
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    line = inputFile.readline()
    # loop through the file and write each line read back to the outputfile
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
    #Test Code to wipe outputFile
    # open('outputFile.txt', 'w').close()
    copyFile(inputFile, outputFile)

if __name__ == "__main__":
    main()