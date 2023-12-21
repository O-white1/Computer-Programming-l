import math
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
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button1.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 66)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Add"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button2.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(93, 66)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Subtract"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button3.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 95)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Multiply"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button4.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(93, 95)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 23)
		self._button4.TabIndex = 3
		self._button4.Text = "Divide"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button5.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(12, 124)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 23)
		self._button5.TabIndex = 4
		self._button5.Text = "Floor Divide"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button6.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(93, 124)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 23)
		self._button6.TabIndex = 5
		self._button6.Text = "Power"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button7.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(12, 153)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(156, 23)
		self._button7.TabIndex = 6
		self._button7.Text = "Modulus"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "Number 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 32)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "Number 2:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox1.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(118, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 26)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox2.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(118, 35)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 26)
		self._textBox2.TabIndex = 10
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label6.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(174, 66)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(216, 110)
		self._label6.TabIndex = 14
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button8.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(224, 12)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(75, 43)
		self._button8.TabIndex = 15
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button9.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(315, 13)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(75, 42)
		self._button9.TabIndex = 16
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(409, 206)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "SimpleCalc140"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 + num2
		self._label6.Text = str(sol)

	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 - num2
		self._label6.Text = str(sol)

	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 * num2
		self._label6.Text = str(sol)

	def Button4Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 / num2
		self._label6.Text = str(sol)

	def Button5Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 // num2
		self._label6.Text = str(sol)

	def Button6Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 ** num2
		self._label6.Text = str(sol)

	def Button7Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sol = num1 % num2
		self._label6.Text = str(sol)

	def Button8Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self.label6.Text = ""

	def Label1Click(self, sender, e):
		pass

	def Button9Click(self, sender, e):
		Application.Exit()