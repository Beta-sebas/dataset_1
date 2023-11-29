import json

with open("dataset_teoria.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_one_dataset = []
    
    for data in dataset:
        messages = data.get("messages", [])
        new_one_data = {
            "data": "User: " + messages[1]["content"] + " Assistant: " + messages[2]["content"] if len(messages) > 2 else ""
        }
        new_one_dataset.append(new_one_data)
    
    return new_one_dataset

new_one_dataset = convert_format(dataset)

with open("dataset_one_format.jsonl", 'w', encoding="utf8") as file:
    for data in new_one_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')