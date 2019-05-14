import os
import binascii


def find_biggest():

        objects = os.listdir('game_files/nca')

        sofar = 0
        name = ""

        for file in objects:
                size = os.path.getsize(os.path.join('game_files/nca', file))
                if size > sofar:
                        sofar = size
                        name = file
        return name, sofar

def find_tik():
        name = []
        for file in os.listdir("game_files/nca"):
                if file.endswith(".tik"):
                        name = file
        return name

def find_titlekey(tik):
        os.listdir('game_files/nca')
        with open('game_files/nca/' + tik,"rb") as f:
                f.seek(0x180)
                val = f.read(16)
                return binascii.hexlify(bytearray(val))
