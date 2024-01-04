import math
import System.Drawing
import System.Windows.Forms
import _random

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("Whack_A_Mole.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button1 = System.Windows.Forms.Button()
		self._TL = System.Windows.Forms.Button()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._TM = System.Windows.Forms.Button()
		self._TR = System.Windows.Forms.Button()
		self._ML = System.Windows.Forms.Button()
		self._MM = System.Windows.Forms.Button()
		self._MR = System.Windows.Forms.Button()
		self._BL = System.Windows.Forms.Button()
		self._BM = System.Windows.Forms.Button()
		self._BR = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._label6 = System.Windows.Forms.Label()
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button1.Font = System.Drawing.Font("Ravie", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.InfoText
		self._button1.Location = System.Drawing.Point(181, 113)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(478, 183)
		self._button1.TabIndex = 0
		self._button1.Text = "Play Crustacean Station!"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# TL
		# 
		self._TL.Location = System.Drawing.Point(181, 12)
		self._TL.Name = "TL"
		self._TL.Size = System.Drawing.Size(141, 109)
		self._TL.TabIndex = 1
		self._TL.Text = "button2"
		self._TL.UseVisualStyleBackColor = True
		self._TL.Visible = False
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackgroundImage = resources.GetObject("pictureBox1.BackgroundImage")
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
		self._pictureBox1.Location = System.Drawing.Point(12, 12)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(141, 109)
		self._pictureBox1.TabIndex = 2
		self._pictureBox1.TabStop = False
		self._pictureBox1.Visible = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackgroundImage = resources.GetObject("pictureBox2.BackgroundImage")
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(12, 158)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(141, 109)
		self._pictureBox2.TabIndex = 3
		self._pictureBox2.TabStop = False
		self._pictureBox2.Visible = False
		# 
		# TM
		# 
		self._TM.Location = System.Drawing.Point(350, 12)
		self._TM.Name = "TM"
		self._TM.Size = System.Drawing.Size(141, 109)
		self._TM.TabIndex = 4
		self._TM.Text = "button3"
		self._TM.UseVisualStyleBackColor = True
		self._TM.Visible = False
		# 
		# TR
		# 
		self._TR.Location = System.Drawing.Point(518, 12)
		self._TR.Name = "TR"
		self._TR.Size = System.Drawing.Size(141, 109)
		self._TR.TabIndex = 5
		self._TR.Text = "button4"
		self._TR.UseVisualStyleBackColor = True
		self._TR.Visible = False
		# 
		# ML
		# 
		self._ML.Location = System.Drawing.Point(181, 158)
		self._ML.Name = "ML"
		self._ML.Size = System.Drawing.Size(141, 109)
		self._ML.TabIndex = 6
		self._ML.Text = "button5"
		self._ML.UseVisualStyleBackColor = True
		self._ML.Visible = False
		# 
		# MM
		# 
		self._MM.Location = System.Drawing.Point(350, 158)
		self._MM.Name = "MM"
		self._MM.Size = System.Drawing.Size(141, 109)
		self._MM.TabIndex = 7
		self._MM.Text = "button6"
		self._MM.UseVisualStyleBackColor = True
		self._MM.Visible = False
		# 
		# MR
		# 
		self._MR.Location = System.Drawing.Point(518, 158)
		self._MR.Name = "MR"
		self._MR.Size = System.Drawing.Size(141, 109)
		self._MR.TabIndex = 8
		self._MR.Text = "button7"
		self._MR.UseVisualStyleBackColor = True
		self._MR.Visible = False
		# 
		# BL
		# 
		self._BL.Location = System.Drawing.Point(181, 315)
		self._BL.Name = "BL"
		self._BL.Size = System.Drawing.Size(141, 109)
		self._BL.TabIndex = 9
		self._BL.Text = "button8"
		self._BL.UseVisualStyleBackColor = True
		self._BL.Visible = False
		# 
		# BM
		# 
		self._BM.Location = System.Drawing.Point(350, 315)
		self._BM.Name = "BM"
		self._BM.Size = System.Drawing.Size(141, 109)
		self._BM.TabIndex = 10
		self._BM.Text = "button9"
		self._BM.UseVisualStyleBackColor = True
		self._BM.Visible = False
		# 
		# BR
		# 
		self._BR.Location = System.Drawing.Point(518, 315)
		self._BR.Name = "BR"
		self._BR.Size = System.Drawing.Size(141, 109)
		self._BR.TabIndex = 11
		self._BR.Text = "button10"
		self._BR.UseVisualStyleBackColor = True
		self._BR.Visible = False
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Stencil", 72, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(657, 62)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(193, 121)
		self._label1.TabIndex = 12
		self._label1.Text = "0"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Visible = False
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Stencil", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(689, 26)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(115, 36)
		self._label2.TabIndex = 13
		self._label2.Text = "Score:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Visible = False
		# 
		# timer1
		# 
		self._timer1.Tick += self.Timer1Tick
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(163, 69)
		self._label3.TabIndex = 14
		self._label3.Text = "Whack The Mole!"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Visible = False
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 67)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(163, 54)
		self._label4.TabIndex = 15
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Visible = False
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 124)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(163, 23)
		self._label5.TabIndex = 16
		self._label5.Text = "Seconds!"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label5.Visible = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackgroundImage = resources.GetObject("pictureBox3.BackgroundImage")
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(12, 315)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(141, 109)
		self._pictureBox3.TabIndex = 17
		self._pictureBox3.TabStop = False
		self._pictureBox3.Visible = False
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox4.Location = System.Drawing.Point(680, 170)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(141, 109)
		self._pictureBox4.TabIndex = 18
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(680, 315)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(141, 109)
		self._pictureBox5.TabIndex = 19
		self._pictureBox5.TabStop = False
		self._pictureBox5.Visible = False
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Ravie", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(181, 12)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(478, 66)
		self._label6.TabIndex = 20
		self._label6.Text = "Get the Blue Crab!"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Visible = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(844, 448)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._BR)
		self.Controls.Add(self._BM)
		self.Controls.Add(self._BL)
		self.Controls.Add(self._MR)
		self.Controls.Add(self._MM)
		self.Controls.Add(self._ML)
		self.Controls.Add(self._TR)
		self.Controls.Add(self._TM)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._TL)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Whack-A-Mole"
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self.ResumeLayout(False)
		
		

	def Button1Click(self, sender, e):
		self._button1.Visible = False
		self._TL.Visible = True
		self._TM.Visible = True
		self._TR.Visible = True
		self._ML.Visible = True
		self._MM.Visible = True
		self._MR.Visible = True
		self._BL.Visible = True
		self._BM.Visible = True
		self._BR.Visible = True
		self._label1.Visible = True
		self._label2.Visible = True
		self._label3.Visible = True
		self._label4.Visible = True
		self._label5.Visible = True
		self._label6.Visible = True
		self._timer1.Start()

		self.TimeLeft = 10
		self.death = 10
		self.score = 0
		self.lives = 3
		self.lvl = 1
		
		
		pic1 = self._pictureBox2.BackgroundImage
		self.pic2 = self._pictureBox3.BackgroundImage
		self.pic3 = self._pictureBox4.BackgroundImage
		self.pic4 = self._pictureBox5.BackgroundImage
		
		self.mole = pic1


	def Timer1Tick(self, sender, e):
		self.TimeLeft -= 1
		self.death -= 1
		
		if self.TimeLeft == 0:
			self.LCV1 = round(random(1, 4)
			if LCV1 == 1: #?
				self.TL.BackgroundImage = pic1
			elif LCV1 == 2:
				self.TL.BackgroundImage = pic2
			elif LCV1 == 3:
				self.TL.BackgroundImage = pic3
			elif LCV1 == 4:
				self.TL.BackgroundImage = pic4
				
				
			self.LCV2 = math.round(math.random(1-4))
			if LCV2 == 1:
				self.TM.BackgroundImage = pic1
			elif LCV2 == 2:
				self.TM.BackgroundImage = pic2
			elif LCV2 == 3:
				self.TM.BackgroundImage = pic3
			elif LCV2 == 4:
				self.TM.BackgroundImage = pic4
				
			self.LCV3 = math.round(math.random(1-4))
			self.LCV4 = math.round(math.random(1-4))
			self.LCV5 = math.round(math.random(1-4))
			self.LCV6 = math.round(math.random(1-4))
			self.LCV7 = math.round(math.random(1-4))
			self.LCV8 = math.round(math.random(1-4))
			self.LCV9 = math.round(math.random(1-4))
			
			
			