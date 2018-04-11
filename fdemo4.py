import tkinter as tk

class FDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("挑選數字")

        self.label = tk.Label(self)
        self.label["text"] = "1, 7, 13, 19, 25"
        self.label.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "挑選大於10的數字"
        self.button["command"] = self.select
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "結果是"
        self.result.grid(row=3, column=0, sticky=tk.N+tk.W)

    def select(self):
        for i in filter(lambda x: x > 10, [1, 7, 13, 19, 25]):
            self.result["text"] += str(i) + " "

if __name__ == '__main__':
   root = tk.Tk()
   app = FDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：fdemo4.py
# 功能：示範 lambda 運算式
# 作者：張凱慶
