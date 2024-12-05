from pathlib import Path

path = Path('guest.txt')
name = ''
i = 0
while(name.casefold() != 'quit'):
    name = input("What is your name?  Enter 'quit' to quit: ").strip()
    if(name.casefold() != 'quit' and i == 0):
        contents = f"{name}\n"
    elif(name.casefold() != 'quit' and i != 0):
        contents += f"{name}\n"
    else: break
    i += 1    

path.write_text(contents)