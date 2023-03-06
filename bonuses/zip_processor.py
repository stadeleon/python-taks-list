import zipfile
import pathlib


def compress(filepaths, destination_dir):
    with zipfile.ZipFile(pathlib.Path(destination_dir, "compressed.zip"), 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
    return len(archive.infolist())


def extract(extract_filename, destination_dir=''):
    extracted_file_names = {'files': [], 'directory': ''}
    with zipfile.ZipFile(pathlib.Path(extract_filename), 'r') as archive:
        destination = pathlib.Path(destination_dir).joinpath(pathlib.Path(extract_filename).stem)
        extracted_file_names['directory'] = destination
        # archive.extractall(destination)
        filelist = archive.filelist

        for file in filelist:
            extracted_file_names['files'].append(archive.extract(file, destination))

    return extracted_file_names

# if __name__ == "__main__":
#     compress(filepaths='')

# if __name__ == "__main__":
#     extract('filename.zip, /Users/username/target/path')
