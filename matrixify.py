import sublime, sublime_plugin

class MatrixifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
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
			separators = lines[0].split('%')
			dim = len(separators) - 1
			lengths = [0] * dim
			for i in range(dim):
				for l in range(i+1,len(lines)-1,dim):
					lengths[i] = max(lengths[i] , len(lines[l]))
			output = ""
			for i in range(1,len(lines)):
				index = dim-1 if (i%dim)==0 else (i%dim)-1
				line = lines[i]
				output += separators[index] + line + (lengths[(i%dim) -1] - len(line))*" "
				if (i%dim) == 0:
					output += separators[dim] + "\n"
			self.view.replace(edit, sel, output)
