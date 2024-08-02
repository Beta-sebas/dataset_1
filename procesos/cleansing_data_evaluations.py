import json

filename="evaluation_fase_dataset_temp0.1.json"

with open(filename+"l", encoding="utf-8") as f:
    dataset = [json.loads(line) for line in f]
    
def clean_llama_unnecessary(dataset):
    
  
    for i in range(len(dataset)):
        
        print("---------------------------------------------------")
        print("ANTES:")
        print(dataset[i]["generado_llama_2"])
        
        #partición
        partes=dataset[i]["generado_llama_2"].split("\n\n")
        
        #asignación
        dataset[i]["generado_llama_2"] = partes[0]
        
        
        print("DESPUES:")
        print(dataset[i]["generado_llama_2"])
        


clean_llama_unnecessary(dataset)

with open(filename, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)    