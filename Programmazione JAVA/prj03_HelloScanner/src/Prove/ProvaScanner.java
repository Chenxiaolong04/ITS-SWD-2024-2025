package Prove;

import java.util.Scanner;

public class ProvaScanner {

	public static void main(String[] args) {
		System.out.print("Inserisci il tuo nome: ");
		Scanner scanner1 = new Scanner(System.in);
		String nome=scanner1.nextLine();
		System.out.println("Ciao "+nome);
		
		System.out.print("Username: ");
		Scanner username = new Scanner(System.in);
		String user=username.nextLine();

		System.out.print("Password: ");
		Scanner password = new Scanner(System.in);
		String pass=password.nextLine();

		if(user.equals("xiaolong")&&pass.equals("12345")) {
			System.out.println("Sei loggato");
		}else {
			System.out.println("Non sei loggato");

		}
	}

}
