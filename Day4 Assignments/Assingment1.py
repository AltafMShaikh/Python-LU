file1 = open("myfile.txt", "w") 
L = ["I Love LetsUpgrade"] 
file1.writelines(L) 
file1.close() 

# append mode 
file1 = open("myfile.txt", "a") 

file1.write("Forever") 
file1.write("\tbeacuse they deserve it.") 


file1 = open("myfile.txt", "r") 
print(file1.read()) 
print() 
file1.close() 
