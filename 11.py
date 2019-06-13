dic = {
  'ID' : 1,
  'NOMBRE' : 'Juan',
}

dic['id'] = dic.pop('ID')
dic['nombre'] = dic.pop('NOMBRE')
dic['id'] = '1'

print(dic)