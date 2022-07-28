import statistics
import random
import plotly.figure_factory as pf
import plotly.graph_objects as pg


diceSum = []
for i in range(0,1000):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    diceSum.append(d1+d2)

mean = statistics.mean(diceSum)
median = statistics.median(diceSum)
mode = statistics.mode(diceSum)
stdev = statistics.stdev(diceSum)


print("Mean : " , mean)
print("Median : " , median)
print("Mode : " , mode)
print("Std Deviation : " , stdev)

print("----------------------------------")

graph = pf.create_distplot([diceSum] , ["Dice Sum"] , show_hist= False)
graph.show()


# -----------------------------------------------------------------------------

stdevStart1 , stdevEnd1 = mean-stdev , mean+stdev

stdevStart2 , stdevEnd2 = mean-(2 * stdev) , mean+(2 * stdev)

stdevStart3 , stdevEnd3 = mean-(3 * stdev) , mean+(3 * stdev)


listOfDataLyingWithin1 = [i for i in diceSum if i>stdevStart1 and i<stdevEnd1]

listOfDataLyingWithin2 = [i for i in diceSum if i>stdevStart2 and i<stdevEnd2]

listOfDataLyingWithin3 = [i for i in diceSum if i>stdevStart3 and i<stdevEnd3]


a = len(listOfDataLyingWithin1)

b = len(listOfDataLyingWithin2)

c = len(listOfDataLyingWithin3)

n = len(diceSum)

# --------------------------------------------------------------------

p1 = (a*100)/n
p2 = (b*100)/n
p3 = (c*100)/n

print("Percentage of data within stdev 1 : " , p1)

print("Percentage of data within stdev 2 : " , p2)

print("Percentage of data within stdev 3 : " , p3)