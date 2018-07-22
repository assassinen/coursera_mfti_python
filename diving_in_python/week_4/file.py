
class File:

    def __init__(self, file_name, mode='a+'):
        self.file_name = file_name
        self.mode = mode
        self.f = None

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()
        if not line:
            self.f.close()
            raise StopIteration
        return line

    def write(self, line):
        with open(self.file_name, self.mode) as f:
            f.write(line)

    def readline(self):
        if self.f is None:
            self.f = open(self.file_name, 'r')
        try:
            result = self.f.readline()
        except:
            result = False
        return result





obj = File('file.txt')
# obj.write('line\n')
print(obj.readline())
print(obj.readline())
print(obj.readline())

for i in obj:
    print(i)