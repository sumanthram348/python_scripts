import os

req_path = input("Enter your directory path:")
if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. please pass only directory path")
else:
    all_f_ds = os.listdir(req_path)
    if len(all_f_ds) == 0:
        print(f"The given path {req_path} is a empty path")
    else:
        reg_ex = input("Enter the required extension .py/.sh/.txt:")
        req_files = []
        for each_f in all_f_ds:
            if each_f.endswith(reg_ex):
                req_files.append(each_f)
        if len(req_files) == 0:
            print(f"There are no {reg_ex} file in the location of {req_path}")
        else:
            print(f"There are {len(req_files)} files in the location of {req_path} with extension of {reg_ex}")
            print(f"So, the files are:{req_files}")
