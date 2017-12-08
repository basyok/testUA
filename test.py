import re

#Task 1
#"asdflj  port )(unclosed"
string = "asdflj (kla (inner) asd) port (another ))(unclosed"
def fn(st):
    for x in re.finditer("\([\w ]+\)", st, re.IGNORECASE):
        st = st.replace(x.group(0), "")
    return st

result = fn(fn(string))
print(result)



#Task Additional
with open("./parameters.txt") as f:
    params = {}
    x = f.readline().split(" ")
    params["common"] = {}
    params["common"]["aisleLength"] = x[0]
    params["common"]["walkSpeed"] = x[1]
    params["common"]["runSpeed"] = x[2]
    params["common"]["runTime"] = x[3]
    params["common"]["linesTotal"] = x[4].strip("\n")

    print(params)

    #have speed boost
    #beside lanes – is the distance which is either to be run or walked
    if (params["common"]["linesTotal"] is not None and int(params["common"]["linesTotal"]) > 0):
        counter = 1
        for line in f.readlines():
            l = line.split(" ")
            params["line{}".format(counter)] = {}
            params["line{}".format(counter)]["start"] = l[0]
            params["line{}".format(counter)]["end"] = l[1]
            params["line{}".format(counter)]["speed"] = l[2].strip("\n")
            counter += 1
        print(params)

        totalLanesDistance = 0
        totalLanesTime = 0
        for k,v in params.items():
            if k.find("line") != -1:
                distance = float(v["end"]) - float(v["start"])
                laneSpeed = float(v["speed"]) + float(params["common"]["walkSpeed"])
                laneTime = distance / laneSpeed
                totalLanesDistance += distance
                totalLanesTime += laneTime

        totalUnaidedDistance = float(params["common"]["aisleLength"]) - totalLanesDistance
        totalRunDistance = float(params["common"]["runSpeed"]) * float(params["common"]["runTime"])

        if totalUnaidedDistance > 0:
            remainedUnaidedDistance = totalLanesDistance - totalRunDistance
            if remainedUnaidedDistance > 0:
                timeRemainder = remainedUnaidedDistance / float(params["common"]["walkSpeed"])
                minimalTime = totalLanesTime + timeRemainder + float(params["common"]["runTime"])
            elif remainedUnaidedDistance == 0:
                timeRemainder = (totalRunDistance + remainedUnaidedDistance) / float(params["common"]["runSpeed"])
                minimalTime = totalLanesTime + timeRemainder + float(params["common"]["runTime"])
            elif remainedUnaidedDistance < 0:
                timeRemainder = (totalRunDistance + remainedUnaidedDistance) / float(params["common"]["runSpeed"])
                minimalTime = totalLanesTime + timeRemainder
        elif totalUnaidedDistance == 0:
            minimalTime = totalLanesTime

        print(minimalTime)

    #don't have speed boost
    else:
        runDistance = int(params["common"]["runSpeed"]) * int(params["common"]["runTime"])
        print(runDistance)
        remainedDistance = int(params["common"]["aisleLength"]) - runDistance
        remainedTime = remainedDistance / int(params["common"]["walkSpeed"])
        minimalTime = int(params["common"]["runTime"]) + remainedTime
        print(minimalTime)


