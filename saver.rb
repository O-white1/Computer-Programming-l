require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DimGray
		@button1.ForeColor = System::Drawing::SystemColors.Control
		@button1.Location = System::Drawing::Point.new(12, 243)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(261, 111)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DimGray
		@button2.ForeColor = System::Drawing::SystemColors.Control
		@button2.Location = System::Drawing::Point.new(270, 243)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(261, 111)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.DimGray
		@button3.ForeColor = System::Drawing::SystemColors.Control
		@button3.Location = System::Drawing::Point.new(526, 243)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(261, 111)
		@button3.TabIndex = 2
		@button3.Text = "exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.GradientInactiveCaption
		@label1.Location = System::Drawing::Point.new(-24, -48)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(860, 288)
		@label1.TabIndex = 3
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(799, 378)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "phone numbers"
		self.ResumeLayout(false)
	end
	

	def Button1Click(sender, e)
		@label1.Text = "(608) 563-5566
		(608) 752-0100
		1 (877) 767-3937
		(608) 563-5530
		(608) 741-9464"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end

	def Button3Click(sender, e)
		Application.exit
	end
end

