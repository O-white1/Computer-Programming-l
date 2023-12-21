require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Salmon
		@button1.Location = System::Drawing::Point.new(118, 137)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(191, 68)
		@button1.TabIndex = 0
		@button1.Text = "SHOW"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Salmon
		@button2.Location = System::Drawing::Point.new(412, 137)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(191, 68)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightCoral
		@label1.Location = System::Drawing::Point.new(118, 60)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(485, 74)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(625, 60)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 145)
		@button3.TabIndex = 3
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(827, 261)
		self.Controls.Add(@button3)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Quote"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "The oldest and strongest emotion is fear, and the oldest and strongest kind of fear is the fear of the unknown. HP. Lovecraft."
		
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

