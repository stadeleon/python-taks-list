import PySimpleGUI as sg

source_label = sg.Text('Select files to compress')
source_input = sg.Input(tooltip='enter path here')
source_location_selector_button = sg.FilesBrowse('Choose')

destination_label = sg.Text('Select destination folder')
destination_input = sg.Input(tooltip='enter path here')
destination_location_selector_button = sg.FolderBrowse('Choose')

status = sg.Text('Compression completed successfully')

button = sg.Button('Compress')
layout = [[source_label, source_input, source_location_selector_button],
          [destination_label, destination_input, destination_location_selector_button],
          [button]]
window = sg.Window('File Zipper', layout=layout)
window.read()
window.close()

