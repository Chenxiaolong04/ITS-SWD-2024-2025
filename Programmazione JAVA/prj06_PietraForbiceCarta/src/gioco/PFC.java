package gioco;

import java.util.Random;
import java.util.Scanner;

public class PFC {

	public static void main(String[] args) {
		String[] scelte= {"Pietra","Forbice","Carta"};
		String sceltaUmano = sceltaUmano(scelte);
		String sceltaMacchina=sceltaMacchina(scelte);
		System.out.println("Scelta umano: "+sceltaUmano);
		System.out.println("Scelta macchina: "+sceltaMacchina);
        String risultato = determinaVincitore(sceltaUmano, sceltaMacchina);
        System.out.println(risultato);
	}

	private static String sceltaMacchina(String[] scelte) {
		Random rand = new Random();
		int casuale=rand.nextInt(0,scelte.length);
		
		return scelte[casuale];
	}

	private static String sceltaUmano(String[] scelte) {
		System.out.println("Scegli tra: ");
		for(String scelta : scelte) {
			System.out.println(scelta);
		}
		Scanner input = new Scanner(System.in);
		String risposta= input.nextLine();
		
		return risposta;
	}
	private static String determinaVincitore(String sceltaUmano, String sceltaMacchina) {
        if (sceltaUmano.equalsIgnoreCase(sceltaMacchina)) {
            return "Pareggio!";
        }

        if ((sceltaUmano.equalsIgnoreCase("Pietra") && sceltaMacchina.equalsIgnoreCase("Forbice")) ||
            (sceltaUmano.equalsIgnoreCase("Forbice") && sceltaMacchina.equalsIgnoreCase("Carta")) ||
            (sceltaUmano.equalsIgnoreCase("Carta") && sceltaMacchina.equalsIgnoreCase("Pietra"))) {
            return "Hai vinto!";
        } else {
            return "Hai perso!";
        }
    }
}
