Extension={"abc.py":"python",
           "abc.c":"C program file",
           "abc.exe":"Executable file",
           "abc.fla":"Adobe flsh file",
           "abc.ico":"Icon file",
           "abc.gif":"GIF graphics file",
           "abc.jpg":"JPEG graphics file",
           "abc.img":"Bitmap graphic",
           "abc.html":"Web page file-HTML"}
x=Extension.get(input("Enter the file name :"))
print("The extension of the file is :")
print(x)
