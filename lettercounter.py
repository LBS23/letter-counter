def letterCounter(words):
    letterdict = dict()
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter in letterdict.keys():
                    letterdict[letter] += 1
                else:
                    letterdict[letter] = letterdict.get(letter, 0) +1
    return letterdict


def languageSetter():
    while True:
        language = input("Enter the language of the file / Ingresa el lenguaje del archivo: ES (Español) / EN (English): ")
        if language.upper() == 'ES' or language.upper() == 'EN':
            break
        else:
            print("Invalid input, try again / Ingreso invalido, intente de nuevo")
            continue

    return language.upper()


def fileReader():
    while True:
        filename = input("Enter the name of the text / Ingrese el nombre del texto: ")
        try:
            with open(filename, encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Couldn't find the file {filename} try again / No se pudo encontrar el archivo llamado {filename} Intente de nuevo")
        except UnicodeDecodeError:
            print(f"The file {filename} is not encoded in UTF-8, try again / El archivo {filename} no esta codificado en UTF-8 Intente de nuevo")


def wordSplitter(sentence):
    return sentence.split()


def main():
    languageSetter()
    filecontent = fileReader()
    sentences = wordSplitter(filecontent)
    letters = letterCounter(sentences)
    sortedLetters = dict(sorted(letters.items(), key=lambda item:item[1], reverse=True))
    print(sortedLetters)
    return None


main()
