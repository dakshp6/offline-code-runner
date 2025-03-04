import os
import json
from practice import Solution

if __name__ == '__main__':

    file = None

    if os.stat("testcases.txt").st_size != 0:
        file = open("testcases.txt", "r")

    else:
        print("No Test Cases in file")
        exit()


    counter = 0

    for line in file:
        if not line.strip():
            continue
        line = line.strip()
        counter+=1

        args = []

        ls = list(line.split(" "))

        for i in ls:
            args.append(json.loads(i))
    
        res = Solution.practiceFunc(*args)
        print("Test Case " + str(counter) + ": " + line + "\nResult: " + str(res) + "\n")
    
    file.close()