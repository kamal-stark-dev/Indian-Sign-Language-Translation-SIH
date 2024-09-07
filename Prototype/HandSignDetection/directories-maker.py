import os

base_path = r"C:\Users\91638\Desktop\Projects\Github\Indian-Sign-Language-Translation-SIH\Prototype\HandSignDetection\Signs"

dir_names = ["A", "B", "C"]

for dir_name in dir_names:
  full_path = os.path.join(base_path, dir_name)
  os.makedirs(full_path, exist_ok=True)

print("\nDirectories created succesfully!!\n")