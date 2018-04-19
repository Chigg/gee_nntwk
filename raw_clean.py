#cleaning

import re
import itertools

def main():

	file = input("Please enter file Path:\n")

	inFile = open(file, "r")
	text = inFile.readlines()
	output_file = file[:-7]
	output_file = output_file+"clean.txt"
	output = open(output_file, 'w')

	for line in text:
		#find urls
		find = re.findall('(http|ftp|https)(://)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?', line)			

		#join and write to output file
		if find:
			s = ''.join(itertools.chain(*find))
			output.write(s)
			output.write('\n')
			

		find = ""
		
	print("Done!")
main()