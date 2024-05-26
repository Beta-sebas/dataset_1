import json
# Abre el archivo en modo lectura
with open('TRL9FLUJOS.txt', 'r') as archivo:
    # Lee el contenido del archivo
    flujos_iniciales = archivo.read()

dataset=[]

flujos_separados = flujos_iniciales.split('\n---\n')



for flujo in flujos_separados:
    messages=[]
    messages.append({"role": "system", "content": "Este es un asistente especializado en el modelo de Niveles de Madurez Tecnol\u00f3gica (TRL) de la NASA, capaz de evaluar y clasificar tecnolog\u00edas en el campo de la agricultura seg\u00fan los 9 niveles de madurez. Debes tambi\u00e9n responder consultas sobre el TRL, abarcando definiciones, actividades recomendadas y criterios de progresi\u00f3n, actuando como una fuente de conocimiento sobre c\u00f3mo avanzar tecnolog\u00edas desde la concepci\u00f3n hasta la comercializaci\u00f3n."})
    
     
    lines = flujo.split('\n\n')
    
    for line in lines:
        partes = line.split(':')
        
        if partes[0]=="Usuario":
            content = ':'.join(partes[1:])
            messages.append({"role": "user", "content": content.strip()}) #concatenar el resto de partes para que sean incluidas
        if partes[0]=="Asistente":
            content = ':'.join(partes[1:])
            messages.append({"role": "assistant", "content":  content.strip()})  #concatenar el resto de partes para que sean incluidas
    
    print(messages)
    
    new_data={"messages": messages}
    dataset.append(new_data)
    
    
    
with open("TRL9FLUJOS_openai.jsonl", 'w', encoding="utf8") as file:
    for data in dataset:
       json_line = json.dumps(data)
       file.write(json_line + '\n')
