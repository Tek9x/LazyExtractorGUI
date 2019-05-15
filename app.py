import PySimpleGUI27 as sg
import subprocess
import util
from os import remove


menu_def = [['[F]ile', ['Extract',['NSP', 'XCI']]],['[M]isc', 'About']]

layout = [[sg.MenuBar(menu_def), sg.Output(size=(60, 5), background_color='Black',text_color='Green', font='None')]]

window = sg.Window('LazyExtractor [Alpha]').Layout(layout)

while True:
    event, value = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'NSP':
        filename = sg.PopupGetFile('Open File', no_window=True, file_types=(("Switch File Types", "*.nsp"),))
        if filename is not '':
            print 'Extracting NSP:'
            window.Refresh()
            print subprocess.check_output(['squirrel', '-ogame_files/nca','--NSP_copy_nca', '%s' % filename])
            window.Refresh()
            subprocess.check_output(['squirrel', '-ogame_files/nca', '--NSP_copy_ticket', '%s' % filename])
            subprocess.check_output(['squirrel', '-ogame_files/nca', '--NSP_copy_xml', '%s' % filename])
            window.Refresh()
            print 'DONE!'
            window.Refresh()
            print 'Checking for Title Key File...'
            keyfile = util.find_tik()
            window.Refresh()
            print 'Grabbing title key for you...'
            window.Refresh()
            key = util.find_titlekey(keyfile)
            print 'title key found: %s' % key
            window.Refresh()
            print 'Searching for Xml File...'
            if not util.xml_check():
                print 'No XML file found, Trying Biggest NCA File'
                print 'Finding Biggest NCA file...'
                window.Refresh()
                ncafile = util.find_biggest()[0]
                print 'Found Biggest: %s' % ncafile
                print 'Extracting NCA file, PLEASE WAIT..May look like its doing nothing..'
                window.Refresh()
                print subprocess.check_output(['hactool','-k keys.txt', '--titlekey=%s' % key, '-t', 'nca', '--romfsdir=game_files/romfs', '--exefsdir=game_files/exefs', 'game_files/nca/%s' % ncafile])
                print 'Thanks for waiting, check game_files directory.'
            else:
                print 'Parsing NSP XML file...'
                xmlnca = util.xml_check()
                print 'Extracting NCA file, PLEASE WAIT..May look like its doing nothing..'
                print subprocess.check_output(
                    ['hactool', '-k keys.txt', '--titlekey=%s' % key, '-t', 'nca', '--romfsdir=game_files/romfs',
                     '--exefsdir=game_files/exefs', 'game_files/nca/%s' % xmlnca])
                print 'Thanks for waiting, check game_files directory.'



        else:
            print ''
    if event == 'XCI':
        filename = sg.PopupGetFile('Open File', no_window=True, file_types=(("Switch File Types", "*.xci"),))
        subprocess.check_output(['hactool', '-k keys.txt', '-t', 'xci', '--outdir=game_files', '%s' % filename])
        ncafile = util.find_biggest()
        subprocess.check_output(['hactool', '-k keys.txt', '-t', 'xci', '--romfsdir=game_files/romfs','--exefsdir=game_files/exefs', '%s' % ncafile])



    if event == 'About':
        print 'LazyExtracter\n version: 0.2A\n Description: Allows the extraction of NSP and XCI Nintendo Switch files'




