class FileReader:

    def __init__(self, file=None):
        self.file = file

    def read(self):
        # result = ''
        try:
            with open(self.file, 'r') as f:
                result = f.read()
        except FileNotFoundError:
            result = ''
            # raise

        return result

# reader = FileReader("whatsapp.htl")
# print(123)
# print(reader.read())
# print(321)