import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Example
addToClipBoard('nickolastomi@gmail.com')
