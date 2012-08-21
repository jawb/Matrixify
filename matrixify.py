import sublime, sublime_plugin

class MatrixifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def on_done(input):
			sels = self.view.sel()
			for sel in sels:
				lines = []
				separators = []
				lengths = []
				dim = 0
				lines = self.view.substr(sel)
				lines = lines.splitlines()
				lines = filter(None, lines)
				lines = [i.strip() for i in lines]
				separators = input.split('%')
				dim = len(separators) - 1
				lengths = [0] * dim
				for i in range(dim):
					for l in range(i,len(lines)-1,dim):
						lengths[i] = max(lengths[i] , len(lines[l]))
				output = ""
				for i in range(0,len(lines)):
					line = lines[i]
					output += separators[i%dim] + line + (lengths[(i%dim)] - len(line))*" "
					if (i%dim) == dim-1:
						output += separators[dim] + "\n"
				self.view.replace(edit, sel, output)

		self.view.window().show_input_panel("Enter matrix format", "", on_done, None, None)
