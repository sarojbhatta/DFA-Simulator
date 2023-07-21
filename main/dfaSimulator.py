import os

#request user to enter the input file. The valid filename if dfa.txt
file_name=input("Enter the name of the input file - dfa.txt: ")
if os.path.exists(file_name):

    # open the given file and read all lines. Once read, add it to a list read_file. Further, strip all elements of read_file list by a whitespace and keep the transitions in a 2-D list.
    with open(file_name) as file:
        file=file.readlines()
        
        read_file=[]
        for i in file:
            read_file.append(i.strip("\n"))
        #print("read: \n", read_file)
        cleaned_list=[]
        for i in read_file:
            cleaned_list.append(i.split(" "))
        #print ("cleanedlist: \n", cleaned_list) 
        final_state=cleaned_list[0][0]
        start_state=cleaned_list[0][0]
    
    # Open the output file named output.txt to write the given string and accepted/rejected state once the program is run.
    output_filename="output.txt"
    output_file=open(output_filename,"w+")
    user_input=input("Enter the string to test:")
    #output_file.write(user_input+ ":")
    
    # Ask for input string to test and as long as it is not "quit." continue the loop
    while user_input.lower() !='quit.':
        output_file.write("\n\n"+user_input)
        user_input=list(user_input)
        
        current_state=cleaned_list[0][0]
        
        isAccepted=True

        # For every alphabet in the given string
        for i in range(0,len(user_input)):
            
            isValidInput = False 

            # For every transition fuction 
            for j in range(1, len(cleaned_list)):

                # if the current state is available as start of the transition function and the current alphabet is available in that particular transition function, move the current state to the output state of the transition function.
                if current_state==cleaned_list[j][0] and user_input[i]==cleaned_list[j][1]:
                    print(current_state+" --"+ user_input[i] + "--> " + cleaned_list[j][2])
                    current_state=cleaned_list[j][2]
                    isValidInput = True
                    break
            
            # check if the input is valid. If no, output - invalid
            if isValidInput == False:
                print("invalid string input")
                output_file.write("\ninvalid string input")
                isAccepted=False
                break
        
        # Check if the program reached the final state after going through the given string and if the string is accepted, output- accepted. Write the corresponding accepted/rejected state for the string in the output file.
        if current_state==final_state and isAccepted==True:
            print("accepted")
            output_file.write("\naccepted")
        else:
            print("rejected")
            output_file.write("\nrejected")
        user_input=input("Enter a sting to test or Enter 'quit.' to exit: ")
    
    # Close the output file
    output_file.close()

# If the given filename is not found, ask the user to enter the correct filename.
else: 
    print("No such file found. Please enter a correct filename (dfa.txt) after you restart the program!")

# END of the Program