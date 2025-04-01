#create a sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
#find all the introns
intron = re.findall(r'(GT.*AG)', seq) #begin with first GT and end with last AG
largest_intron = intron[0] #set the first intron as the largest
length = len(largest_intron) #the length of the intron
print("the longest intron is", intron)
print("the length of it is", length)
