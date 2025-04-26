import os
import shutil

folders = {
    'scripts': ['.py'],
    'dados': ['.csv', '.json'],
    'config': ['.gitignore', 'readme.md']
}

project_dir = os.getcwd()

def create_folder(folder_name):
    folder_path = os.path.join(project_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file(file_path, folder_name):
    dest_folder = os.path.join(project_dir, folder_name)
    shutil.move(file_path, dest_folder)

def organize_files():
    for folder, extensions in folders.items():
        create_folder(folder)  # Cria a pasta para cada tipo de arquivo

        for file_name in os.listdir(project_dir):
            file_path = os.path.join(project_dir, file_name)

            if os.path.isdir(file_path):
                continue  # Ignorar diretórios

            # Verificar se o arquivo corresponde a algum tipo de extensão
            if any(file_name.endswith(ext) for ext in extensions):
                move_file(file_path, folder)
                print(f'Movendo {file_name} para a pasta {folder}')

if __name__ == "__main__":
    organize_files()