﻿#import math  +.
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("prog_65h.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(118, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter pounds:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkRed
		self._label2.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(12, 38)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(118, 37)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter shillings:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkRed
		self._label3.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(12, 61)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(105, 27)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter pence"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkRed
		self._textBox1.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._textBox1.Location = System.Drawing.Point(109, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(118, 27)
		self._textBox1.TabIndex = 3
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkRed
		self._textBox2.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._textBox2.Location = System.Drawing.Point(109, 35)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(118, 27)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkRed
		self._textBox3.Font = System.Drawing.Font("Old English Text MT", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._textBox3.Location = System.Drawing.Point(109, 61)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(118, 27)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MidnightBlue
		self._label4.Font = System.Drawing.Font("Old English Text MT", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Image = resources.GetObject("label4.Image")
		self._label4.Location = System.Drawing.Point(12, 91)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(215, 112)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Old English Text MT", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button1.Image = resources.GetObject("button1.Image")
		self._button1.Location = System.Drawing.Point(233, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(180, 50)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Old English Text MT", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button2.Image = resources.GetObject("button2.Image")
		self._button2.Location = System.Drawing.Point(233, 82)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(180, 50)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Old English Text MT", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button3.Image = resources.GetObject("button3.Image")
		self._button3.Location = System.Drawing.Point(233, 153)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(180, 50)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(420, 217)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog_65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		poundsOLD = int(self._textBox1.Text)
		shillings = int(self._textBox2.Text)
		penceOLD = int(self._textBox3.Text)
		pence2pound = int(penceOLD / 100)
		shillings2pounds = int(shillings /20)
		poundsNEW = str(shillings2pounds + poundsOLD)
		
		self._label4.Text = str(poundsNEW) + "." + str(penceOLD)
		

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""