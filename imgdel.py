from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import os
def func(count):
#checks whether there is a duplicate
	image=e1.get()
	folder=e2.get()
	included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
	try:
		mylist = [fn for fn in os.listdir(folder) if any(fn.endswith(ext) for ext in included_extensions)]
		#gets the image filenames in the path entered in the text field
	except:
		l3=Label(master,text="Folder not found",fg="red").grid(row=3)#if folder name is not found
	a=plt.imread(image)
	print(mylist)
	for img in mylist:
		b=plt.imread(os.path.join(folder,img))
		if  np.array_equal(a,b):
			delete_file(folder,img)
			count=1
	if count==1:
		l3=Label(master,text="Image Deleted").grid(row=3)
	else:
		l3=Label(master,text="No duplicate image found").grid(row=3)			
def delete_file(folder,img):#for deleting the file
	fullpath = os.path.join(folder,img)
	os.remove(fullpath)
if __name__ == "__main__":
	count=0
	master=Tk()
	master.title("Duplicate Image Finder")
	l1=Label(master,text="Image Name").grid(row=0)
	l2=Label(master,text="Folder Path").grid(row=1)
	l3=Label(master,text="").grid(row=3)
	e1=Entry(master,width=40)
	e1.grid(row=0,column=1)
	e2=Entry(master,width=40)
	e2.grid(row=1,column=1)
	button1=Button(master,text="Check",command=lambda:func(count),height=1,width=7)
	button1.grid(row=2,column=1)
	mainloop()
	