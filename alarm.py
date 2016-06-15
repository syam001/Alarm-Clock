# Alarm clock
# Loop and print the time
# Activate a youtube video if the time is equal 
# Patrick Mogianesi /June 15th 2016/

#Import libraries
import time
import webbrowser

#The User can set the time they want to wake up. The String the user puts in must be the same as the example to work.
print "What time do you want to wake up?"
print "Use this form.\nExample: 06:30:00"
Alarm = raw_input("> ")


#I first need to state the Time variable so it's usable in the while-loop
Time = time.strftime("%H:%M:%S")



#When the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:
	
	print "The time is " + Time
	
	#Restating the Time variable allows the time to refresh
	#When I tried keeping the variable outside of the loop it just repeated the inital time
	Time = time.strftime("%H:%M:%S")
	
	#This keeps the loop from flooding the command line with updates of the time :P
	time.sleep(60)

#If the Time variable is equal to the Alarm string, this code activates
if Time == Alarm:

	print "Time to Wake up!"
	#Using the webbrowser library, it opens this youtube video link.
	webbrowser.open("https://www.youtube.com/watch?v=OGbhJjXl9Rk")
