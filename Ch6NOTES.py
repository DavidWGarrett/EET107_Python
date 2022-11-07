#File demo

#OBJECT AND VARIABLE DIFFERENT

def write_demo():
    out_file = open('ch6notes.txt', mode='w')
    #mode='w' is write, r is read

    out_file.write('FIRST TEXT OUTPUT\n')
    #.write sends info to file)
    out_file.write('SWEET')

    #IMPORTANT close file when done - avoids corrupt file
    out_file.close()

#mode='w' wipes out existing files, watch out!
#out_file write needs \n for new lines

def append_demo():
    for i in range(6):
        out_file = open('ch6notes.txt', mode='a')
        out_file.write('text appended\n')
        out_file.write('SWEET') # If you don't write \n, cursor stops after sweet

def read_demo():
    in_file = open('ch6notes.txt', mode='r') # read mode
    print('first line')
    line1 = in_file.readline()
    print(line1)
    print('second line')
    line2 = in_file.readline()
    print(line2)
    strings = in_file.read() # data taken in needs to go somewhere, sequential file access, take info from beginning to end
    # .read will read from the current position, not beginning. Code was at line 3
    in_file.close()
    print(strings)

#If you don't specify file path, it'll assume relative path (which is same folder as .py

def full_path():
    in_file = open(r'C:\Users\David\Documents\notes.txt', mode='r') # (put r before string means raw string, no control characters)
    buffer = in_file.read()
    in_file.close()
    print(buffer)

def read_line_demo():
    #READ AND PROCESS LINES LINE BY LINE
    #commonly use while loop line by line, not python
    in_file = open('ch6notes.txt', 'r') # DON'T NEED TO WRITE MODE
    for line in in_file:
        print(line.rstrip('\n'))  #Print line character does \n automatically, it make text double spaced
    in_file.close() #rstrip is for strings, can strip off the \n







