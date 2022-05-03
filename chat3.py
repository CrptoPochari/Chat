lines = []
with open("3.txt", "r", encoding = "utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(" ")
	# In python, string is treat as list
	time = s[0][:5]
	name = s[0][5:]
	print("time= ", time,"name= ", name)	
	print(line)