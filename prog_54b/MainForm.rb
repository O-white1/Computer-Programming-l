require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(12, 12)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(130, 20)
		@textBox1.TabIndex = 0
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(12, 64)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(130, 20)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(12, 38)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(130, 20)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(12, 90)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(130, 20)
		@textBox4.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.RosyBrown
		@label1.Location = System::Drawing::Point.new(149, 8)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(266, 102)
		@label1.TabIndex = 4
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(12, 116)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(130, 43)
		@button1.TabIndex = 5
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(149, 116)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(130, 43)
		@button2.TabIndex = 6
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(285, 116)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(130, 43)
		@button3.TabIndex = 7
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.MistyRose
		self.ClientSize = System::Drawing::Size.new(815, 379)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "prog_54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end



	def Button3Click(sender, e)
		applicatiom.quit
		end

	def Button2Click(sender, e)
		@label1.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end
end

