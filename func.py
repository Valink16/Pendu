from sys import getsizeof, exit
def loadFile(filename):
    """
    :param filename:
    :return: dict: Containing "content" and "size"
    """
    filename="wordList"
    try: #Opening file
        with open(filename,"r") as file:
            fichier=file.read()
            size=getsizeof(fichier)
            return {"content": fichier, "size": size}

    except FileNotFoundError:
      sys.exit(""""{}" doesn't exist.""".format(filename))

def prtDebug(str):
    print("[Debug] "+str)

def createMask(w):
    mask=[]
    for l in range(len(w)):
        mask.append("*")
    return  mask