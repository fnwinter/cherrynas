# Copyright 2022 fnwinter@gmail.com

def HumanReadByte(byte):
    if byte < 1024:
        return f"{byte} bytes"
    if byte < 1024 ** 2:
        kb = byte / 1024
        return f"{kb:.2f} KB"
    if byte < 1024 ** 3:
        mb = byte / 1024 ** 2
        return f"{mb:.2f} MB"
    if byte < 1024 ** 4:
        gb = byte / 1024 ** 3
        return f"{gb:.2f} GB"
    pb = byte / 1024 ** 4
    return f"{pb:.2f} PB"
