import re

# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

# print(re.search('^Life', 'Life is too short'))
# print(re.search('^Life', 'My Life'))

# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'Life is too short, you need python'))

# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))

# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))
#
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# p = re.compile(r"(\w+)\s+((\d+)[-](\d+)[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group(4))


# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())

# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234")
# print(m.group("name"))


# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())

# p = re.compile(".*[.](?!bat$|exe$).*$")
# m = p.search("bat.bat.exe")
# print(m.group())

# p = re.compile('(blue|white|red)')
# m = p.subn('colour', 'blue socks and red shoes kkkwhite')
# print(m)
#

s = '<html><head><title>Title</title>'
print(len(s))

print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())