
import re
import email.utils
for _ in range(int(input())):
    s = input()
    u = email.utils.parseaddr(s)
    if re.search("^[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}$",u[-1],re.I):
        print(s)