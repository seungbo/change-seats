import tkinter as tk
import random
from tkinter import *
import tkinter.font
import pyautogui as p
from datetime import datetime
import tkinter.messagebox as msgbox

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("자리 바꾸기")
        self.geometry("400x300+700+210")
        photo=PhotoImage(file='symbol-only.png')
        self.wm_iconphoto(False, photo)
        
        self.frames = {}
        
        # 프레임을 생성
        self.frame1 = Frame1(self)
        self.frames[Frame1] = self.frame1
        
        self.frame2 = Frame2(self)
        self.frames[Frame2] = self.frame2
        
        self.frame3 = Frame3(self)
        self.frames[Frame3] = self.frame3
        
        self.current_frame = None
        self.show_frame(Frame1)

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_class]
        self.current_frame.pack(fill="both", expand=True)

        if frame_class == Frame2:
                    self.geometry("427x650+800+180")            
        elif frame_class == Frame3:
                    self.geometry("935x500+460+210")
        else:
            self.geometry("400x300+700+210")
    a = '없음'


class Frame1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="1-3전용 프로그램입니다.",font=17)
        label.place(x=85, y=15)

        label = tk.Label(self, text="옵션 선택해주세요.")
        label.place(x=10, y=55)

        button = tk.Button(self, text="혼자", command=lambda: master.show_frame(Frame2))
        button.place(x=20, y=100)
        button = tk.Button(self, text="짝꿍", command=lambda: master.show_frame(Frame3))
        button.place(x=80, y=100)




class Frame2(tk.Frame, App):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        font1 = tkinter.font.Font(family='Nanum Pen', size=18)
        font2 = tkinter.font.Font(size=14)
        font3 = tkinter.font.Font(size=11)

        member = ['강승우', '김민경', '김성산', '김승훈', '김찬희', '김채영', '남성호', '류다현', '박세준', '박주은', '이승보', '이승현', '이하랑', '천유찬','천지민', '최해진', '최현우', '최현주', '황기성']
        newmember = []

        seat0 = tk.Label(self, text='칠판', width=8, height=2, relief="solid", font=font2, borderwidth=1)
        seat0.grid(row=0, column=1, sticky=tk.N+tk.E+tk.W+tk.S, columnspan=2, pady=27)

        seat_labels = []
        for i in range(1, 6):
            for j in range(4):
                if i == 5 and j == 3:
                    break
                seat_label = tk.Label(self, text=self.a, width=8, height=2, relief="solid",font=font1, borderwidth=1)
                seat_label.grid(row=i, column=j, sticky=tk.N+tk.E+tk.W+tk.S, padx=3, pady=3)
                seat_labels.append(seat_label)

        def Randomcmd():
            newmember.clear()
            random.shuffle(member)
            random.shuffle(member)
            for i in range(19):
                newmember.append(member[i])
            delay = 500
            for j, seat_label in enumerate(seat_labels):
                master.after(j * delay, update_label, seat_label, j)
        
        def update_label(label, i):
            if sum == 19:
                pass
            label.config(text=newmember[i])

        def Savecmd():
            p.screenshot('자리 배치도.jpg', region=(810,210,425,600))
            msgbox.showinfo('알림', '사진이 저장 되었습니다.')

        def Clock():    
            Time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            clock.config(text=Time)
            clock.after(1000, Clock)

        def Reset():
            for label in seat_labels:
                label.config(text=self.a)

        def Exit():
            master.quit()
        
        clock = tk.Label(self, text='', font=font3)
        clock.place(x=0, y=0)
        Clock()

        Random = tk.Button(self, text='랜덤 돌리기', command=Randomcmd, font=font3)
        Random.place(x=20, y=550)

        reset = tk.Button(self, text='reset', command=Reset, font=font3)
        reset.place(x=140, y=550)

        save = tk.Button(self, text='사진 저장', command=Savecmd, font=font3)
        save.place(x=205, y=550)

        exit = tk.Button(self, text='종료', command=Exit, font=font3)
        exit.place(x=305, y=550)

        button = tk.Button(self, text="홈 가기", command=lambda: master.show_frame(Frame1))
        button.place(x=360, y=550)



class Frame3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        font1 = tkinter.font.Font(family='Nanum Pen', size=18)
        font2 = tkinter.font.Font(size=14)
        font3 = tkinter.font.Font(size=11)

        member = ['강승우', '김민경', '김성산', '김승훈', '김찬희', '김채영', '남성호', '류다현', '박세준', '박주은', '이승보', '이승현', '이하랑', '천유찬','천지민', '최해진', '최현우', '최현주', '황기성']
        newmember = []

        #기본 값
        a = '없음'

        seat1 = tk.Label(self, text='책상', width=13, height=2, relief="solid", font=font2, borderwidth=1)
        seat1.grid(row=0, column=1, sticky=N+E+W+S, pady=13)

        seat_labels = []
        for i in range(1, 4):
            for j in range(3):
                seat_label = tk.Label(self, text=a, width=25, height=2, relief="solid", font=font1, borderwidth=1)
                seat_label.grid(row=i, column=j, sticky=N+E+W+S, padx=3, pady=3)
                seat_labels.append(seat_label)

        #함수
        def Randomcmd():
            sum = 0
            newmember.clear()
            random.shuffle(member)
            random.shuffle(member)
            for i in range(0, 20, 2):
                newmember.append(member[i:i + 2])
            delay = 500
            sum = 0
            for i, label in enumerate(seat_labels):
                sum+=1
                if sum == 8:
                    master.after(i * delay, update_label1, label, i)
                    continue
                master.after(i * delay, update_label, label, i)

        def update_label(label, i):
            label.config(text=newmember[i])
            
        def update_label1(label, i):
            label.config(text=newmember[i]+newmember[-1])

        def Savecmd():
            p.screenshot('자리 배치도.jpg', region=(470,248,935,320))
            msgbox.showinfo('알림', '사진이 저장 되었습니다.')

        def Clock():
            Time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            clock.config(text=Time)
            clock.after(1000, Clock)

        def Reset():
            for label in seat_labels:
                label.config(text=a)

        def Exit():
            master.quit()

        Random = Button(self, text='랜덤 돌리기', command=Randomcmd, font=font3)
        Random.place(x=150, y=360)

        reset = Button(self, text='reset', command=Reset, font=font3)
        reset.place(x=310, y=360)

        save = Button(self, text='사진 저장', command=Savecmd, font=font3)
        save.place(x=410, y=360)

        exit = Button(self, text='종료', command=Exit, font=font3)
        exit.place(x=540, y=360)

        button = tk.Button(self, text="홈 가기", command=lambda: master.show_frame(Frame1))
        button.place(x=630, y=360)

        clock = Label(self, text='', font=font3)
        clock.place(x=0, y=0)
        Clock()

if __name__ == "__main__":
    app = App()
    app.mainloop()