while True:
    editori=input("Editori: ")
    mjono = "Visual Studio CODE"
    if editori.lower() == mjono.lower():
        print("Loistava valinta")
        break
    word="Word"
    note="Notepad"
    if editori.lower() == word.lower() or editori.lower() == note.lower():
        print("surkea")
    else:
        print("ei ole hyvä")
