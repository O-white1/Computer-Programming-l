import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button1.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 191)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(493, 28)
		self._button1.TabIndex = 0
		self._button1.Text = "Quit"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button2.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 162)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(493, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button3.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 133)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(493, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Calc"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._radioButton1.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(12, 12)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 3
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Adult"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._radioButton2.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(12, 43)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 4
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._radioButton3.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(12, 73)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 5
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._radioButton4.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(12, 103)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 6
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior(60+)"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(122, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(120, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "Number of months:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox1.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(248, 14)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 22)
		self._textBox1.TabIndex = 8
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._checkBox1.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(396, 44)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(121, 24)
		self._checkBox1.TabIndex = 9
		self._checkBox1.Text = "Yoga Lessons"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._checkBox2.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(396, 74)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(121, 24)
		self._checkBox2.TabIndex = 10
		self._checkBox2.Text = "Katate Lessons"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._checkBox3.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(396, 104)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(121, 24)
		self._checkBox3.TabIndex = 11
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(396, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 23)
		self._label2.TabIndex = 12
		self._label2.Text = "Select Lesson Type:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label3.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(122, 43)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(120, 25)
		self._label3.TabIndex = 13
		self._label3.Text = "Price:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Font = System.Drawing.Font("Segoe UI Variable Display", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(248, 43)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 24)
		self._label4.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(519, 235)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "p250Member"
		self.ResumeLayout(False)
		self.PerformLayout()


	def RadioButton4CheckedChanged(self, sender, e):
		pass
	def Button3Click(self, sender, e):
		lesson = 1 # yoga
		adu = 40
		chi = 20
		stu = 25
		sen = 30
		pscale = 0
		mdisc = 0
		if self._radioButton1.Checked:
			pscale = 40
		elif self._radioButton2.Checked:
			pscale = 20
		elif self._radioButton3.Checked:
			pscale = 25
		elif self._radioButton4.Checked:
			pscale = 30
		months = self._textBox1.Text
		if months >= 1 and months <= 3:
			mdisc = 0
		elif months > 3 and months <= 6:
			mdisc = 0.05
		elif months > 6 and months <= 9:
			mdisc = 0.08
		elif months >= 10:
			mdisc = 0.10
		
		
		if self._checkBox1.Checked == True:
			self._checkBox2.Checked = False
			self._checkBox3.Checked = False
			lesson = 1
		if self._checkBox2.Checked == True:
			self._checkBox1.Checked = False
			self._checkBox3.Checked = False
			lesson = 2 # karate
		if self._checkBox3.Checked == True:
			self._checkBox1.Checked = False
			self._checkBox2.Checked = False
			lesson = 3 # personal trainer
			
		if lesson == 1:
			lessonCash = 10
		elif lesson == 2:
			lessonCash = 30
		elif lesson == 3:
			lessonCash = 50
		tot1 = (months * pscale) + (lessonCash)
		discount = tot1 * mdisc
		TrueTotal = to1 - discount
		self._label4.Text = str(TrueTotal)
		
		