class FilesParser:

    def make_list_with_metadata_path(self, path):
        with open(path, encoding='utf-8') as f:
            strings = f.readlines()
        return [path.split('/')[-1], len(strings)] + [el.strip() for el in strings]       

if __name__ == '__main__':
    file_class = FilesParser()
    list_of_paths = ['text1.txt', 'text2.txt', 'text3.txt']
    list_of_files = []
    for path in list_of_paths:
        file = file_class.make_list_with_metadata_path(path)
        list_of_files.append(file)
    list_of_files = sorted(list_of_files, key=lambda file: file[1])
    for file in list_of_files:
        print(*file, sep='\n')
