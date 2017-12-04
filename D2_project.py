
import json

business_id =[]
categories = []
i = 0
with open("business.json") as json_file:
    try:
        for line in json_file:
            line_contents = json.loads(line)
            #business_id.append(line_contents['business_id'])
            categories.append(line_contents['categories'])
            i += 1
    except UnicodeDecodeError:
        print("failed to parse data")
        pass

for i in categories:
    if 'Health' and 'Pets' and 'Zoos' not in i:
        print(i)

#print(len(business_id))
print('\n')



b_id =[]
j = 0
with open("review.json") as json_file:
    try:
        for l in json_file:
            l_contents = json.loads(l)
            b_id.append(l_contents['business_id'])
            j += 1
    except UnicodeDecodeError:
        print("failed to parse data")
        pass
#print(b_id)
#print(len(set(b_id)))


for id in business_id:
    if id in b_id:
        pass
    else:
        print('F')




