package controller;


import java.util.ArrayList;
import java.util.List;

import model.Prodotto;

public class magazzinoCTRL {
	
	private String nome;
	private List<Prodotto> prodotti;
	
	public magazzinoCTRL(String nome) {
		super();
		this.nome = nome;
		prodotti=new ArrayList<>();
	}
	public void addProdotto(Prodotto p) {
		prodotti.add(p);
	}
	public List<Prodotto> getProdotti() {
		return prodotti;
	}
}
