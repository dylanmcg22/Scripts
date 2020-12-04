import io  # io is input output

with open('log.txt', 'w') as writeFile:
    toLog = input("What do yo want to write to the log? ")
    writeFile.write(toLog)