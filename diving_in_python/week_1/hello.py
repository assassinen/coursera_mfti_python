print("Привет, мир!")

x = 0
y = 12
name = x or y
print(name)

print(r"//\\")
n = r"строка"
print(n)
print("a"*3)

n = "привет"
print(n[:])

a = b"test"
# b = b"тест"
c = b""

x = "Москва"
if "ква" not in x:
  print("1")
elif "ва" not in x:
  print("2")
else:
  print("3")


n = 0
while n < 3:
    if n > 0:
        continue
    else:
        break
    n += 1

print(n)


s = ""

for i in range(2, 10, 2):
		s += str(i)

print(s)
print()
print(bool(0.000001))