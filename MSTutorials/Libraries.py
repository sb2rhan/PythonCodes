#   importing classes from datetime library

# from datetime import datetime, timedelta

#   the now function returns a datetime object
#today = datetime.now()
#print("Today is: " + str(today))

#print("Day: " + str(today.day))
#print("Month: " + str(today.month))
#print("Year: " + str(today.year))

#  timedelta is used to define a period of time

#seven_days = timedelta(weeks = 1)
#a_week_ago = today - seven_days
#print("A week ago was: " + str(a_week_ago))


# trying to operate with try and catch
# Python is sensitive at spaces 
# after ':' should be 4 spaces!!!

#try:
#    birthday = input("When's your birthday(dd/mm/yyyy): ")
#    print("This is try/catch")
#    birthday_date = datetime.strptime(birthday, "%d/%m/%Y")       # converting string to datetime object
#    print("Birthday: "+str(birthday_date))                        # then outputing it as a string
#    birthday_eve=birthday_date-timedelta(days=1)
#    print("Day before birthday: " + str(birthday_eve))
#except ValueError as e:
#    print("You entered incorrect date")
#else:
#    print("Something else went wrong")
#finally:
#    print("This is try/catch")