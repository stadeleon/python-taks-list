import PySimpleGUI as sg
from zip_processor import compress

source_label = sg.Text('Select files to compress')
source_input = sg.Input(tooltip='enter path here')
source_location_selector_button = sg.FilesBrowse('Choose', key='source_files')

destination_label = sg.Text('Select destination folder')
destination_input = sg.Input(tooltip='enter path here')
destination_location_selector_button = sg.FolderBrowse('Choose', key='target_location')

status = sg.Text('', key='status')

button = sg.Button('Compress')
layout = [[source_label, source_input, source_location_selector_button],
          [destination_label, destination_input, destination_location_selector_button],
          [button], [status]]
window = sg.Window('File Zipper', layout=layout)
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


window.close()

