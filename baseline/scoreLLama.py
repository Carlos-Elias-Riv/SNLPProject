import json
import re

file_path = "output.jsonl"
results = []
pattern = r'[a-zA-Z]+'
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Convert the JSON string to a dictionary
        #print(line)
        data = json.loads(line)
        # Append the dictionary to the list
        #data_list.append(data)
        pos = data['text'].find("Response:")
        data['text'] = data['text'][pos + len("Response:"):]
        data['text'] = data['text'].replace(" ", "")
        matches  = re.findall(pattern, data['text'])
        
        text = ""

        for match in matches:
            text += match

        data['text'] = text
        results.append(data)

#print(results)
        
ground_truth = []

with open("test.jsonl", 'r') as file:
    for line in file:
        data = json.loads(line)
        pos = data['text'].find("Response:")
        data['text'] = data['text'][pos + len("Response:"):]
        data['text'] = data['text'].replace(" ", "")
        ground_truth.append(data)

#print(ground_truth)
possible_answers = ['yes', 'no']
matchcounter = 0
errorcounter = 0

for pos in range(len(ground_truth)):
    #print(ground_truth[pos]['text'], results[pos]['text'])
    bool1 = possible_answers[0] in results[pos]['text']
    bool2 = possible_answers[1] in results[pos]['text']
    if bool1 != bool2:
        if ground_truth[pos]['text'] in results[pos]['text']:
            print("Match")
            print(ground_truth[pos]['text'], results[pos]['text'])
            matchcounter += 1
        else:
            pass
            #print("No match")

    else: 
        print("Error")
        errorcounter += 1

print("Match counter: ", matchcounter)
print("Error counter: ", errorcounter)
print("Len ground_truth", len(ground_truth))