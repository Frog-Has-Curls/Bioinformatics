

#Frequent Words as dictionary solution for Bioinformarics course

def FrequentWords(text,k):
  dict={}
  for i in range(len(text)-k):
    zdanie=text[i:i+k]
    if zdanie in dict:
      dict[zdanie]+=1
    else:
      dict[zdanie]=1
  return(dict)