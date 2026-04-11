def encode(message, index):
    if not message:  #enkripton mesazhin duke perdorur indeksin e krijuar nga libri
        return ""    #kontrollon inputin

    message = message.lower().strip()
    words = message.split()

    encoded = []

    for word in words:
        if word in index:
            encoded.append(str(index[word][0]))
        else:
            encoded.append("X")

    return " ".join(encoded)