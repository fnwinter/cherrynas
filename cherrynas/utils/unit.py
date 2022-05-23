def HumanReadByte(byte):
    if byte < 1024:
        return f"{byte} bytes"
    elif byte < 1024 ** 2:
        kb = byte / 1024
        return f"{kb:.2f} KB"
    elif byte < 1024 ** 3:
        mb = byte / 1024 ** 2
        return f"{mb:.2f} MB"
    elif byte < 1024 ** 4:
        gb = byte / 1024 ** 3
        return f"{gb:.2f} GB"
    else:
        pb = byte / 1024 ** 4
        return f"{pb:.2f} PB"
