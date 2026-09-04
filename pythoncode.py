# print vertical output [range(start,end,skip)]
for i in range(1,6,1):
  for j in range(1,6,1):
    print(i)

# print convert vertical output to horizontal output
for i in range(1,6,1):
  for j in range(1,6,1):
    print(i, end = " ")

# print shape shape output with *
for i in range(1,6,1):
  for j in range(1,6,1):
    print("*" , end = " ")
  print("\r")

# print right angle triangle with number
for i in range(1,6,1):
  for j in range(1,i,1):
    print(i, end = " ")
  print("\r")

# print right angle triangle with *
for i in range(1,6,1):
  for j in range(1,i,1):
    print("*", end = " ")
  print("/r")

# print left angle triangle with number
for i in range(1,6,1):
  for k in range(1,6-i,1):
    print(end = " ")
  for j in range(1,i,1):
    print(i, end = "")
  print("\r")

# print left angle triangle with *
for i in range(1,6,1):
  for k in range(1,6-i,1):
    print(end = " ")
  for j in range(1,i,1):
    print("*", end = "")
  print("\r")
