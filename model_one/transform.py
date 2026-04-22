import json
import re
def get_data(data_file, show=False):
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if show:
            for item in data:
                print(f"loaded: {item['url']}")
            print()
            print()
            print("====loaded====")
            print()

        return data



    return all



def raw(inp,ind):
    data = get_data(inp, show=False)[ind]["text"]
    data = re.sub(r'={2,3}', '', data)  # usuń == i ===
    data = data.replace('\n', ' ')      # usuń \n
    data = data.replace('(', ' ')      # usuń \n
    data = data.replace(')', ' ')      # usuń \n
    tokens = [n for i in data.split(". ") for n in i.split(" ") if n.strip()]
    return " ".join(tokens)
def add_token_transform(inp,ind,lists):
    te=lists[0]
    ty=lists[1]
    for i in raw(inp,ind).split(" "):
        if i in te:
            pass
        else:
             te.append(i)
             ty.append([])
    return te,ty
def token_transform(inp,lists):
    te=[]
    ty=[]
    for i in range(len(inp)):
        x=add_token_transform(inp,i,lists)
        te=te+x[0]
    for i in te:
        ty.append(5580*[0])
    return te,ty
          
def get_list_dic(inp):
        da=get_data("dic.json")
        dic_te=[]
        dic_ty=[]
        for i in da:
             dic_te.append(i["text"])
             dic_ty.append(i["type"])        
        return dic_te,dic_ty

