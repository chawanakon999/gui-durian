#writefile.py
from datetime import datetime


def writetext (quantity,total):
	#THAI DATE
	stamp = datetime.now() 
	stamp = stamp.replace(year=stamp.year+543) # Adding 543 is B.E.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	# 3 line:These are functions for saving into txt.
	filename = 'data.txt' 
	with open(filename,'a',encoding='utf-8') as file: # encoding='utf-8' เพื่อบันทึกเป็นภาษาไทย
		file.write('\n'+'วัน-เวลา :{} ทุเรียน: {} กิโลกรัม ราคาทั้งหมด : {:,.2f} บาท '.format(stamp,quantity,total)) 
		#This ‘\n’ is going up a new line.Then is saved.


#writetext(90,9000)
#writetext(91,9100)
#writetext(92,9200)
