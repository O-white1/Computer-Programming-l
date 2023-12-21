import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(142, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(124, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Circle Radius:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(3, 77)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(143, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Circumpherance:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGray
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(132, 77)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 104)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Circle Area:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkGray
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(132, 104)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(3, 130)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 51)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(56, 187)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 51)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(113, 130)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 51)
		self._button3.TabIndex = 8
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGray
		self.ClientSize = System.Drawing.Size(814, 423)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog_54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""

	def Button1Click(self, sender, e):
		rad = float(self._textBox1.Text)
		pie = 3.14159
		radx2 = rad * 2
		circ = radx2 * pie
		radxrad = rad * rad
		area = radxrad * pie
		self._label5.Text = str(round(area, 3))
		self._label3.Text = str(round(circ, 3))