﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._textBox1.Location = System.Drawing.Point(141, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 21)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._textBox2.Location = System.Drawing.Point(141, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 21)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter Speed of car:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(12, 41)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Enter Speed limit:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(12, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Fine:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Old English Text MT", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(141, 64)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(247, 10)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(247, 39)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(165, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(247, 64)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(424, 97)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog_82a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()



	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		car  = int(self._textBox1.Text)
		limit = int(self._textBox2.Text)
		dif = int(car - limit)
		fine = str(dif * 10)
		self._label4.Text = str(fine)

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()