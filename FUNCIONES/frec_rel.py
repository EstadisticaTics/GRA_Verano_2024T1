def frec_rel(fa_absoluta):
  

  total_datos = sum(fa_absoluta)
  fr = []

  for i in range(len(fa_absoluta)):
    fr.append((fa_absoluta[i] / total_datos) * 100)

  return fr
