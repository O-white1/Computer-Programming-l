﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("lang_58T.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
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
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(431, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(169, 20)
		self._textBox1.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(431, 61)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(169, 20)
		self._textBox2.TabIndex = 12
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightGray
		self._label11.ForeColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(325, 35)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 13
		self._label11.Text = "Amount owed:"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightGray
		self._label12.ForeColor = System.Drawing.Color.Black
		self._label12.Location = System.Drawing.Point(325, 61)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 14
		self._label12.Text = "Amount Given:"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.Font = System.Drawing.Font("Ravie", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.PeachPuff
		self._button1.Location = System.Drawing.Point(615, 360)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(143, 53)
		self._button1.TabIndex = 15
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.BackgroundImage = resources.GetObject("button2.BackgroundImage")
		self._button2.Font = System.Drawing.Font("Ravie", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.PeachPuff
		self._button2.Location = System.Drawing.Point(457, 360)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(143, 53)
		self._button2.TabIndex = 16
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Image = resources.GetObject("label1.Image")
		self._label1.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label1.Location = System.Drawing.Point(37, 57)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(151, 61)
		self._label1.TabIndex = 0
		self._label1.Text = "Dollars:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Red
		self._label2.Image = resources.GetObject("label2.Image")
		self._label2.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label2.Location = System.Drawing.Point(37, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(151, 61)
		self._label2.TabIndex = 1
		self._label2.Text = "Quarters:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Red
		self._label3.Image = resources.GetObject("label3.Image")
		self._label3.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label3.Location = System.Drawing.Point(37, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(151, 61)
		self._label3.TabIndex = 2
		self._label3.Text = "Dimes:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Black
		self._label4.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Red
		self._label4.Image = resources.GetObject("label4.Image")
		self._label4.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label4.Location = System.Drawing.Point(37, 205)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(151, 61)
		self._label4.TabIndex = 3
		self._label4.Text = "Nickels:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Black
		self._label5.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Red
		self._label5.Image = resources.GetObject("label5.Image")
		self._label5.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label5.Location = System.Drawing.Point(37, 253)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(151, 61)
		self._label5.TabIndex = 4
		self._label5.Text = "Pennies:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Black
		self._label6.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Red
		self._label6.Image = resources.GetObject("label6.Image")
		self._label6.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label6.Location = System.Drawing.Point(117, 57)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(151, 61)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Black
		self._label7.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Red
		self._label7.Image = resources.GetObject("label7.Image")
		self._label7.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label7.Location = System.Drawing.Point(117, 103)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(151, 61)
		self._label7.TabIndex = 6
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Black
		self._label8.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Red
		self._label8.Image = resources.GetObject("label8.Image")
		self._label8.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label8.Location = System.Drawing.Point(117, 156)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(151, 61)
		self._label8.TabIndex = 7
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Black
		self._label9.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Red
		self._label9.Image = resources.GetObject("label9.Image")
		self._label9.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label9.Location = System.Drawing.Point(117, 205)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(151, 61)
		self._label9.TabIndex = 8
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Black
		self._label10.Font = System.Drawing.Font("Pristina", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Red
		self._label10.Image = resources.GetObject("label10.Image")
		self._label10.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label10.Location = System.Drawing.Point(117, 253)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(151, 61)
		self._label10.TabIndex = 9
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightGray
		self._label13.ForeColor = System.Drawing.Color.Black
		self._label13.Location = System.Drawing.Point(325, 88)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 17
		self._label13.Text = "Change:"
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.White
		self._label14.ForeColor = System.Drawing.Color.Black
		self._label14.Location = System.Drawing.Point(431, 88)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(169, 23)
		self._label14.TabIndex = 18
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(785, 425)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
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
		self.ResumeLayout(False)
		self.PerformLayout()
	
	def Button2Click(self, sender, e):
		num1 = int(textBox1.Text)
		num2 = int(textBox2.Text)
		self.label14.Text = str(num1 - num2)