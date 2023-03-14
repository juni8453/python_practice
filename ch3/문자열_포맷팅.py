# %d(정수), %f(실수), %s(문자)
my_str = "My name is %s" % "Tany"
print(my_str)

my_int = "%d %d" % (1, 2)
print(my_int)

my_float = "%f %f" % (3.14, 3.5)
print(my_float)

# format() 메서드 사용
print("My name is {}".format("Tany"))
print("My age is {}".format("28"))
print("{} * {} = {}".format(2, 3, 2 * 3))

# 중괄호 순서를 바꿀 수도 있다.
print("{1} * {2} = {0}".format(2, 3, 2 * 3))
print("{}, {}".format("apple", "banana"))
