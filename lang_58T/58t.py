import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(150, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "Dollars:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Red
		self._label2.Location = System.Drawing.Point(12, 51)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(150, 42)
		self._label2.TabIndex = 1
		self._label2.Text = "Quarters:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Red
		self._label3.Location = System.Drawing.Point(12, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 42)
		self._label3.TabIndex = 2
		self._label3.Text = "Dimes:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Black
		self._label4.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Red
		self._label4.Location = System.Drawing.Point(12, 135)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(150, 42)
		self._label4.TabIndex = 3
		self._label4.Text = "Nickles:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Black
		self._label5.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Red
		self._label5.Location = System.Drawing.Point(12, 177)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(150, 42)
		self._label5.TabIndex = 4
		self._label5.Text = "Pennies:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Black
		self._label6.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Brown
		self._label6.Location = System.Drawing.Point(159, 9)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(150, 42)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Black
		self._label7.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Brown
		self._label7.Location = System.Drawing.Point(159, 51)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(150, 42)
		self._label7.TabIndex = 6
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Black
		self._label8.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Brown
		self._label8.Location = System.Drawing.Point(159, 93)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(150, 42)
		self._label8.TabIndex = 7
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Black
		self._label9.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Brown
		self._label9.Location = System.Drawing.Point(159, 135)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(150, 42)
		self._label9.TabIndex = 8
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Black
		self._label10.Font = System.Drawing.Font("Chiller", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Brown
		self._label10.Location = System.Drawing.Point(159, 177)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(150, 42)
		self._label10.TabIndex = 9
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Juice ITC", 26.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Brown
		self._button1.Location = System.Drawing.Point(315, 173)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(170, 61)
		self._button1.TabIndex = 10
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(671, 265)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "lang_58T"
		self.ResumeLayout(False)



