import os 
from pdf2image import convert_from_path

# Caminho que estão os PDF's, neste mesmo caminho serão salvo os pdf's, importante que seja uma pasta separada para não confundir
diretorio = "C:\\meu_diretorio\\" 

dirs = os.listdir(diretorio)

for file in dirs:
    file_path = os.path.join(diretorio, file)
    
    if file.lower().endswith(".pdf"):
        print(f"Convertendo: {file_path}")
        
        folder_name = os.path.splitext(file)[0]
        folder_path = os.path.join(diretorio, folder_name)
        
        os.makedirs(folder_path, exist_ok=True)
        
        images = convert_from_path(file_path)
        
        for i, image in enumerate(images, start=1):
            output_path = os.path.join(folder_path, f"{folder_name}-pagina-{i}.jpg")
            image.save(output_path, "JPEG")
            
        print(f"PDF convertido e salvo em: {folder_path}\n")

print("Todos os arquivos foram convertidos!")