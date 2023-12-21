import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Whack_A_Mole.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button10 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button1.Font = System.Drawing.Font("Snap ITC", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DeepPink
		self._button1.Location = System.Drawing.Point(181, 113)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(478, 183)
		self._button1.TabIndex = 0
		self._button1.Text = "Start Whack-A-Mole"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(181, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(141, 109)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Visible = False
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
		self._pictureBox2.Location = System.Drawing.Point(12, 127)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(141, 109)
		self._pictureBox2.TabIndex = 3
		self._pictureBox2.TabStop = False
		self._pictureBox2.Visible = False
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(350, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(141, 109)
		self._button3.TabIndex = 4
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Visible = False
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(518, 12)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(141, 109)
		self._button4.TabIndex = 5
		self._button4.Text = "button4"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Visible = False
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(181, 158)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(141, 109)
		self._button5.TabIndex = 6
		self._button5.Text = "button5"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Visible = False
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(350, 158)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(141, 109)
		self._button6.TabIndex = 7
		self._button6.Text = "button6"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Visible = False
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(518, 158)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(141, 109)
		self._button7.TabIndex = 8
		self._button7.Text = "button7"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Visible = False
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(181, 327)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(141, 109)
		self._button8.TabIndex = 9
		self._button8.Text = "button8"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Visible = False
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(350, 327)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(141, 109)
		self._button9.TabIndex = 10
		self._button9.Text = "button9"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Visible = False
		# 
		# button10
		# 
		self._button10.Location = System.Drawing.Point(518, 327)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(141, 109)
		self._button10.TabIndex = 11
		self._button10.Text = "button10"
		self._button10.UseVisualStyleBackColor = True
		self._button10.Visible = False
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
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(852, 448)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button10)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Whack-A-Mole"
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self.ResumeLayout(False)
		
		
		


	def Button1Click(self, sender, e):
		self._button1.Visible = False
		self._button2.Visible = True
		self._button3.Visible = True
		self._button4.Visible = True
		self._button5.Visible = True
		self._button6.Visible = True
		self._button7.Visible = True
		self._button8.Visible = True
		self._button9.Visible = True
		self._button10.Visible = True