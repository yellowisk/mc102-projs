N = float(input())
notes= [100, 50, 20, 10, 5, 2, 1]
hun_b = N//100
ft_b = (N%100)//50
twn_b = ((N%100)%50)//20
t_b = (((N%100)%50)%20)//10
f_b = ((((N%100)%50)%20)%10)//5
tw_b = (((((N%100)%50)%20)%10)%5)//2

o_c = ((((((N%100)%50)%20)%10)%5)%2)//1
half_c = (((((((N%100)%50)%20)%10)%5)%2)%1)//0.5
quarter_c = ((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)//0.25
dime_c = (((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)//0.1
nickel_c = ((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)//0.05
penny_c = (((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)%0.05)/0.01



print("NOTAS:")
print(f"{hun_b:.0f} nota(s) de R$ 100.00")
print(f"{ft_b:.0f} nota(s) de R$ 50.00")
print(f"{twn_b:.0f} nota(s) de R$ 20.00")
print(f"{t_b:.0f} nota(s) de R$ 10.00")
print(f"{f_b:.0f} nota(s) de R$ 5.00")
print(f"{tw_b:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{o_c:.0f} moeda(s) de R$ 1.00")
print(f"{half_c:.0f} moeda(s) de R$ 0.50")
print(f"{quarter_c:.0f} moeda(s) de R$ 0.25")
print(f"{dime_c:.0f} moeda(s) de R$ 0.10")
print(f"{nickel_c:.0f} moeda(s) de R$ 0.05")
print(f"{penny_c:.0f} moeda(s) de R$ 0.01")