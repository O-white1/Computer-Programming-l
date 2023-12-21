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
		self._label2 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Transparent
		self._button1.Location = System.Drawing.Point(11, 300)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 59)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DimGray
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Transparent
		self._button2.Location = System.Drawing.Point(111, 300)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 59)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DimGray
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Transparent
		self._button3.Location = System.Drawing.Point(209, 300)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 59)
		self._button3.TabIndex = 2
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DimGray
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Transparent
		self._label2.Location = System.Drawing.Point(11, 12)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 19)
		self._label2.TabIndex = 4
		self._label2.Text = "Y:"
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DimGray
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Transparent
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(38, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(251, 277)
		self._listBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(316, 373)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog_122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for x in range(-12, 16+1):
			y = (x ** 6) - (3 * (x ** 5)) - (93 * (x ** 4)) + (87 * (x ** 3)) + (1596 * (x ** 2)) + ((-1380 * x) -2800)
			self._listBox1.Items.Add(str(x))
			self._listBox1.Items.Add(str(y))

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()