actor_dictionary = {'Daniel Craig': ['Casino Royale', 'Skyfall', 'Spectre'], 'Tom Cruise': ['Mission Impossible', 'Vanilla Sky', 'Top Gun', 'Minority Report'], 'Rowan Atkinson': [' Mr Bean', 'Johnny English']}


for key, value in actor_dictionary.items():
    print(key + " worked in", value)

for key, value in actor_dictionary.items():
    print(key+" worked in",len(value), " movies")

for key, value in sorted(actor_dictionary.items(), key=lambda x: x[0].split()[-1],reverse=False):
    print(key)