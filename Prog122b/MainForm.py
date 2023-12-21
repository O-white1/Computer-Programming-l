import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox2 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._listBox1.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 31
		self._listBox1.Location = System.Drawing.Point(12, 43)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(381, 159)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button1.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 217)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(322, 80)
		self._button1.TabIndex = 1
		self._button1.Text = "Show List"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button2.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(340, 217)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 80)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._button3.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(456, 217)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(334, 80)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._listBox2.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox2.FormattingEnabled = True
		self._listBox2.ItemHeight = 31
		self._listBox2.Location = System.Drawing.Point(399, 43)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(391, 159)
		self._listBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DimGray
		self._label1.Font = System.Drawing.Font("Perpetua Titling MT", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(381, 31)
		self._label1.TabIndex = 5
		self._label1.Text = "Hours:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DimGray
		self._label2.Font = System.Drawing.Font("Perpetua Titling MT", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(399, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(391, 31)
		self._label2.TabIndex = 6
		self._label2.Text = "Pay in Dollars:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(802, 309)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range (1, 40+1):
			self._listBox1.Items.Add(num)
		for num in range (1, 40+1):
			self._listBox2.Items.Add(num * 4)
			

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._listBox2.Items.Clear()
		
	def Button3Click(self, sender, e):
		Application.Exit()