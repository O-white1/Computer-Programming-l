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
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(5, 435)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(837, 45)
		self._button1.TabIndex = 0
		self._button1.Text = "Quit"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(5, 345)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(837, 39)
		self._button2.TabIndex = 1
		self._button2.Text = "Calc"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(5, 390)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(837, 39)
		self._button3.TabIndex = 2
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(166, 66)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(267, 43)
		self._label1.TabIndex = 3
		self._label1.Text = "Pay Per Year"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(166, 243)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(253, 38)
		self._label2.TabIndex = 4
		self._label2.Text = "Pay per period"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(166, 109)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(267, 39)
		self._label3.TabIndex = 5
		self._label3.Text = "Pay periods per year"
		self._label3.Click += self.Label3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(439, 74)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(439, 117)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(417, 243)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(145, 38)
		self._label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(861, 485)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "p153SalCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)	
		self._label4.Text = str(num1 / num2)

	def Button3Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button1Click(self, sender, e):
		Application.Exit()