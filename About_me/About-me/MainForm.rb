require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Cursor = System::Windows::Forms::Cursors.Cross
		@button1.Location = System::Drawing::Point.new(12, 179)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(208, 106)
		@button1.TabIndex = 0
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(601, 179)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(208, 106)
		@button3.TabIndex = 2
		@button3.Text = "clear"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(797, 167)
		@label1.TabIndex = 3
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Silver
		self.ClientSize = System::Drawing::Size.new(821, 308)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button1)
		self.Cursor = System::Windows::Forms::Cursors.NoMove2D
		self.Name = "MainForm"
		self.Text = "About-me"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "My name is owen white and I like music."
	end

	def Button3Click(sender, e)
		@label1.Text = ""
	end
end

