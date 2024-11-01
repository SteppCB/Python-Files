import os

def count_lines_words_in_file(file_path):
    try:
        # Checking if the file exists
        if os.path.exists(file_path):
            # Opening the file in read mode
            with open(file_path, 'r') as file:
                content = file.readlines()
                words = [word for line in content for word in line.split()]
                print(f"Number of lines: {len(content)}")
                print(f"Number of words: {len(words)}")
        else:
            # If the file does not exist, print an error message
            print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
