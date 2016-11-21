CODEC = 'utf-8'
text = u'This line is busy'
text_bytes = text.encode(CODEC)

f_path = '/tmp/1'
with open(f_path, 'w') as fout:
	fout.write(text_bytes)

with open(f_path, 'r') as fin:
	data = fin.read()

print data.decode(CODEC)
