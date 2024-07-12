print("---------------------------------")
print("Calculadora de Partidas Rankeadas")
print("---------------------------------")

VitoriaJogador = int(input("Digite o número de vitórias: "))
DerrotaJogador = int(input("Digite o número de derrotas: "))


def CalculoPartida(vitorias, derrotas):
    SaldoVitorias = vitorias - derrotas
    return SaldoVitorias

saldo = CalculoPartida(VitoriaJogador, DerrotaJogador)

def Classificacao(saldo):
    if saldo <= 10 and saldo <= 20:
        return "Ferro"
    elif saldo >= 11 and saldo <= 20:
        return "Bronze"
    elif saldo >= 21 and saldo <= 50:
        return "Prata"
    elif saldo >= 51 and saldo <= 80:
        return "Ouro"
    elif saldo >= 81 and saldo <= 90:
        return "Diamante"
    elif saldo >= 91 and saldo <= 100:
        return "Lendário"
    elif saldo > 100:
        return "Imortal"
  
classificacao = Classificacao(saldo)


print(f"O Herói tem saldo de vitórias {saldo} e está no nível {classificacao}")
