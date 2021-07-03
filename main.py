from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developer By Faruq")
        # resige na korar jonno window
        self.root.resizable(False, False)
        # akhon opore title baNABO

        # ata nichi likha k middle e rakhbo anchor='w'

        title = Label(self.root, text="    Qr Code Generator", font=(
            "times new roman", 40), bg='#ff6666', fg='white', anchor='w').place(x=0, y=0, relwidth=1)

        # akhon3 no work employee detail er window banabo

        # ==========Employee Details window=========

        # ata korlam jokon last 4 no work pore=======Variables========#ata holo info generate er jonno data fatch kora jonno.
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()
        # 4 no ai 4 variable k entry field e assign korbo

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Frame.place(x=50, y=100, width=500, height=380)

        emp_title = Label(emp_Frame, text="Employee Details", font=(
            "goudy old style", 20), bg='#ff4d4d', fg='white').place(x=0, y=0, relwidth=1)

        # box er vitore coto box
        lbl_emp_code = Label(emp_Frame, text="Employee ID", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=20, y=60)
        lbl_name = Label(emp_Frame, text="Employee Name", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=20, y=100)
        lbl_department = Label(emp_Frame, text="Emp Department", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=20, y=140)
        lbl_designation = Label(emp_Frame, text="Emp Designation", font=(
            "times new roman", 15, 'bold'), bg='white').place(x=20, y=180)

        # text field er jonno
        txt_emp_code = Entry(emp_Frame, font=(
            "times new roman", 15), textvariable=self.var_emp_code, bg='#ffcccc').place(x=200, y=60)
        txt_name = Entry(emp_Frame, font=(
            "times new roman", 15), textvariable=self.var_name, bg='#ffcccc').place(x=200, y=100)
        txt_department = Entry(emp_Frame, font=(
            "times new roman", 15), textvariable=self.var_department, bg='#ffcccc').place(x=200, y=140)
        txt_designation = Entry(emp_Frame, font=(
            "times new roman", 15), textvariable=self.var_designation, bg='#ffcccc').place(x=200, y=180)

        # akhon 2 button banabo
        btn_generate = Button(emp_Frame, text='Qr Generate', command=self.generate, font=(
            'times new roman', 18, 'bold'), bg='#330000', fg='white').place(x=90, y=250, width=180, height=30)
        btn_clear = Button(emp_Frame, text='Clear', command=self.clear, font=(
            'times new roman', 18, 'bold'), bg='#800000', fg='white').place(x=282, y=250, width=120, height=30)

        # nice error message show koranor jonno
        self.msg = ''
        self.lbl_msg = Label(emp_Frame, text=self.msg, font=(
            "times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=305, relwidth=1)

        # Employee qr code er jonno box banabo.

        # ==========Employee QR COde window=========
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        qr_title = Label(qr_Frame, text="Employee QR Code", font=(
            "goudy old style", 20), bg='#ff4d4d', fg='white').place(x=0, y=0, relwidth=1)

        # image show koranor jonno

        self.qr_code = Label(qr_Frame, text='No Qr\nAvaible', font=(
            'times new roman', 15), bg='#ffb3b3', fg='white', bd=1, relief=RIDGE)
        # atake place korbo
        self.qr_code.place(x=35, y=100, width=180, height=180)

    # clear er kaj
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        # qr clear
        self.qr_code.config(image='')

        ########4 no work akhane theke ja ja info dibo ta qr code e generate hbe####

    def generate(self):
        # variable entry te add korar pore akhane variable assign kore dekhbo pass kore dekhbo data fatch hosse kina.
        if self.var_designation.get() == '' or self.var_emp_code.get() == '' or self.var_department.get() == '' or self.var_name.get() == '':
            self.msg = 'All Fields are Required!!!'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            ###5 no work qr code import korar por akhane qr bananor kaj korbo_###
            #=======updating Notification=====+#
            qr_data = (
                f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation:{self.var_designation.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            #import resize korar por#
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            #image save korar jonno#
            qr_code.save("Employee_QR/EMP_" +
                         str(self.var_emp_code.get())+'.png')
            #qr code hoa gelo akhan akhon run korle image dekhabe seta dekhbo###
            #============qr code image update=============== tar jonno pillow library install kora lagbe=====#
            # install korar por
            self.im = ImageTk.PhotoImage(file="Employee_QR/EMP_" +
                                         str(self.var_emp_code.get())+'.png')
            # akhon qr k lagabo image file e tai opore ***self.qr_code*** ata korecilam ata lagabo
            self.qr_code.config(image=self.im)

            self.msg = 'QR Generate Successfully!!!!'
            self.lbl_msg.config(text=self.msg, fg='green')
    # tar por opore generate ke call korbo 42 no line e----
    # variable entry te add korar pore akhane variable assign kore dekhbo pass kore dekhbo data fatch hosse kina.

    ########______5no work________akhane qr bananor kaj korbo____________#######


# image resize korar jonno ****python-resize-image******* karon jokon image save korecilam run kore oita onk boro dekhascilo tai coto korar jonno ata

root = Tk()
obj = Qr_Generator(root)  # obj k call korbe
root.mainloop()  # widow off na hobar jonno

# work 2 title,width,height,center e set korar jonno
