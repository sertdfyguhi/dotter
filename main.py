from sys import argv

def run(text):
	stack = []
	toprint = ''
	a = False
	l = text.split('_')
	for idx, item in enumerate(l):
		if item.startswith('..............'):
			stack.append(chr(int(item[14:])))
		elif item.startswith('.............'):
			stack.insert(0, chr(int(item[13:])))
		elif item == '............':
			toprint += ''.join(stack)
		elif item == '...........':
			toprint += ''.join(stack)[::-1]
		elif item == '..........':
			toprint += stack[-1]
		elif item == '.........':
			toprint += stack[0]
		elif item == '........':
			del stack[-1]
		elif item == '.......':
			del stack[0]
		else:
			print(f"{idx + 1}: error")
			a = True
			break
	if a == False:
		print(toprint)

if len(argv) > 1:
  with open(argv[1], 'r') as f:
    text = f.read()
  run(text)
else:
	while True:
		text = input('> ')
		run(text)