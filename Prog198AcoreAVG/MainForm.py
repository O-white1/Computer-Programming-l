import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 298)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(837, 54)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Maroon
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(220, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(230, 29)
		self._textBox1.TabIndex = 1
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Maroon
		self._textBox2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(219, 53)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(231, 29)
		self._textBox2.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Maroon
		self._textBox3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(219, 88)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(231, 29)
		self._textBox3.TabIndex = 3
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(202, 29)
		self._label1.TabIndex = 4
		self._label1.Text = "Class A Tickets sold:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 46)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(202, 30)
		self._label2.TabIndex = 5
		self._label2.Text = "Class B Tickets sold:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Maroon
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 76)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(202, 35)
		self._label3.TabIndex = 6
		self._label3.Text = "Class C Tickets sold:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Maroon
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(456, 81)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(187, 23)
		self._label4.TabIndex = 9
		self._label4.Text = "Class C Tickets sold:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Maroon
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(456, 46)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(187, 35)
		self._label5.TabIndex = 8
		self._label5.Text = "Class B Tickets sold:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Maroon
		self._label6.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(456, 16)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(187, 30)
		self._label6.TabIndex = 7
		self._label6.Text = "Class A Tickets sold:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Maroon
		self._label7.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(640, 16)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(128, 23)
		self._label7.TabIndex = 10
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Maroon
		self._label8.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(640, 39)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(128, 30)
		self._label8.TabIndex = 11
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Maroon
		self._label9.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(640, 69)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(128, 35)
		self._label9.TabIndex = 12
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Maroon
		self._label10.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.White
		self._label10.Location = System.Drawing.Point(456, 104)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(187, 39)
		self._label10.TabIndex = 13
		self._label10.Text = "Total Revanue:"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Maroon
		self._label11.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.White
		self._label11.Location = System.Drawing.Point(640, 104)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(128, 39)
		self._label11.TabIndex = 14
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(12, 358)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(837, 58)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(12, 422)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(837, 51)
		self._button3.TabIndex = 16
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Brown
		self.ClientSize = System.Drawing.Size(861, 485)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog198AcoreAVG"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox3TextChanged(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass
	
	
	
	

	def Button1Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		ARev = A * 15
		BRev = B * 12
		CRev = C * 9
		TotRev = ARev + BRev + CRev
		
		self._label7.Text = str(ARev)
		self._label8.Text = str(BRev)
		self._label9.Text = str(CRev)
		self._label11.Text = str(TotRev)

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()