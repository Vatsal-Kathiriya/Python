import os

files = os.listdir("C:\\Users\\vatsa\\OneDrive\\Pictures\\Screenshots\\COA")

j = 1

for file in files:
    if file.endswith(").png"):
      i = f"Screenshot ({int(j)}).png"
      print(file)
      print(i)
      print(j)
      os.rename(f"C:\\Users\\vatsa\\OneDrive\\Pictures\\Screenshots\\COA\\{file}", f"C:\\Users\\vatsa\\OneDrive\\Pictures\\Screenshots\\COA\\{i}")
      j = j + 1
      