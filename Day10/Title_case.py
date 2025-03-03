# Function to format the first and last name properly  
def format_name(f_name, l_name):  
    # Check if either input is empty  
    if f_name == "" or l_name == "":  
        return "You Did Not Give An Input"  
    
    # Convert the first letter of each name to uppercase  
    formated_f_name = f_name.title()  
    formated_l_name = l_name.title()  
    
    # Return the formatted full name  
    return f"{formated_f_name} {formated_l_name}"  

# Get user input and print the formatted name  
print(format_name(input("What's your first name? "), input("What's your last name? ")))  
