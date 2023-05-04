day = int(input("Enter a day of the month: ")) # Taking input from the user

if day % 2 != 0:    # if - else loop is perfect to find out odd and even
    print("It's an odd day. Don't Go Outside.")
else:
    print("It's an even day. You can go outside.")