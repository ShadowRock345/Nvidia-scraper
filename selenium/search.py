import re
re.M

a = "[\n  {\n    abc\n    \"purchaseLink\" : \"https://bla+3090\"\n    \"purchaseLink\" : \"https://bla+3080\"\n    blubs\n  }\n]\n"

m = re.search("\"purchaseLink\"\s+:\s+\"([^\"]*)\"", a)

print (a)
print (m.group(1))