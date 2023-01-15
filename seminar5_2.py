from itertools import groupby
from os import path


def create_file_decompress(decompress_str):
    with open('decompress.txt', 'w') as data:
        data.write("".join(decompress_str))


def create_file_compress(compress_str):
    with open('compress.txt', 'w') as data:
        data.write("".join(compress_str))


def compress(my_str):
    compress_list = "".join([f"{len(list(j))}{i}" for i, j in groupby(my_str)])
    return compress_list


def decompress(file_name):
    with open(file_name, "r") as file:
        if path.exists(file_name):
            data = file.read()
            print(f"Compressed data from a file {data}")
            decoded_str = ''
            count = ''
            for char in data:
                if char.isdigit():
                    count += char
                else:
                    if not count:
                        decoded_str += char
                    else:
                        decoded_str += int(count)*char
                        count = ''
        else:
            print(f"No such file was found")
    return decoded_str


new_list = list(input("Enter the string to compress: "))
create_file_decompress(new_list)
compress_data = compress(new_list)
create_file_compress(compress_data)
print(f'Decompress data {"".join(new_list)}')
print(f"Compress data {compress_data}")
decoded_string = decompress('compress.txt')
print(decoded_string)
