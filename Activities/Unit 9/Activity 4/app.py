# Python String Operations
str1 = "Hello"
str2 = "World!"

# using +
print("str1 + str2 = ", str1 + str2)

# using *
print("str1 * 3 =", str1 * 3)

# --------------------------
# --------------------------

# using +
newStr1 = str1 + str2
assert newStr1 == "HelloWorld!", "String addition wrong value"

# using *
newStr2 = str1 * 3
assert newStr2 == "HelloHelloHello", "String multiplication wrong value"
