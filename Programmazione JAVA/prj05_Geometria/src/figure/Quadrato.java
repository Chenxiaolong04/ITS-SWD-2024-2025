package figure;

public class Quadrato extends rettangolo{
	private Segmento lato;
	/**
	 * Costruttore del quadrato: prima costruisco il
	 * rettangolo passando 2 volte il lato del quadrato
	 * 
	 * @param lato
	 */
	public Quadrato(Segmento lato) {
		super(lato, lato);//costruisco il rettangolo passando 2 volte lato
		this.lato=lato;
	}
	@Override
	public String toString() {
		return "Quadrato [perimetro()=" + perimetro() + ", area()=" + area() + "]";
	}
	@Override
	public double perimetro() {
		System.out.println("Metodo di quadrato");
		return lato.lunghezza()*4;
	}

}
