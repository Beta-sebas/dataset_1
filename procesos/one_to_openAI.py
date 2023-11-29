import json

with open("80 datos postfinetuinig.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def convert_format(dataset):
    
    new_openAI_dataset = []
    
    for data in dataset:
        
        messages = []
        
        text = data.get("data")
        resultado = text.split(' Assistant: ')
        
        messages.append({"role": "system", "content": "Este es un asistente para la evaluación del TRL."})
        messages.append({"role": "user", "content": resultado[0].replace("User: ","")})
        messages.append({"role": "assistant", "content": resultado[1]})
        
        openAI_data = {"messages": messages}
        print(openAI_data)
        new_openAI_dataset.append(openAI_data)
    
    
    return new_openAI_dataset

new_openAI_dataset = convert_format(dataset)

with open("80dataset_openAI_format.jsonl", 'w', encoding="utf8") as file:
    for data in new_openAI_dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')
