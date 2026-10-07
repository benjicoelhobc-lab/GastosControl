case 3:
			print("===============================")
			if len(gastos) == 0:
				print("Nenhum gasto cadastrado.")
			else:
				for gasto in gastos:
					print("===============================")
					print(f"Descrição: {gasto['Descrição: ']}")
					print(f"Valor: R$ {gasto['Valor']:.2f}")
					print(f"Categoria: {gasto['Categoria']}")

		case 4:
			print("==========SITUAÇÃO FINANCEIRA==========")
			if renda_mensal == 0:
				print("Vc ainda não informou sua renda mensal.")
			else:
				saldo = renda_mensal - total_gasto
				print(f"Renda mensal de: R$ {renda_mensal}")
				print(f"Total gasto de: R$ {total_gasto}")
				print(f"Saldo: R$ {saldo}")
				if saldo > 0:
					print("Situação: Vc ainda possui dinheiro disponível.")
				elif saldo == 0:
					print("Situação: Vc gastou exatamente a sua renda.")
				else:
					print("Situação: Vc está no vermelho")
