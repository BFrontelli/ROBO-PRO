import os,importlib
def carregar():
 plats=[]
 for a in os.listdir('plataformas'):
  if a.endswith('.py') and a!='__init__.py':
   m=importlib.import_module(f'plataformas.{a[:-3]}')
   plats.append((a[:-3],m.coletar_ofertas))
 return plats
