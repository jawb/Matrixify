import sublime_plugin


def read_format(format):
    separators = format.split('%')
    dim = len(separators) - 1
    return (separators, dim)


def generate_format(dim):
    format = ""
    for i in range(dim):
        format += "%,"
    return format


def elements_to_matrix(format, elements):
    (separators, dim) = read_format(format)
    lengths = [0] * dim
    for i in range(dim):
        for l in range(i, len(elements) - 1, dim):
            lengths[i] = max(lengths[i], len(elements[l]))
    output = ""
    for i in range(0, len(elements)):
        el = elements[i]
        output += separators[i % dim] + el + (lengths[(i % dim)] - len(el)) * " "
        if (i % dim) == dim - 1:
            output += separators[dim] + "\n"
    return output


class MatrixifyCommand(sublime_plugin.TextCommand):
    def run(self, edit, dim=0, reqsep=False, sep="\n"):
        self.reqsep = reqsep
        self.sep = sep
        self.format = None
        self.stat = 0
        self.text = ""
        self.edit = edit

        if dim == 0 and not reqsep:
            self.stat = 1
            self.text += "Enter format :"
        if dim > 0 and reqsep:
            self.stat = 2
            self.format = generate_format(dim)
            self.text += "Enter separator :"
        if dim == 0 and reqsep:
            self.stat = 3
            self.text += 'Enter ("format", "separator") :'

        if self.stat > 0:
            self.view.window().show_input_panel(self.text, "", self.on_arg_done, None, None)
        else:
            self.format = generate_format(dim)
            self.done()

    def on_arg_done(self, input):
        if self.stat == 1:
            self.format = input
        if self.stat == 2:
            self.sep = input
        if self.stat == 3:
            (self.format, self.sep) = eval(input)
        self.done()

    def done(self):
        sels = self.view.sel()
        for sel in sels:
            self.elements = self.view.substr(sel).split(self.sep)
            output = elements_to_matrix(self.format, self.elements)
            self.view.replace(self.edit, sel, output)
