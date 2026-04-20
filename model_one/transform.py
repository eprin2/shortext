import json

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

    
for i in get_data("data.json", show=True)[0]["text"].split(". "):
    print(i)