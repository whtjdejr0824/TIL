import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
print(fw.title) # 창의 제목 정보
print(fw.size) # 창의 크기 정보 (width, height)
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
pyautogui.click(fw.left + 25, fw.top + 20)

for w in pyautogui.getAllWindows():
  print(w) # 모든 윈도우 가져오기
