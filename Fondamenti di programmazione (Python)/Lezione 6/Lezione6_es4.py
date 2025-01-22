str = "X-DSPAM-Confidence:0.8475"
indice=str.find(":")
n=float(str[indice+1:len(str)])
print(n)
