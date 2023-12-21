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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(11, 123)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(520, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 161)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(519, 33)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 200)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(519, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(11, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(169, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Class A purchased:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(11, 41)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(169, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Class B purchased:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(11, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(169, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Class C purchased:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(177, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 29)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(177, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 29)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(177, 64)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 29)
		self._textBox3.TabIndex = 8
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DimGray
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(283, 13)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(121, 23)
		self._label4.TabIndex = 9
		self._label4.Text = "Class A rev:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DimGray
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(283, 41)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(121, 23)
		self._label5.TabIndex = 10
		self._label5.Text = "Class B rev:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DimGray
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(283, 70)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(121, 23)
		self._label6.TabIndex = 11
		self._label6.Text = "Class C rev:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DimGray
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(410, 13)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(121, 23)
		self._label7.TabIndex = 14
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DimGray
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(410, 39)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(121, 23)
		self._label8.TabIndex = 13
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DimGray
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(410, 70)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(121, 23)
		self._label9.TabIndex = 12
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DimGray
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label10.Location = System.Drawing.Point(156, 96)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(121, 23)
		self._label10.TabIndex = 15
		self._label10.Text = "Total Rev:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DimGray
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label11.Location = System.Drawing.Point(283, 97)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(121, 23)
		self._label11.TabIndex = 16
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(556, 419)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "P_186_SS"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = 15
		b = 12
		c = 9
		apurch = int(self._textBox1.Text)
		bpurch = int(self._textBox2.Text)
		cpurch = int(self._textBox3.Text)
		arev = a * apurch
		brev = b * bpurch
		crev = c * cpurch
		self._label7.Text = arev
		self._label8.Text = brev
		self._label9.Text = crev
		tot = (a * apurch) + (b * bpurch) + (c * cpurch)
		self._label11.Text = str(tot)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()