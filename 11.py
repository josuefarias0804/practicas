dic = {
  'ID' : 1,
  'NOMBRE' : 'Juan',
}
print({clave.lower(): str(valor) for clave, valor in dic.items()})

dic['id'] = dic.pop('ID')
dic['nombre'] = dic.pop('NOMBRE')
dic['id'] = '1'

print(dic)

