def divide_numbers():
    # user input
    numerator = float (input("enter the numerator"))
    denominator = float (input("enter the denominator"))
    # division
    
    result = numerator / denominator
    
    print("the result is ", result)
    except ValueError:
    print("Error: You must enter a number")
    except ZeroDivisionError:
print("Error: You cannot divide by zero")






