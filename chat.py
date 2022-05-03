# What is \ufeff> sublime add its encoding code
def read_file(filename):
	lines = []
	with open(filename,"r", encoding="utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new_lines = []
	person = None
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue		
		if person:
			new_lines.append(person + ": " + line)
	return new_lines

def write_file(filename, lines):
	with open(filename,"w") as f:
		for line in lines:
			f.write(line + "\n")

def main():
	lines= read_file("input.txt")
	lines= convert(lines)
	write_file("output.txt",lines)
	print(lines)

main()