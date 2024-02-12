import json

with open("amadeus_TRL_CONCEPTUAL_DATASET.jsonl", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
    
def show_dataset():
        
        print(json.dumps(dataset, indent=2))
      
        
def modify_system_job():
    
    new_system_job = "INSERT HERE NEW SYSTEM JOB"
    new_jsonl_name = "dataset_01_modified.jsonl"
    
    for data in dataset:
        data["messages"][0]["content"] = new_system_job
    
    with open(new_jsonl_name, 'w', encoding="utf8") as file:
        for data in dataset:
            json_line = json.dumps(data)
            file.write(json_line + '\n')


       
modify_system_job()
show_dataset()