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
    inputFile = "testPythonFile.txt"
    outputFile = "outputFile.txt"

    #Test Code to clear outputFile
    open('outputFile.txt', 'w').close()

    # copyFile()
    copyFile(inputFile, outputFile)

    #count the number of times the print keyword is used in the output file
    print_count = printCounter(inputFile)
    print("The numebr of times key word print is used: ", print_count)

if __name__ == "__main__":
    main()