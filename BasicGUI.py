#BasicGUI.py

from tkinter import * #เป็นการ import  package ที่เป็นตัวหลัก
from tkinter import ttk, messagebox #package ย่อย
from datetime import datetime
import csv
#################################################
def timestamp(thai=True):
	if thai == True:
		#THAI DATE
		stamp = datetime.now() 
		stamp = stamp.replace(year=stamp.year+543) # Adding 543 is B.E.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #date-time
	return stamp

def writetext (quantity,total):
	#THAI DATE
	# stamp = datetime.now() 
	# stamp = stamp.replace(year=stamp.year+543) # Adding 543 is B.E.
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	# 3 line:These are functions for saving into txt.
	stamp = timestamp()
	filename = 'data.txt' 
	with open(filename,'a',encoding='utf-8') as file: # encoding='utf-8' เพื่อบันทึกเป็นภาษาไทย
		file.write('\n'+'วัน-เวลา :{} ทุเรียน: {} กิโลกรัม ราคาทั้งหมด : {:,.2f} บาท '.format(stamp,quantity,total)) 
		#This ‘\n’ is going up a new line.Then is saved.
######################################################

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data
###########################################
def sumdata():
	# ฟังชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก CSV ไฟล์สรุปออกมาเป็น 2 อย่าง
	result = readcsv()
	# print(result)
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return(sumquan,sumtotal)



GUI = Tk()
GUI.geometry('600x600')  #ปรับขนาด GUI #เครื่องหมายคูณจะใช้ x ตัวเล็ก # 500 = แนวตั้ง 300 = แนวนอน
GUI.title('โปรแกรมสำหรับแม่ค้าทุเรียน v.0.0.1')

file =PhotoImage(file='') #ใส่รูป
IMG= Label(GUI,image=file,text='')
IMG.pack()


L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('TH SarabunPSK',30,'bold'),fg="red")
L1.pack() # .place(x,y) ใส่ location , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน (กิโลกรัม)',font=('TH SarabunPSK',20))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('TH SarabunPSK',20,"bold")) #ดึง entry จากไฟล์ ttk 
E1.pack()

def Calculate(event=None):
	quantity = v_quantity.get()
	price = 100
	print('จำนวน',float(quantity) * price)
	cal = float(quantity) * price
	# ENG DATE
	# stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #date-time

	# writetext(quantity,cal)
	data = [timestamp(),quantity,cal]
	writecsv(data)


	# pop up
	
	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('')  #clear data
	E1.focus()


B1 = ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20) 

E1.bind('<Return>',Calculate)

def SummaryData(event):
	#pop up 
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = 'จำนวนที่ขายได้ทั้งหมด: {} กิโลกรัม\nยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1]) # \n ขึ้นบรรทัดใหม่
	messagebox.showinfo(title,text)


GUI.bind('<F1>',SummaryData) #เป็นการตรวจสอบว่ามีการกดอะไรบ้าง
GUI.bind('<F2>',SummaryData)

E1.focus()  #ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()  #mainloop มีไว้เพื่อให้ software run ตลอดเวลา 

