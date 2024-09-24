namespace Exercicio3;

public class ContaPoupanca : ContaBancaria{
    public double taxa;

    public void VerSaldo(){
        Console.Write($"SALDO: R${Saldo + (taxa*100)}");
    }

}