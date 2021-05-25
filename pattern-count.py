# counting how many times pattern is in text (e.g. genome) - solution for Bioinformatics course


def PatternCount(text,pattern):
    count=0
    for i in range(len(text)+1-len(pattern)): 
        if text[i:i+len(pattern)]==pattern:
            count+=1
    return count