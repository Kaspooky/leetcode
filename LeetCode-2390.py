def removeStar(s: str):
    retString = ""
    newString = [x for x in s]
    indexList = []
    if s.count("*") >= len(s)/2:
        return ""
    print(s.count("*"))
    print(newString)
    for i, char in enumerate(newString[1:], start=1):
        if char == "*":
            # print("* found at: ", i)
            indexList.append(i)
            counter = i-1
            while counter >= 0:
                # print("counter: ", counter)
                if char == "\*":
                    # print("* found at: ", counter)
                    counter -= 1
                    continue
                if counter not in indexList:
                    # print("Removing char at: ", counter)
                    indexList.append(counter)
                    break
                else:
                    counter -= 1
                    continue
        # print(i, " ", char)
    indexList.sort(reverse=True)
    for val in indexList:
        newString.pop(val)
    return retString.join(newString)


print(removeStar("leet**cod*e"))


# enumerate s
# when we find a '*', we backtrack from given index and remove the earliest non '*' character.
