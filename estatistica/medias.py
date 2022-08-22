x = [39,38,27,22,20,17,10,10,10,10,7,7,7,7,6]

def media_aritmetica(x):
  n = len(x)
  soma = 0
  for i in range(0,n):
    soma = soma + x[i]
  media = soma / n
  return (media)
#------------------------------
def media_harmonica(x):
    n = len(x)
    soma = 0
    for i in range(0,n):
        soma = soma + (1/x[i])
    media = n / soma
    return (media)
#------------------------------
def media_ponderada(x, w):
  soma_encima = 0
  soma_embaxio = 0
  for i in range(0, len(x)):
    soma_encima = soma_encima + x[i]*w[i]
    soma_embaixo = soma_embaixo + w[i]
  media = soma_encima / soma_embaixo 
#------------------------------
def mediana(x):
  x.sort()
  n= len(x)
  if n % 2 ==0:
    a = int(n/2)
    mediana = x[a]
  else:
    a = int(n/2)
    b = a-1
    mediana = 0.5*(x[a]+x[b])
    return(mediana)  