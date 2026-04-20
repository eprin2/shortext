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



def raw(inp):
    data = get_data(inp, show=False)[0]["text"]
    data = re.sub(r'={2,3}', '', data)  # usuń == i ===
    data = data.replace('\n', ' ')      # usuń \n
    tokens = [n for i in data.split(". ") for n in i.split(" ") if n.strip()]
    return " ".join(tokens)
print(raw("data.json"))