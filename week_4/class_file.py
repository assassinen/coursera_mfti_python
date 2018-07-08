import os
import tempfile



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

    def __add__(self, obj):
        new_file = os.path.join(tempfile.gettempdir(), self.file_name.split('/')[-1] + '_' + obj.file_name.split('/')[-1])
        # new_file = os.path.join(tempfile.gettempdir(), )
        # new_file = 'three'
        new_obj =  self.create_integrated_obj(new_file)
        for line in self:
            new_obj.write(line)
        for line in obj:
            new_obj.write(line)
        return new_obj

    @classmethod
    def create_integrated_obj(cls, file_name):
        return cls(file_name)

    def __str__(self):
        return self.file_name


if __name__ == "__main__":
    obj = File('file.txt')

    for line in File('file.txt'):
        print(line)

    print(obj)
    # obj.write('строка1\n')
    # obj.write('строка2\n')

    second = File('second_2')
    second.write('это второй файл1\n')
    # # second.write('это второй файл2\n')
    #
    integrated = obj + second
    print(integrated)
    # # print(integrated.file_name)
    #
    # for i in integrated:
    #     print(i)

    # print(obj.readline())
    # print(obj.readline())
    # print(obj.readline())

    # for i in obj:
    #     print(i)