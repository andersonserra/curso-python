# Criar 500 arquivos com o nome hello-world:
#para nao criar um vetor com 500 strings de 1 a 500 você pode usar os métodos list(range(value1,to-value2))

#start code
numeros = list(range(1,500))
#items = ["1","2","3"]
content = "This is the first line of code\nThis is my second line of code with %s the first item in my list\nAnd this is my last line of code"

for item in numeros:
    with open("%s_hello_world.txt" % item, "w") as f:
        f.write(content % item)
