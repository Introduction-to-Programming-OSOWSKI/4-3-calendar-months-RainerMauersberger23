def calendar(c):
    for i in range(0, len(month)):
        if c == month[i]:
            return i

    return c + " is not a month"

month = ["january", "febuary", "march", "april", "may", "june", "july", "august" "september", "october", "november", "december"]
print (calendar("june"))