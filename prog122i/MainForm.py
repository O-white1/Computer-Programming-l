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
		self._listBox1 = System.Windows.Forms.ListBox()
		self._listBox2 = System.Windows.Forms.ListBox()
		self._listBox3 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Transparent
		self._button1.Location = System.Drawing.Point(12, 345)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(144, 69)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DimGray
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Transparent
		self._button2.Location = System.Drawing.Point(162, 345)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 69)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DimGray
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Transparent
		self._button3.Location = System.Drawing.Point(312, 345)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 69)
		self._button3.TabIndex = 2
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DimGray
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Transparent
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(143, 324)
		self._listBox1.TabIndex = 3
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.Color.DimGray
		self._listBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox2.ForeColor = System.Drawing.Color.Transparent
		self._listBox2.FormattingEnabled = True
		self._listBox2.ItemHeight = 20
		self._listBox2.Location = System.Drawing.Point(163, 13)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(143, 324)
		self._listBox2.TabIndex = 4
		# 
		# listBox3
		# 
		self._listBox3.BackColor = System.Drawing.Color.DimGray
		self._listBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox3.ForeColor = System.Drawing.Color.Transparent
		self._listBox3.FormattingEnabled = True
		self._listBox3.ItemHeight = 20
		self._listBox3.Location = System.Drawing.Point(313, 13)
		self._listBox3.Name = "listBox3"
		self._listBox3.Size = System.Drawing.Size(143, 324)
		self._listBox3.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(468, 426)
		self.Controls.Add(self._listBox3)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(-25, 0+1):
			sqr = num * num
			num_cbrt = abs(num) ** 0.33
			numnew = abs(num)
			self._listBox1.Items.Add(-(numnew))
			self._listBox2.Items.Add(-(sqr))
			self._listBox3.Items.Add(-(num_cbrt))
		for num in range(1, 25+1):
			sqr = num * num
			self._listBox1.Items.Add(num)
			self._listBox2.Items.Add(sqr)
			self._listBox3.Items.Add(str(num ** 0.33))
		

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._listBox2.Items.Clear()
		self._listBox3.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
		