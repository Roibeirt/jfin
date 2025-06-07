import os
import re

full_dir = os.listdir(os.getcwd())

for dir in full_dir:
    movie_name = file_type = re.search(r'^(.*)\)[^)]*$', dir).group(1)
    test = input(f'Correct Movie Title (y/n)? {movie_name}')
    # Guard Clause
    if test.capitalize() == "N":
        print("Skipping")
        continue
    movie_dir = os.listdir(f'./{dir}')
    files = []
    for file in movie_dir:
        # I like guard clauses more than indentation
        if os.path.isfile(f'./{dir}/{file}') == False:
            continue
        file_extenstion = re.search(r'\.([^.]+)$', file).group(1)
        # Not handling subs yet
        if file_extenstion == "srt":
            continue
        file_change_record = {"original" : file, "new" : f"{movie_name}.{file_extenstion}"}
        files.append(file_change_record)
    print("Making the following changes: ")
    for file in files:
        print(f'{file['original']} : {file['new']}')
    test = input("Proceed (y/n)? ")
    if test.capitalize() == "N":
        print("Skipping")
        continue
    for file in files:
        os.rename(f'./{dir}/{file["original"]}',f'./{dir}/{file["new"]}')
    os.rename(f'./{dir}', f'./{movie_name}')