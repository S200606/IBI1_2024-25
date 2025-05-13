human = open(r'C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical13\P04179.fasta', 'r').readlines()
human_sequence = ''.join(line.strip() for line in human[1:])
mouse = open(r'C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical13\P09671.fasta', 'r').readlines()
mouse_sequence = ''.join(line.strip() for line in mouse[1:])
random = open(r'C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical13\random.fasta', 'r').readlines()
random_sequence = ''.join(line.strip() for line in random[1:])



def load_blosum():
    matrix = open(r'C:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical13\BLOSUM62.txt', 'r').readlines()
    blosum = {}
    labels = matrix[0].strip().split()
    for i, line in enumerate(matrix[1:]):
        scores = line.strip().split()
        x_label = scores[0]  # amino acid
        blosum[x_label] = {}
        for j, score in enumerate(scores[1:]):
            blosum[x_label][labels[j]] = int(score)
    return blosum

def align(seq1,seq2,blosum):
    score = 0
    identical = 0
    for aa1,aa2 in zip(seq1,seq2):
        if aa1 in blosum and aa2 in blosum[aa1]:
            score += blosum[aa1][aa2]
            if aa1 == aa2:
                identical += 1
    caids = (identical / len(seq1)) * 100
    print(f"Alignment score: {score}")
    print(f"Percentage of identical amino acids: {caids:.2f}%")
    return score, caids

blosum = load_blosum()
        

print('huaman vs mouse:',align(human_sequence, mouse_sequence,blosum))
print('huaman vs random:',align(human_sequence, random_sequence,blosum))
print('mouse vs random:',align(mouse_sequence, random_sequence,blosum))
    