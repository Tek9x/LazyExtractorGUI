import PySimpleGUI27 as sg
import subprocess
import util


menu_def = [['[F]ile', ['Extract']],['[A]bout']]

layout = [[sg.MenuBar(menu_def), sg.Output(size=(60, 5), background_color='Black',text_color='Green', font='None')]]

window = sg.Window('LazyExtractor [Final]').Layout(layout)

while True:
    event, value = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Extract':
        filename = sg.PopupGetFile('Open File', no_window=True, file_types=(("Switch File Types", "*.nsp"),))
        if filename is not '':
            print 'Extracting NCA:'
            print subprocess.check_output(['squirrel', '-ooutput_files','--NSP_copy_nca', '%s' % filename])
            subprocess.check_output(['squirrel', '-ooutput_files', '--NSP_copy_ticket', '%s' % filename])
            print 'DONE!'
            print 'Checking for Title Key File...'
            keyfile = util.find_tik()
            print 'Grabbing title key for you...'
            key = util.find_titlekey(keyfile)
            print 'title key found: %s' % key
            print 'Finding Biggest NCA file...'
            ncafile = util.find_biggest()[0]
            print 'Found Biggest: %s' % ncafile
        else:
            print ''




