import json
# Abre el archivo en modo lectura
with open('flujos iniciales.txt', 'r') as archivo:
    # Lee el contenido del archivo
    flujos_iniciales = archivo.read()

dataset=[]

flujos_separados = flujos_iniciales.split('\nPREGUNTA TRL\n')



for flujo in flujos_separados:
    messages=[]
    messages.append({"role": "system", "content": "Este es un asistente para la evaluación del TRL."})
    
     
    lines = flujo.split('\n\n')
    
    for line in lines:
        partes = line.split(':')
        
        if partes[0]=="Cliente":
            messages.append({"role": "user", "content": partes[1]})
        if partes[0]=="Asistente":
            messages.append({"role": "assistant", "content": partes[1]})
    
    print(messages)
    
    new_data={"messages": messages}
    dataset.append(new_data)
    
    
    
with open("flujos_openAI_format.jsonl", 'w', encoding="utf8") as file:
    for data in dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')