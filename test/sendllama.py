import replicate
# Import the json module
import json
import re

pattern = r'[a-zA-Z]+'

# Define the path to your JSONL file
file_path = 'test.jsonl'

# Initialize an empty list to store the dictionaries
data_list = []

# Open the file in read mode
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Convert the JSON string to a dictionary
        #print(line)
        data = json.loads(line)
        # Append the dictionary to the list
        #data_list.append(data)
        pos = data['text'].find("Response: ")
        data['text'] = data['text'][:pos + len("Response: ") - 1]
        data_list.append(data)

# Now, data_list contains a list of dictionaries
print(data_list)

raw_answers = []
counter = 0
for data in data_list: 
    #print(data['text'])


    output = replicate.run(
        "carlos-elias-riv/llama2-semanticsimilarity:bc54eb33e31e8588f4ceefbedc3616af7204a6e8816f0c3ffccab149a4be9d95",
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 0.9,
            "prompt": data['text'],
            "temperature": 0.75,
            "max_new_tokens": 128,
            "min_new_tokens": -1
        }
    )

    # The carlos-elias-riv/llama2-semanticsimilarity model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    temp = ""
    for item in output:
        temp += item
    temp = temp.lower()
    print(temp, counter)
    if "yes" or "no" in temp:
        raw_answers.append(temp)
    else: 
        raw_answers.append("error")

    counter += 1

    

print(raw_answers)

responses = []

for i in range(len(data_list)):
    responses.append({"text": data_list[i]['text'] + raw_answers[i]})

# we save the data to a jsonl file

with open('output.jsonl', 'w') as outfile:
    for entry in responses:
        json.dump(entry, outfile)
        outfile.write('\n')

