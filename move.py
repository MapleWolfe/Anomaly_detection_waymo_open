import shutil
import os

# Define the paths - and move the 
source_file = os.path.expanduser("/Users/ning/Desktop/detected.png") 
destination_folder = os.path.expanduser("/Users/ning/Desktop/demo/staticFiles/uploads/")  

# Create the destination folder if it doesn't exist, if exists then remove the file with same name
os.makedirs(destination_folder, exist_ok=True)
destination_file = os.path.join(destination_folder, os.path.basename(source_file))

# Move the file
shutil.move(source_file, destination_folder)
#if os.path.exists(destination_file):
    #os.remove(destination_file)
print("File moved successfully.") 
 