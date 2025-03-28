package gioco;

public class Dado {
	int facce=6;
	int valoreFacciaSuperiore = 1;
	void lanciaDado() {
		valoreFacciaSuperiore=(int)(Math.random()*facce)+1;
		
	}
}
