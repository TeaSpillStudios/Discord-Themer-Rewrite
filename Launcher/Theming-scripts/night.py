import pyperclip, pyautogui, time, os

time.sleep(3)

isUnix = False

if os.name == "posix":
    isUnix = True

if isUnix:
    themeFile = open("Theming-files/night.txt", 'r', encoding="ISO-8859-1").read()
else:
    themeFile = open("Theming-files\\night.txt", 'r', encoding="mcbs").read()

pyperclip.copy(themeFile)

if isUnix:

    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts/Discord.png"))

    pyautogui.hotkey("ctrl", "shift", "i")

    time.sleep(3)

    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts/Sources.png"))
    time.sleep(3)
    pyautogui.doubleClick(pyautogui.locateCenterOnScreen("Theming-scripts/assets.png"))
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts/CSSfile.png", confidence=0.75))
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts/Line1.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts/Line1144.png"))
    pyautogui.hotkey("ctrl", "a")
    time.sleep(3)
    pyautogui.press("right")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    pyautogui.hotkey("ctrl", "shift", "i")
else:

    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts\\Discord.png"))

    pyautogui.hotkey("ctrl", "shift", "i")

    time.sleep(3)

    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts\\Sources.png"))
    time.sleep(3)
    pyautogui.doubleClick(pyautogui.locateCenterOnScreen("Theming-scripts\\assets.png"))
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts\\CSSfile.png", confidence=0.75))
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts\\Line1.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen("Theming-scripts\\Line1144.png"))
    pyautogui.hotkey("ctrl", "a")
    time.sleep(3)
    pyautogui.press("right")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    pyautogui.hotkey("ctrl", "shift", "i")
