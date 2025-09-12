package com.xiaolong.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity //dice a spring che questa classe corrisponde ad una classe in sql
@Table(name="prodotti")//serve per dire che la tabella si chiama prodotti e non prodotto perchè altrimenti senza questa riga spring va a cercare la tabella prodotto visto che si chiama cosi la classe
public class Prodotto {
	@Id//serve per dire che la cosa che c'è subito dopo è una primary key 
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	private String nome;
	private String categoria;
	private double prezzo;
	private int giacenza;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCategoria() {
		return categoria;
	}
	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}
	public double getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}
	public int getGiacenza() {
		return giacenza;
	}
	public void setGiacenza(int giacenza) {
		this.giacenza = giacenza;
	}
}
