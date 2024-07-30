import json

with open("amadeus_TRL_CONCEPTUAL_DATASET_v1.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_basic_dataset = []
    
    for data in dataset:
        messages = data.get("messages", [])
        new_basic_data = {
            "prompt": messages[1]["content"] if len(messages) > 1 else "",
            "response": messages[2]["content"] if len(messages) > 2 else "",
        }
        new_basic_dataset.append(new_basic_data)
    
    return new_basic_dataset

new_basic_dataset = convert_format(dataset)

with open("amadeus-train.jsonl", 'w', encoding="utf8") as file:
    for data in new_basic_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')