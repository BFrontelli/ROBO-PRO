import json,os,time
ARQ='data/cache.json'
TTL=21600

def ja_enviado(l):
 os.makedirs('data',exist_ok=True)
 if not os.path.exists(ARQ): json.dump({},open(ARQ,'w'))
 c=json.load(open(ARQ))
 if l in c and time.time()-c[l]<TTL: return True
 c[l]=time.time(); json.dump(c,open(ARQ,'w')); return False
