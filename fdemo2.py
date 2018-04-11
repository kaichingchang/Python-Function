import tkinter as tk

def hello(name):
    name.insert(0, "Hello, ")
    name.insert(2, "!")

class FDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("說哈囉")

        self.label = tk.Label(self)
        self.label["text"] = "請輸入暱稱："
        self.label.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "說哈囉"
        self.button["command"] = self.hello
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = ""
        self.result.grid(row=3, column=0, sticky=tk.N+tk.W)

    def hello(self):
        name = [self.entry.get()]
        hello(name)
        s = ""
        for i in name:
            s += i
        self.result["text"] = s



if __name__ == '__main__':
   root = tk.Tk()
   app = FDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：fdemo2.py
# 功能：示範函數的參數
# 作者：張凱慶
