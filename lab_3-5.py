
#Create a Python file named lab_3-5.py

#Import the time and math modules.
import time
#Calculate 22 using math.pow and again using the ** operator.
2**2
#Record the time using time.process_time before and after each calculation (Hint: you may need to store the result of time.process_time in a variable)
print time._process_time 2**2 
#Add a statement that prints the elapsed time after each statement is processed. Run the program. What do you notice? Write it as a comment.
print (time._process_time)
#Change each statement that records the time to use time.perf_counter instead of time.process_time.
print (time.perf_counter)
#Run the program again. What do you notice? Write it as a comment.

