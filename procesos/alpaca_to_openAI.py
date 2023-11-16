import json

with open("dataset_alpaca_format.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]


def convert_format(dataset):
    new_openAI_dataset = []
    
    for data in dataset:
        
        messages = []
        
        if data.get("name"):
            messages.append({"role": "system", "content": data.get("name")})
        if data.get("instruction"):
            messages.append({"role": "user", "content": data.get("instruction")})
        if data.get("instances") and len(data["instances"]) > 0 and data["instances"][0].get("output"):
            messages.append({"role": "assistant", "content": data["instances"][0]["output"]})
        
        openAI_data = {"messages": messages}
        new_openAI_dataset.append(openAI_data)
    
    return new_openAI_dataset



new_openAI_dataset = convert_format(dataset)

with open("dataset_openAI_format.jsonl", 'w', encoding="utf8") as file:
    for data in new_openAI_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')