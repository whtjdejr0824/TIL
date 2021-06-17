from openpyxl.styles import Font
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 번호, 영어, 수학
al = ws["A1"] # 번호
b1 = ws["B1"] # 영어
c1 = ws["C1"] # 수학

# A 열의 너비를 5로 설정
ws.column_dimentions["A"].width = 5

# 1 행의 높이를 50 으로 설정
ws.row_dimentions[1].height = 50

# 스타일 적용
a1.font = Font(color ="FF0000", italic=True, bold=True) # 글자 색은 빨갛게, 이탤릭, 두껍게 적용
b1.font = Font(color="CC33FF", name="Arial", strike=True) # 폰트를 Arial로 설정, 취소선 적용
c1.font = Font(color="0000FF", size=20, underline="single") # 글자 크기를 20, 밑줄 적용


wb.save("sample_style.xlsx")