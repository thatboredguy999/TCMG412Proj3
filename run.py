t = open ('http_access_log.txt', 'r')
q1 = 0
q2 = 0

for line in t:
        if '/1995' in line:
                q1 = q1 + 1
for line in t:
        if ',199' in line:
                q2 = q2 + 1

print (q1)
print (q2)
