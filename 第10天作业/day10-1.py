def read_dic(path):
    codon_dict = {}
    with open(path, 'r') as f:
        for line in f:
            codon, animo = line.split()
            if len(codon) == 3:
                codon_dict[codon] = animo
    return codon_dict

def transcript(dna):
    tem_dic = {"A":"U","T":"A","C":"G","G":"C"}
    rna  = ''
    for i in range(len(dna)):
        rna += tem_dic[dna[i]]
    return rna

def translate(dna, codon_dict):
    rna = transcript(dna)
    st = ed = False
    index = 0
    amino = ''
    while not ed and index+3 <= len(rna):
        codon = rna[index:index+3]
        if codon == 'AUG' and not st:
            st = True
            amino += codon_dict[codon]
        elif st and codon_dict[codon] == 'stop':
            ed = True
        elif st:
            amino += codon_dict[codon]
        index += 3 if st else 1 
    return amino

def read_fa(path):
    seq_dict = {}
    with open(path,'r') as f:
        text = f.readlines()
        for i in range(0,len(text),2):
            seq_dict[text[i][1:-1]] = text[i+1][:-1]
    return seq_dict


def dna2protein():
    codon_dict = read_dic('codon.txt')
    seq_dict = read_fa('seq.fa')
    protein_dict = {}
    for k,v in seq_dict.items():
        protein_dict[k] = translate(v,codon_dict)
    with open('protein.txt','w') as f:
        for k,v in protein_dict.items():
            f.write(k+'\n')
            f.write(v+'\n')
# seq2压根就没有匹对的中止密码子
dna2protein()

