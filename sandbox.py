
from tkinter.constants import N


numberCode = "000"
temp = list(numberCode)
temp[1] = "1"
numberCode = "".join(temp)
print(numberCode)