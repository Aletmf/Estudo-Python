namespace Exercicio3;

public class ContaEspecial : ContaBancaria{
    private double Limite;

    public override void AbrirConta(double depositoInicial){
        Limite = 2 * depositoInicial;
    }

    public override void Sacar(double Saque){
        if (Saque > Limite){
            Console.Write("LIMITE INDISPONÍVEL.");
        }
        else{
            VerSaldo();
            base.Sacar(Saque);
        }
    }
}
