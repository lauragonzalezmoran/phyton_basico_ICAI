#Marathon Time Calucultor - www.101computing.net/marathon

#Step 1: INPUT: Ask the runner for their pace (e.g. 5:25)
str_pace = input("At what pace do you run a km? (e.g. 5:21): ")

#Step 2: PROCESS: Convert this input into a number of seconds: e.g. 5:25 = 5 * 60 + 25 = 325 seconds
#...

minutes = int(str_pace[:1])

seconds = int(str_pace[-2:])

total_secs = (minutes * 60) + seconds

#Step 3: PROCESS: Multiply this total by 42 as there are 42km in a Marathon
#...
totalTime = total_secs * 42

#Step 4: PROCESS: Convert this new total using the hh:mm:ss format. (e.g 3:47:30)
#...


#Step 5: OUTPUT: Display this new total on screen (using the hh:mm:ss format). (e.g 3:47:30)
#...
print(f"The total time is: {totalTime}")