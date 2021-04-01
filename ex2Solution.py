class Py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(Py_solution().reverse_words('hello world'))
