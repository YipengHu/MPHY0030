import zipfile
import os
import shutil

# extract zipped file
zip_file_path = r'./group_exercise_materials.zip'
extract_to_file_path = r'./'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_file_path)

file_extensions_dict = {
    'audio': ['aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma'],
    'compressed': ['7z', 'deb' , 'pkg', 'rar' , 'rpm' , 'z' , 'zip', 'gz'],
    'code': ['js', 'jsp', 'html', 'ipynb', 'py', 'java', 'css'],
    'documents': ['ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'doc', 'docx', 'txt', 'tex', 'odt'],
    'images': ['bmp' , 'gif' 'ico' , 'jpeg', 'jpg', 'png', 'svg', 'tif', 'tiff'],
    'videos': ['avi', 'flv', 'h264', 'mkv' , 'mov', 'mp4', 'mpg', 'mpeg', 'wmv', 'webm']
    }

# function to show all files in folder
path = r'./group_exercise_materials'
os.listdir(path)

# function to create new folder
# my_new_folder_path = r'./my_new_folder'
# os.mkdir(my_new_folder_path)
# os.rmdir(my_new_folder_path)

# function to join halves of paths
# full_path = os.path.join(['abc/def', 'ghi/jkl'])

# function to move file
# file_path = r'my_file.zip'
# move_to = r'my_folder/my_file.zip'
# shutil.move(file_path, move_to)

declutter_path = r'group_exercise_materials'

# get only files
files = [elem for elem in os.listdir(declutter_path) if os.path.isfile(os.path.join(declutter_path, elem))]

# make folders if they do not exist
folder_names = list(file_extensions_dict.keys()) + ['others']
for folder_name in folder_names:
    if not os.path.exists(os.path.join(declutter_path, folder_name)):
        os.mkdir(os.path.join(declutter_path, folder_name))

for file in files:
    
    # get file extension    
    file_extension = file.split('.')[-1]
    
    # pick which folder to add the file to
    try:
        for folder_name in folder_names:
            if file_extension in file_extensions_dict[folder_name]:
                break
    except KeyError:
            folder_name = folder_names[-1]
    
    # move the file
    file_path = os.path.join(declutter_path, file)
    move_to = os.path.join(declutter_path, folder_name, file)
    
    shutil.move(file_path, move_to)

