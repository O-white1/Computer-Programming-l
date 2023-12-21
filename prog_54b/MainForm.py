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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MistyRose
		self._label1.Location = System.Drawing.Point(18, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.MistyRose
		self._label2.Location = System.Drawing.Point(18, 35)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Maroon
		self._label3.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.MistyRose
		self._label3.Location = System.Drawing.Point(18, 58)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Maroon
		self._label4.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.MistyRose
		self._label4.Location = System.Drawing.Point(18, 81)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Number 4:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.WhiteSmoke
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.Black
		self._textBox1.Location = System.Drawing.Point(124, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 33)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.WhiteSmoke
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.Black
		self._textBox2.Location = System.Drawing.Point(124, 32)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 33)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.WhiteSmoke
		self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox3.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.Black
		self._textBox3.Location = System.Drawing.Point(124, 58)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 33)
		self._textBox3.TabIndex = 6
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.WhiteSmoke
		self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox4.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.ForeColor = System.Drawing.Color.Black
		self._textBox4.Location = System.Drawing.Point(124, 81)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 33)
		self._textBox4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Maroon
		self._label5.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.MistyRose
		self._label5.Location = System.Drawing.Point(18, 158)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(141, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "The sum is:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Maroon
		self._label6.Font = System.Drawing.Font("Viner Hand ITC", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.MistyRose
		self._label6.Location = System.Drawing.Point(18, 181)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(141, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "The average is:"
		self._label6.Click += self.Label6Click
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Ravie", 9, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(328, 18)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 73)
		self._button1.TabIndex = 10
		self._button1.Text = "Caclulate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Ravie", 9, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(328, 97)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 73)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Ravie", 9, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(328, 176)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 73)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Font = System.Drawing.Font("Symbol", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 2)
		self._label7.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label7.Location = System.Drawing.Point(183, 158)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 13
		# 
		# label8
		# 
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label8.Font = System.Drawing.Font("Symbol", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 2)
		self._label8.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label8.Location = System.Drawing.Point(183, 186)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(443, 261)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog_54b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def TextBox3TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		SUM = int(num1 + num2 + num3 + num4)
		AVG = int(SUM / 4)
		self._label7.Text = str(SUM)
		self._label8.Text = str(AVG)
		
		

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()