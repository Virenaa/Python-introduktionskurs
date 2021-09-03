def combineDicts(dict1, dict2):
    for key,value in dict2.items():
        if key in dict1.keys():
            dict1[key]+=value
        else:
            dict1[key]= value
dict1={'Ägg':2, 'Bröd':1, 'Smör':1, 'Potatis':5, 'Gifflar':1}
dict2={'Nudlar': 4, 'Nutella':2, 'Gifflar':2, 'Bröd':1}

combineDicts(dict1,dict2)
print(dict1)
