def read_file(file_path):
    file = open(file_path, 'r')
    data = file.read()
    return data