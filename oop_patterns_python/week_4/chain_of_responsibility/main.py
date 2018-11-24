class SomeObject:
    def __init__(self):
        self.integer_field = 1
        self.float_field = 0.1
        self.string_field = "a"


class EventSet:
    def __init__(self, type):
        self.type = type

class EventGet:
    def __init__(self, type):
        self.type = type

class NullHandler:
    def __init__(self, subccessor=None):
        self.__subccessor = subccessor

    def handle(self, obj, event):
        if self.__subccessor is not None:
            return self.__subccessor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type == int:
            return obj.integer_field
        elif isinstance(event, EventSet) and isinstance(event.type, int):
            obj.integer_field = event.type
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type == float:
            return obj.float_field
        elif isinstance(event, EventSet) and isinstance(event.type, float):
            obj.float_field = event.type
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type == str:
            return obj.string_field
        elif isinstance(event, EventSet) and isinstance(event.type, str):
            obj.string_field = event.type
        else:
            return super().handle(obj, event)

obj = SomeObject()

class Chain():
    def __init__(self):
        self.handlers = IntHandler(FloatHandler(StrHandler(NullHandler())))
        # self.handlers = IntHandler()

    def handle(self, obj, event):
        return self.handlers.handle(obj, event)

chain = Chain()
# print(chain.chain)
# chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
print(chain.handle(obj, EventGet(str)))
print("===")
print(chain.handle(obj, EventSet(10)))
print(chain.handle(obj, EventSet("kshdf")))
print(chain.handle(obj, EventGet(str)))
print(chain.handle(obj, EventSet(5.6)))
print("===")
print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
print(chain.handle(obj, EventGet(str)))
# chain.handle(obj, EventSet([1,4,5]))
# print("===")
# chain.handle(obj, EventGet(int))
# chain.handle(obj, EventGet(float))
# chain.handle(obj, EventGet(str))
# chain.handle(obj, EventGet(list))



# def handle_event(self, obj, event):
#     if isinstance(event, EventGet) and event.type == "float":
#         print(obj.float_field)
#     elif isinstance(event, EventSet) and isinstance(event.type, float):
#         obj.float_field = event.type
#     else:
#         return self.successor.handle_event(obj, event)