import pyautogui
# file_menu = pyautogui.lacateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.lacateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png")
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.lacateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1488, 760)
# pyautogui.moveTo(trash_icon)
                                      
# pyautogui.mouseInfo()
# 1488, 623
# 1881, 760        
