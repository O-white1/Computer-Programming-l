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
		@button1.Location = System::Drawing::Point.new(12, 283)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(192, 91)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(552, 283)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(192, 91)
		@button2.TabIndex = 1
		@button2.Text = "Exit"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(274, 283)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(192, 91)
		@button3.TabIndex = 2
		@button3.Text = "Clear"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightCoral
		@label1.Location = System::Drawing::Point.new(12, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(732, 271)
		@label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(756, 386)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Web Design \n Alegbra \n Freshman seminar \n Global studies \n Game design \n Computer design \n English 9 \n "
		
	end

	def Button3Click(sender, e)
		@label1.Text = ""
	end

	def Button2Click(sender, e)
		application.exit
		
	end
end

