import os
import shutil

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    else:
        print(f"Directory '{dir_name}' already exists.")

def list_files_and_dirs(path):
    print(f"Contents of '{path}':")
    for item in os.listdir(path):
        print(item)

def create_and_write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' created and content written.")

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(f"Content of '{file_path}':\n{content}")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"File '{old_name}' renamed to '{new_name}'.")

def delete_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' and its contents deleted successfully.")
    else:
        print(f"Directory '{dir_name}' does not exist.")

if __name__ == "__main__":
    dir_name = "new_directory"
    file_name = "sample.txt"
    new_file_name = "renamed_sample.txt"
    file_content = "Hello, this is a test file."
    

    create_directory(dir_name)
    
    list_files_and_dirs(os.getcwd())
 
    file_path = os.path.join(dir_name, file_name)
    create_and_write_file(file_path, file_content)
 
    read_file(file_path)
    
    
    new_file_path = os.path.join(dir_name, new_file_name)
    rename_file(file_path, new_file_path)
    
    
    list_files_and_dirs(dir_name)
    

    delete_directory(dir_name)
