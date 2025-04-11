import re
def check(DNA_sequence, enzyme_cut_site):
   if re.fullmatch(r"[ACGT]+",DNA_sequence):
      if re.search(r"[ACGT]+",enzyme_cut_site):
         match = re.search(enzyme_cut_site, DNA_sequence)
         if match:
          wanted = match.start()+1
          return wanted
         else:
            return "Not match"
            
      else:
         return "Enzyme not valid"
   else:
       return "DNA sequence not valid"  

# examples
# Case 1
dna1 = "ATACGTAGCT"
enzyme1 = "ACGT"
print(check(dna1, enzyme1))  # Output: 3

# Case 2
dna2 = "ACGTXGCT"
enzyme2 = "AGCT"
print(check(dna2, enzyme2))  # Output: DNA sequence not valid

# Case 3
dna3 = "AAAAAAA"
enzyme3 = "ACGT"
print(check(dna3, enzyme3))  # Output: Not match  
         
    
      