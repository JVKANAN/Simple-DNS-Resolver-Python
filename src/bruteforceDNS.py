import dns.resolver

res = dns.resolver.Resolver()

alvo = input("Digite o domínio que deseja consultar: ")

try:
    resultado = res.resolve(alvo, "A")

    for ip in resultado:
        print(alvo, "->", ip)

except:
    print("Erro ao consultar o DNS para o domínio especificado.")
