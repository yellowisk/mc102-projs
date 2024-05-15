N = int(input())
hun_b = N//100
ft_b = (N%100)//50
twn_b = ((N%100)%50)//20
t_b = (((N%100)%50)%20)//10
f_b = ((((N%100)%50)%20)%10)//5
tw_b = (((((N%100)%50)%20)%10)%5)//2
o_b = ((((((N%100)%50)%20)%10)%5)%2)//1


print(str(N))
print("{} nota(s) de R$ 100,00".format(hun_b))
print("{} nota(s) de R$ 50,00".format(ft_b))
print("{} nota(s) de R$ 20,00".format(twn_b))
print("{} nota(s) de R$ 10,00".format(t_b))
print("{} nota(s) de R$ 5,00".format(f_b))
print("{} nota(s) de R$ 2,00".format(tw_b))
print("{} nota(s) de R$ 1,00".format(o_b))