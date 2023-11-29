import json

with open("dataset_teoria.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_basic_dataset = []
    
    for data in dataset:
        messages = data.get("messages", [])
        new_basic_data = {
            "prompt": messages[1]["content"] if len(messages) > 1 else "",
            "answer": messages[2]["content"] if len(messages) > 2 else "",
        }
        new_basic_dataset.append(new_basic_data)
    
    return new_basic_dataset

new_basic_dataset = convert_format(dataset)

with open("dataset_basic_format.jsonl", 'w', encoding="utf8") as file:
    for data in new_basic_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')