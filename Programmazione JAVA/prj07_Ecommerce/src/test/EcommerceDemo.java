package test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;


import controller.magazzinoCTRL;
import model.Prodotto;
import view.ProdottiView;

public class EcommerceDemo {

	public static void main(String[] args) throws FileNotFoundException {
		Prodotto p1=new Prodotto(1,"Maglia rossa","Abigliamento",15.54,15);
		Prodotto p2=new Prodotto(2,"Maglia blu","Abigliamento",15.54,15);
		Prodotto p3=new Prodotto(3,"Maglia verde","Abigliamento",15.54,15);
		magazzinoCTRL magazzino = new magazzinoCTRL("Magazzino di Firenze");
		magazzino.addProdotto(p1);
		magazzino.addProdotto(p2);
		magazzino.addProdotto(p3);
		List<Prodotto> prodotti=magazzino.getProdotti();
		ProdottiView vista= new ProdottiView();
		File sorgenteFile = new File("prodotti.csv");
		
		File file = new File("prodotti.html");
		PrintWriter pw = new PrintWriter(file);
		Scanner scanner =new Scanner(sorgenteFile);
		while(scanner.hasNextLine()) {
			String riga=scanner.nextLine();
			String[] pezziDiRiga=riga.split(",");
			int id=Integer.parseInt(pezziDiRiga[0]);
			String nome=pezziDiRiga[1];
			String categoria=pezziDiRiga[2];
			double prezzo=Double.parseDouble(pezziDiRiga[3]);
			int giacenza=Integer.parseInt(pezziDiRiga[4]);
			Prodotto p = new Prodotto(id, nome, categoria, prezzo, giacenza);
			magazzino.addProdotto(p);

		}
		for(Prodotto p:prodotti) {
			System.out.println(p);
			pw.println(vista.cardProdotto(p));
		}
		pw.close();
		System.out.println("File prodotto con successo");
	}

}
