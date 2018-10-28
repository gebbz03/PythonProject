
import pickle

dict_data={'name':'Gebb Ebero','country':'Philippines'}

with open('serialize','wb') as fobj:
    pickle.dump(dict_data,fobj)

with open('serialize','rb') as fobj:
    dict_data=pickle.load(fobj)
    print(dict_data)    