'''
objective: learn how to use json file format a little bit
'''
import json

with open('../data/example.json') as f:
    dat = json.load(f)
print(dat)

# write to a json file

data = dict()
data['uri'] = 'someName'
data['db'] = 'analysis'
data['xlim'] = [0,10]
data['ylim'] = [1,2]
data['offset']=10
data['boolean']=True




with open('../../Downloads/temp.json','w') as fout:
    json.dump(data,fout,indent=1)

print(fout)



