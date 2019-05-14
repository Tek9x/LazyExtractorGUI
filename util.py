import os
import binascii


def find_biggest():

        objects = os.listdir('output_files')

        sofar = 0
        name = ""

        for file in objects:
                size = os.path.getsize(os.path.join('output_files', file))
                if size > sofar:
                        sofar = size
                        name = file
        return name, sofar

def find_tik():
        name = []
        for file in os.listdir("output_files"):
                if file.endswith(".tik"):
                        name = file
        return name

def find_titlekey(tik):
        os.listdir('output_files')
        with open('output_files/' + tik,"rb") as f:
                f.seek(0x180)
                val = f.read(16)
                return binascii.hexlify(bytearray(val))
