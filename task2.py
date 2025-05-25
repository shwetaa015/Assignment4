file=open("output.txt","w")
text=input("Enter text to write to file:")
file.write(text + "\n")
print("Data successfully written to ouput.txt.")

file=open("output.txt","a")
add_text=input("Enter additional text to append:")
file.write(add_text+ "\n")
print("Data successfully appended.")

file=open("output.txt","r")
print("\n Final content of output.txt:")
print(file.read())