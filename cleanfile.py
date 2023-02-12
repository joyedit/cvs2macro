# open source file and assign contents to variable myfile
myfile = open('The_Saracen_Windmill_Workshops.csv', 'r')

# set variables
myline = myfile.readline()
new_line = ('\n')

# open new file for writing
newfile = open("scrubbed_file.csv","w")

# cycle through the original file, then write to new file with convert contents
for myline in myfile:
    data = myline.replace(" ","").replace("#","").replace("b",",,").replace("f",",,").replace("h",",,").replace("l",",,").replace("`","").replace(", ,", ",,").replace("r", "d").replace("+", "").replace('"', '').replace("#>", "").replace("j", "").replace(">", "").replace("x", "").replace("i","")
    print(data)
    newfile.write(data)

myfile.close()