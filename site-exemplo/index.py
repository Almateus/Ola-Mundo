vi = float(input('Qual o valor do imovel a ser financiado? R$ '))
sal = float(input ('Qual o valor da sua renda mensal? R$ '))
n = int(input('qual o prazo de pagamento em meses: '))
r = float(input('Qual a taxa efetiva anual do financiamento:  '))
teq = ((1 + r/100)**(1 / 12))-1
print(teq)
vjuros = float(vi* teq)
vprincipal = vi / n
vparcela = vjuros + vprincipal
print('Valor da parcela mensal é de R${:.2f}'.format(vparcela))
print('O valor dos juros mensais é de R${:.2f}'.format(vjuros))
print('O valor de amortizaçao mensal é de R${:.2f}'.format(vprincipal))
comprometimento = (vparcela / sal)* 100
if comprometimento <= 30 :
  print('Sua renda sera compromentida em {:.2f}%, abaixo dos 30%, portanto seu credito está aprovado'.format(comprometimento))
else: 
  print('Seu comprometimento de renda de {:.2f}% esta acima dos 30% permitido, portanto seu credito deverá ser revisto!'.format(comprometimento))
  