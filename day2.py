list = []
result = 0

with open("2.txt") as f:
	list = f.read().splitlines()

for i in range(0, len(list)):
	list[i] = list[i].split(" ")

	list[i][0] = list[i][0].split("-")
	list[i][0][0] = int(list[i][0][0])
	list[i][0][1] = int(list[i][0][1])

	list[i][1] = list[i][1].rstrip(":")

	list[i][2] = list[i][2]
	
  #part 1
	#occ = list[i][2].count(list[i][1])
	#if occ >= list[i][0][0] and occ <= list[i][0][1]:
	#	result += 1
	
	# part 2
	if list[i][2][(list[i][0][0])-1] == list[i][1]: 
		result += 1
	elif list[i][2][(list[i][0][1])-1] == list[i][1]: 
		result += 1

print(result)
