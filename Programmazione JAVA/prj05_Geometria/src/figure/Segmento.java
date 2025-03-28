package figure;


public class Segmento {
	public Punto a,b;
	public Segmento(Punto a,Punto b) {
		//alt+shift+s
		this.a=a;
		this.b=b;
	}
	public double lunghezza() {
		return Math.sqrt(Math.pow(a.x- b.x,2)+Math.pow(a.y-b.y, 2));
	}
	@Override
	public String toString() {
		return "Segmento [a=" + a + ", b=" + b + "]";
	}

	
}
