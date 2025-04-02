import re
donor = input("the donor is:")#input the donor
acceptor = input("the acceptor is:")#input the acceptor
input = open(r"c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")#open the file
# 
spliced_genes = []#set the list to store the spliced genes

#find all the spliced sequences
gene_entry = ""#set the gene entry to empty
for line in input:
    if line.startswith(">"):
        if gene_entry:
            header, sequence = gene_entry.split("\n", 1)
            header = re.findall(r'(>.*?)[_\s]', header)[0]#find the header in the gene entry
            sequence = sequence.replace("\n", "")  # remove newlines in the sequence
            genes = re.findall(fr'(?=({donor}.*?{acceptor}))', sequence)
            genes = [gene for gene in genes if re.search(r"TATA[AT]A[AT]", gene)]  # select the genes that contain TATA
            spliced = "".join(genes)  
            numbers = re.findall(r'TATA[AT]A[AT]', spliced)  
            instances_number = len(numbers)  #count the number of TATA
            if re.search(fr'{donor}.*?{acceptor}',sequence):
              if re.search(r"TATA[AT]A[AT]", sequence):
                if instances_number > 0:
                  header = f"{header},{instances_number}"
                  spliced_genes.append(f"{header}\n{sequence}")
        gene_entry = line.strip()
    else:
        gene_entry += "\n" + line

#process the last gene entry
if gene_entry:
    header, sequence = gene_entry.split("\n", 1)
    header = re.findall(r'(>.*?)[_\s]', header)[0]
    sequence = sequence.replace("\n", "")  
    genes = re.findall(fr'(?=({donor}.*?{acceptor}))', sequence)
    genes = [gene for gene in genes if re.search(r"TATA[AT]A[AT]", gene)]
    spliced = "".join(genes)  
    numbers = re.findall(r'TATA[AT]A[AT]', spliced)  
    instances_number = len(numbers)  #count the number of TATA
    if re.search(fr'{donor}.*?{acceptor}',sequence):
              if re.search(r"TATA[AT]A[AT]", sequence):
                if instances_number > 0:
                  header = f"{header},{instances_number}"
                  spliced_genes.append(f"{header}\n{sequence}")

#write the result to the file:
output = open(fr"c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical7\{donor}{acceptor}_spliced_genes.fa", "w")
output.write("\n".join(spliced_genes))



