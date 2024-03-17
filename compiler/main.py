import basic 

while True:
		text = input("interperter >: ")
		result, error, ast = basic.run("<stdin>", text)
    
		if error: 
			print(error.as_string())
		else: 
			print(result)
			print(ast)