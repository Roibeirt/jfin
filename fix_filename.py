import os
import re
import sys

file_list = os.listdir(os.getcwd())

regex_list = [r'S\d+E\d+',
              r'Season \d+ Episode \d+']

def main():

    show_name = input("Show Name: ")

    first_run = True

    for file in file_list:
        file_type = re.search(r'\.(.+)$', file).group(1)
        for regex_index in range(len(regex_list)):
            match = re.search(regex_list[regex_index], file)
            if match:
                ep_se = handle_match(regex_index, file)
                new_filename = f'Sample file name: {show_name} S{ep_se['season']:02}E{ep_se['episode']:02}.{file_type}'
                if first_run == True:
                    print(f'Sample file name: {new_filename}')
                    proceed = input('Is this correct? Y to proceed, N to cancel ')
                    consent = False
                    while consent == False:
                        if (proceed.lower() == 'y'): consent = True
                        elif (proceed.lower() == 'n'): sys.exit(0)
                        else: proceed = input('Is this correct? Y to proceed, N to cancel')
                    first_run = False
                os.rename(file, new_filename)


def handle_match(regex_index, file_name):
    if regex_index == 0:
        season = re.search(r'S(\d+)', file_name).group(1)
        episode = re.search(r'E(\d+)', file_name).group(1)
        return({'season':season, 'episode':episode})
    if regex_index == 1:
        season = re.search(r'Season (\d+)', file_name).group(1)
        episode = re.search(r'Episode (\d+)', file_name).group(1)
        return({'season':season, 'episode':episode})


if __name__ == "__main__":
    main()