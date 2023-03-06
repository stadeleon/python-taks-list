import PySimpleGUI as sg
import subprocess
from zip_processor import compress, extract

sg.theme("DarkBlue2")
source_label = sg.Text('Select files to compress')
source_extract_label = sg.Text('Select file to extract')
source_input = sg.Input(tooltip='enter path here')
source_extract_input = sg.Input(tooltip='enter path here')
source_location_selector_button = sg.FilesBrowse('Choose to Compress', key='source_files')
source_extract_selector_button = sg.FileBrowse('Choose to Extract', key='source_file')

destination_label = sg.Text('Select destination folder')
destination_input = sg.Input(tooltip='enter path here')
destination_location_selector_button = sg.FolderBrowse('Choose', key='target_location', initial_folder='/Users/leonid.derevianko/Projects/Python/Learning/')

status = sg.Text('', key='status')

compress_button = sg.Button('Compress')
extract_button = sg.Button('Extract')

layout = [[source_label, source_input, source_location_selector_button],
          [source_extract_label, source_extract_input, source_extract_selector_button],
          [destination_label, destination_input, destination_location_selector_button],
          [compress_button], [extract_button], [status]]
window = sg.Window('File Zipper', layout=layout, font=('Helvetica', 15))
while True:
    event, values = window.read()
    # print(event, values)

    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'Compress':
            filesList = values['source_files'].split(';')
            result = compress(filesList, values['target_location'])
            if result:
                window['status'].update(value='Compression completed successfully')
        case 'Extract':
            file_to_extract = values['source_file']
            result = extract(file_to_extract, values['target_location'])
            if len(result['files']):
                window['status'].update(value=f"{len(result['files'])} Files successfully extracted")

            subprocess.run(["/usr/bin/open", f"{result['directory']}"])

window.close()

