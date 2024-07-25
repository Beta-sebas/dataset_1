import json

with open("amadeus_TRL_CONCEPTUAL_DATASET_v1.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_alpaca_dataset = []
    id_count = 0
    
    for data in dataset:        
        messages = data.get("messages", [])
        new_alpaca_data = {                    
            "instruction": messages[1]["content"] if len(messages) > 1 else "",
            "input": "",
            "output": messages[2]["content"] if len(messages) > 2 else ""
        }
        new_alpaca_dataset.append(new_alpaca_data)
    
    return new_alpaca_dataset

new_alpaca_dataset = convert_format(dataset)

with open("amadeus_TRL_CONCEPTUAL_DATASET_alpaca_format.json", "w", encoding="utf-8") as f:
    json.dump(new_alpaca_dataset, f, ensure_ascii=False, indent=4)       