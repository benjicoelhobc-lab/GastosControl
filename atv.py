renda_mensal = 0.0
total_gasto = 0.0
gastos = [ ]
while True:
	print("----------MENU PRINCIPAL----------\n")
	print("1- Informar renda mensal")
	print("2- Cadastrar gasto")
	print("3- Consultar gastos")
	print("4- Consultar situação financeira")
	print("5- Ver estatística")
	print("6- Sair")
	
	opcao = int(input("Escolha uma das opções: "))
	
	match opcao:
		case 1:
			renda_mensal = float(input("Informe a sua renda mensal: R$ "))
			if renda_mensal <= 0:
				print("A renda precisa ser maior do que zero. Por favor, tente novamente.")
			else:
				print("Renda cadastrado com sucesso!")

		case 2:
			descricao = str(input("Descrição: "))
			valor = float(input("Valor: R$ "))
			print("\nCategoria")
			print("1. Alimentação")
			print("2. Transporte")
			print("3. Lazer")
			print("4. Saúde")
			print("5. Outros")
			
			categoria = int(input("Escolha uma das categorias: "))
			
			if categoria == 1:
				categoria = "Alimentação"
			elif categoria == 2:
				categoria = "Transporte"
			elif categoria == 3:
				categoria = "Lazer"
			elif categoria == 4:
				categoria = "Saúde"
			elif categoria == 5:
				categoria = "Outros"
			else:
				print("Cadastro Inválido")
				
			gasto = {"Descrição: ": descricao, "Valor": valor, "Categoria": categoria}
			gastos.append(gasto)
			total_gasto += valor
			print("\nGasto cadastrado com sucesso!")
			
			if renda_mensal == 0:
				print("Atenção! Vc ainda não informou a sua renda mensal.")
			elif total_gasto <= renda_mensal:
				print("Vc está dentro do orçamento.")
			else:
				print("Atenção! Vc ultrapassou a sua renda mensal.")
			continue
