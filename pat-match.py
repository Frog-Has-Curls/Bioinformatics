

#pattern matching for Bioinformatics course

def PatternMatch(pattern, genome):
    match=[i for i in range(len(genome)) if genome.startswith(pattern, i)]
    mat=''
    mat=' '.join([str(ele) for ele in match])
    return(mat)