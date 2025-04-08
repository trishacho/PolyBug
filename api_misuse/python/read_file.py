def read_file_buggy(file_obj):
    """Buggy version that doesn't close the file."""
    file = file_obj  # no with statement, so it won't close automatically
    data = file.read()
    return data

def read_file_fixed(file_obj):
    """Fixed version that closes the file properly."""
    try:
        with file_obj as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None