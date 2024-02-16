#Try /Except

try: 
    f = open('src/CoreySchaferTutorial/teste_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
