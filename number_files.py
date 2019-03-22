def number_files(dir_path):
    """
    Numbers all files in a directory starting
    from zero. Retains extensions.
    """
    files = os.listdir(dir_path)

    for index in range(len(files)):

        file_name = files[index]
        file_root = file_name.split('.')[0]
        file_ext  = file_name.split('.')[1]

        current_path = os.path.join(dir_path,
                file_name)
        desired_path = os.path.join(dir_path,
                file_root  +\
                str(index) +\
                '.'        +\
                file_ext)

        os.rename(current_path, desired_path)
        print(current_path, '=>', desired_path)

number_files(sys.argv[1])
