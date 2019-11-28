import json

def initialisation(list_of_labels,userID):
    try:
        with open('data.json', 'r') as f:
            dic = json.loads(f)
    except TypeError:
        dic = {}
    if userID in dic:

    dic['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
    print(dic)
    with open('data.json', 'w') as f:
        json.dump(dic,f)

initialisation([1],1)
