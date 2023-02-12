# open source file and assign contents to variable myfile
myfile = open('scrubbed_file.csv', 'r')

# set variables
myline = myfile.readline()
scroll = ("\t\tSTANDARDSCROLL_DOWN\n\t\tKEYBOARD_CURSOR_DOWN\n\tEnd of group\n")
keyboard_cursor_right = ("\t\tKEYBOARD_CURSOR_RIGHT\n\tEnd of group\n")
keyboard_cursor_left = ("\t\tKEYBOARD_CURSOR_LEFT\n\tEnd of group")
custom_ctrl_r = ("\t\tCUSTOM_CTRL_R\n\tEnd of group")
stairs = ("\t\tCUSTOM_C\n\t\tSTRING_A099\n\tEnd of group\n")
end_of_macro = ("End of macro")
new_line = ('\n')

# open new file for writing
newfile = open("converting_file.mak","w")

# cycle through the original file, then write to new file with convert contents
for myline in myfile:
    number_of_spaces = myline.count(',')
    data = myline.replace("d","\t\tSELECT\n\tEnd of group\n\t\tSELECT\n\tEnd of group\n").replace("#", "").replace("d,,d", "d,d").replace(",",keyboard_cursor_right)
    print(data + scroll, end = '')
    newfile.write(new_line + data + scroll)
    for num in range(number_of_spaces):
        print("\t\tKEYBOARD_CURSOR_LEFT\n\tEnd of group")
        newfile.writelines(new_line + keyboard_cursor_left)
myfile.close()

# add end of macro statements
print("\t\tCUSTOM_CTRL_R\n\tEnd of group")
print("End of macro")
newfile.write(new_line + custom_ctrl_r + new_line + end_of_macro)
newfile.close()

# opening and creating new .mac file
with open("converting_file.mak", 'r') as r, open('FINAL.mak', 'w') as o:
    for line in r:
        # strip() function
        if line.strip():
            o.write(line)



