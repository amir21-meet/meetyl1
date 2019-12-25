encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l'}
def caesar(a):
	f_text=""
	for Letter in a:
		Letter = encoder_caesar{Letter}
		f_text = f_text + Letter
	print(f_text)
a="meet"
caesar(a)