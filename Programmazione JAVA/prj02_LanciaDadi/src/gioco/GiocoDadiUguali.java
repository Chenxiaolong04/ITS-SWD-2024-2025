package gioco;

public class GiocoDadiUguali {
	public static void main(String[] args) {
	Dado dado1 = new Dado();
	Dado dado2 = new Dado();
	final int NUM_LANCI = 10_000_000; //final serve per dichiarare una costante
	int vittorie=0;
	long start = System.currentTimeMillis();
	for(int i=0; i<NUM_LANCI;i++) {
		dado1.lanciaDado();
		dado2.lanciaDado();
		//System.out.println("Il valore di dado 1: "+dado1.valoreFacciaSuperiore);
		//System.out.println("Il valore di dado 2: "+dado2.valoreFacciaSuperiore);
		if (dado1.valoreFacciaSuperiore==dado2.valoreFacciaSuperiore) {
			//System.out.println("Hai vinto");
			vittorie++;
		}else {
			//System.out.println("Non hai vinto");
		}
	}
	long stop = System.currentTimeMillis();
	float tempoImpiegato = stop-start;
	double percentuale = (double) vittorie/NUM_LANCI*100;
	System.out.println("Numero di partite: "+NUM_LANCI);
	System.out.println("Numero di vittorie: "+vittorie);
	System.out.println("Percentuale: "+percentuale);
	System.out.println("Tempo impiegato: "+tempoImpiegato/1000+" secondi");
	}
}