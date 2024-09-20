import json

def read_players_from_json(filename: str):
    with open(filename, 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return data

def write_to_json(data, filename):
    with open(filename, 'w', encoding="utf8") as file:
        json.dump(data, file, indent=4)

# f = read_players_from_json("../assets/data.json")
# for i in f:
#     if "-" in i["position"]:
#         f.remove(i)
#         continue
#     for key, value in i.items():
#         if value == None:
#             i[key] = 0
#
# write_to_json(f, "../assets/data.json")
