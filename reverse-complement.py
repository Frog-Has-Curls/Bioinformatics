
#return reverse and complementary strand of DNA 


def ReverseComplement(dna):
    complement=''
    for i in dna:
        if i=='A':
            complement+='T'
        if i=='T':
            complement+='A'
        if i=='C':
            complement+='G'
        if i=='G':
            complement+='C'
    return(complement[::-1])