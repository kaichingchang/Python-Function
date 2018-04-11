import tkinter as tk

def do_nothing():
    pass

class FDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("函數物件")

        self.button = tk.Button(self)
        self.button["text"] = "測試"
        self.button["command"] = self.test
        self.button.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.result = tk.Text(self)
        self.result["width"] = 60
        self.result["height"] = 10
        self.result.grid(row=2, column=0, sticky=tk.N+tk.W)

    def test(self):
        self.result.delete(1.0, tk.END)
        self.result.insert(tk.INSERT, str(type(do_nothing)) + "\n")
        self.result.insert(tk.INSERT, str(dir(do_nothing)) + "\n")

if __name__ == '__main__':
   root = tk.Tk()
   app = FDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：fdemo1.py
# 功能：示範函數定義
# 作者：張凱慶
