import keyboard, pyscreenshot, clipboard, time

def screen():
    global saved
    scr = pyscreenshot.grab(bbox=(0, 0, 800, 520))
    scr.save("Scr_" + str(saved) + '.png')
    print(saved)
    saved += 1

def main():
    global saved
    while not keyboard.is_pressed('ctrl+shift+space'):
        pass
    time.sleep(1)
    keyboard.send('ctrl+a')
    time.sleep(0.1)
    keyboard.send('ctrl+x')
    time.sleep(0.1)
    text = clipboard.paste().split('\n')
    saved = -1
    screen()
    for i in range(len(text)):
        text[i] = str(text[i]).strip('\r')
        if i > 0:
            keyboard.send('enter')
            keyboard.send('home')
            screen()
        for j in range(len(text[i])):
            keyboard.write(text[i][j])
            screen()
    keyboard.send('ctrl+s')
    scr = pyscreenshot.grab(bbox=(0, 0, 1920, 1000))
    scr.save("Scr_" + str(saved) + '.png')

if __name__ == "__main__":
    main()