def number_files(dir_path):
    """
    Numbers all files in an arbitrary directory
    starting from zero. Retains extensions.
    """
    files = os.listdir(dir_path)

    for index in range(len(files)):

        current_file_name = files[index]
        current_file_root = current_file_name.split('.')[0]
        file_ext          = current_file_name.split('.')[1]
        
        desired_file_name = current_file_root + str(index) + '.' + file_ext

        current_path      = os.path.join(dir_path, current_file_name)
        desired_path      = os.path.join(dir_path, desired_file_name)
        
        os.rename(current_path, desired_path)
        print(current_path, '=>', desired_path)

number_files(sys.argv[1])
