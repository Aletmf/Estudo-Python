namespace Exercicio3;

public class ContaBancaria{
    public int NumeroConta {get; set;}
    public double Saldo {get; set;}    
    public string NomeTitular {get; set;}   

    public virtual void AbrirConta(double depositoInicial){
        Saldo = depositoInicial;
        VerSaldo();
    }

    public void Depositar(double Deposito){
        Saldo += Deposito;
        VerSaldo();
    }
    public virtual void Sacar(double Saque){
        Saldo -= Saque;
        VerSaldo();
    }

    public void VerSaldo(){
        Console.Write($"SALDO: R${Saldo:F}");
    }
}