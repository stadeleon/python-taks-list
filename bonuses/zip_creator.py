import zipfile
import pathlib


def compress(filepaths, destination_dir):
    with zipfile.ZipFile(pathlib.Path(destination_dir, "compressed.zip"), 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
    return len(archive.infolist())
# if __name__ == "__main__":
#     compress(filepaths=)
