# Fractional knapsack python program
# Input-
# n - the number of total items
# weight - list for weight of each item
# profit - list for profit of each item
# w - total capacity of the bag
print(&quot;Enter the number of total items&quot;)
n = int(input())
print(&quot;Enter the weights of each item&quot;)
weight = list(map(int, input().split()))
print(&quot;Enter the profits of each item&quot;)
profit = list(map(int, input().split()))
print(&quot;Enter the capacity of the bag&quot;)
w = int(input())
items=[]
for i in range(n):
items.append([(profit[i]/weight[i]),i])
items.sort(reverse=True)
# print(items)
curr = 0
tot = 0
print(&quot;Item No. Weight Profit&quot;)
while w&gt;0 and curr&lt;n:
if w &gt;= weight[items[curr][1]]:
fraction = 1
w -= weight[items[curr][1]]
tot += profit[items[curr][1]]
else:
fraction = w/weight[items[curr][1]]
w -= fraction*weight[items[curr][1]]
tot += fraction*profit[items[curr][1]]
print(items[curr][1],fraction*weight[items[curr][1]],fraction*we
ight[items[curr][1]])
curr += 1
print(tot)