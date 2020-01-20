# REVERSE THE LIST (CONTENTS FROM FILE)


#file = open('test.txt')

#file.close()

#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt', 'r') as reader:      #opens a file and close once execution is complete. reader is object here
    content = reader.readlines()           #replacement for above two lines.
    #reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

