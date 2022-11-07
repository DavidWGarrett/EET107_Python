#File demo

#OBJECT AND VARIABLE DIFFERENT

out_file = open('dudefilestring.txt', mode='w')
#mode='w' is write, r is read

out_file.write('FIRST TEXT OUTPUT')
#.write sends info to file)
out_file.write('SWEET')

#IMPORTANT close file when done - avoids corrupt file
out_file.close()

#mode='w' wipes out existing files, watch out!

