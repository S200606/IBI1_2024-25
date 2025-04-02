import re

pattern = r'TATA[AT]A[AT]'#set the aim sequence
genes = []#set the list to store the genes
#input the file
input = open(r"c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
output = open(r"c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical7\tata_genes.fa", "w")

gene_entry="" #set the gene entry to empty
for line in input:   
    if line.startswith(">"):
         if gene_entry:  # process the previous gene entry
             header, sequence = gene_entry.split("\n", 1)#seperate the head and gene sequences by the first newline
             sequence = sequence.replace("\n", "")  # remove newlines in the sequence
             header = re.findall(r'(>.*?)[_\s]', header)[0]#find the header in the gene entry
             if re.search(pattern, sequence):
                 genes.append(f"{header}\n{sequence}")#append the header and sequence to the list
         gene_entry = line.strip()#start a new gene entry
    else:
        gene_entry += "\n" + line#add the line to the gene entry

#process the last gene entry
if gene_entry:
    header, sequence = gene_entry.split("\n", 1)
    sequence = sequence.replace("\n", "")
    header = re.findall(r'(>.*?)[_\s]', header)[0]
    if re.search(pattern,sequence):
        genes.append(f"{header}\n{sequence}")

#write the result to the file
output = open(r"c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical7\tata_genes.fa", "w")
output.write("\n".join(genes))#write the genes to the file and seperate them by newlines


                
                

 
        