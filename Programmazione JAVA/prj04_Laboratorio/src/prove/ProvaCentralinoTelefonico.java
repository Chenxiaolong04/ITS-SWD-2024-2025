package prove;

import java.util.Scanner;

public class ProvaCentralinoTelefonico {
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		boolean gira=true;
		giovanni(input,gira);
	}
	
	private static void giovanni(Scanner input, boolean gira) {
		while(gira) {
			menu();
			String risposta = input.nextLine();
			switch(risposta) {
			case "1":
				System.out.println("Sono l'operatore jimmy, dimmi");
				break;
			case "2":
				System.out.println("Il tuo saldo è 3 euro");
				break;
			case "3":
				System.out.println("Creadito ricaricato");
				break;
			case "4":
				System.out.println("Contratto modificato");
				break;
			case "0":
				break;
			default:
				System.out.println("Scelta non disponibile");
				break;
			}
		}		
	}

	private static void menu() {
		System.out.println("1. Parlare con un operatore");
		System.out.println("2. Conoscere il tuo salto");
		System.out.println("3. Ricarica cellulare");
		System.out.println("4. Nuovo contratto");
		System.out.println("0. Terminare la chiamata");
	}
	
}
