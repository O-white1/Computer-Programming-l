﻿require "mscorlib"
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
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Salmon
		@button1.Location = System::Drawing::Point.new(153, 150)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(177, 60)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Salmon
		@button2.Location = System::Drawing::Point.new(352, 150)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(177, 60)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightCoral
		@label1.Location = System::Drawing::Point.new(153, 68)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(376, 79)
		@label1.TabIndex = 2
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(815, 261)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "fav_club"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "DND Club"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

