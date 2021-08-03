import pyautogui
# pyautogui.FAILSAFE = False # 사용 비추천
# pyautogui.mouseInfo()
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용 
# 64,15, 204,179,144 #CCB390

for i in range(10):
  pyautogui.move(100, 100)
  pyautogui.sleep(1)
