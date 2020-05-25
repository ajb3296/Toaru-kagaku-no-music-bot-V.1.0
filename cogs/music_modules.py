
async def volumeicon(vol : int):
    if vol >= 1 and vol <= 300:
        volicon = ":speaker:"
    elif vol >= 301 and vol <= 600:
        volicon = ":sound:"
    else:
        volicon = ":loud_sound:"
    return volicon