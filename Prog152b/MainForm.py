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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MistyRose
		self._button1.Location = System.Drawing.Point(12, 373)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 103)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DimGray
		self._button2.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MistyRose
		self._button2.Location = System.Drawing.Point(140, 373)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(574, 103)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DimGray
		self._button3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MistyRose
		self._button3.Location = System.Drawing.Point(720, 373)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(122, 103)
		self._button3.TabIndex = 2
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DarkGray
		self._listBox1.Font = System.Drawing.Font("Poor Richard", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 44
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(386, 312)
		self._listBox1.TabIndex = 3
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.Color.DarkGray
		self._listBox2.Font = System.Drawing.Font("Poor Richard", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox2.FormattingEnabled = True
		self._listBox2.ItemHeight = 44
		self._listBox2.Location = System.Drawing.Point(458, 12)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(384, 312)
		self._listBox2.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(854, 488)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(2, 23, 2):
			self._listBox1.Items.Add(num)