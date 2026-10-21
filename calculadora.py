var1 = float(input("Digite o primeiro número: "))
var2 = float(input("Digite o segundo número: "))
var3 = input("Digite qual operação você quer realizar (+, -, /, *): ")

if var3 == "+":
  result = var1 + var2
  print(result)
elif var3 == "-":
  result = var1 - var2
  print(result)
elif var3 == "*":
  if var1 == 0 or var2 == 0:
    result = 0
    print(result)
  else:
    result = var1 * var2
    print(result)
elif var3 == "/":
  if var1 == 0:
    result = 0
    print(result)
  elif var2 == 0:
    print("Essa operação não existe.")
  else:
    result = var1 / var2
    print(result)