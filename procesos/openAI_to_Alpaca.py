import json

with open("dataset_teoria.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_alpaca_dataset = []
    id_count = 0
    
    for data in dataset:
        id_count += 1
        messages = data.get("messages", [])
        new_alpaca_data = {
            "id": id_count,  # Puedes cambiar el ID según sea necesario
            "name": messages[0]["content"] if messages else "",
            "instruction": messages[1]["content"] if len(messages) > 1 else "",
            "instances": [{"input": "", "output": messages[2]["content"]} if len(messages) > 2 else ""],
            "is_classification": False
        }
        new_alpaca_dataset.append(new_alpaca_data)
    
    return new_alpaca_dataset

new_alpaca_dataset = convert_format(dataset)

with open("dataset_alpaca_format.jsonl", 'w', encoding="utf8") as file:
    for data in new_alpaca_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')