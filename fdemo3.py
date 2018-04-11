import tkinter as tk

def hello(name):
    return "Hello, " + name + "!"

class FDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("說哈囉2")

        self.label = tk.Label(self)
        self.label["text"] = "請輸入暱稱："
        self.label.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "說哈囉2"
        self.button["command"] = self.hello
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = ""
        self.result.grid(row=3, column=0, sticky=tk.N+tk.W)

    def hello(self):
        self.result["text"] = hello(self.entry.get())

if __name__ == '__main__':
   root = tk.Tk()
   app = FDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：fdemo3.py
# 功能：示範函數的回傳值
# 作者：張凱慶
