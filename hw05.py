"""
Name: Loke
Peers: None
References: None
"""

def get_letter():
    """
       The users are asked to input an upper case letter from A,B and C, checking if this input is correct.
       If it is not correct, print that "Error: You provided the wrong character." and ask again.
       If the user input more than one letter, print that "Error: You provided the wrong character." and ask again.
    """

    Correct_input = ["A", "B", "C"]
    while True:
        letter = input("Give an single uppercase letter:")
        
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        
        elif letter not in Correct_input:
            print("Error: You provided the wrong character.")
            continue
        # remove the default return and add your code
        else:
            return letter
        
        


def get_digit():
    """ 
       The users are asked to input an digit from 1 to 3, checking if this input is correct.
       If the provided text is not composed of only digits, print that "Error: your input should be only digits."
       If it is not correct, print that "Error: digit needs to be in [1,3]."
    """
    # remove the default return and add your code
    while True:
        num = input("Give an single number character: ")
        
        if not num.isdigit():
            print("Error: your input should be only digits.")
            continue
        
        elif num not in ["1", "2", "3"]:
            print("Error: a single digit needs to be in [1,3].")
            continue
        # remove the default return and add your code
        else:
            return num
    

def check_pattern(letter, digit, lst):
    """
    Checks if any of the words inside the list contain
    the letter and number in that order,
    and prints any that do contain them.
    """

    print("Strings with the pattern:")

    for word in lst:
        for i in range(len(word)):
            if word[i] == letter:
                if digit in word[i + 1:]:
                    print(word, end=" ")
                    break
    print()



#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
        letter = get_letter()
        digit = get_digit()

        check_pattern(letter, digit, st_list)

        answer = input("Try Again? (y/n): ")

        if answer == "y":
            continue
        else:
            break

    print("The End")
    
    
    
    

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()