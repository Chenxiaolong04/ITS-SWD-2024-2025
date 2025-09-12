package com.xiaolong.services;

import java.util.List;

import com.xiaolong.entities.Prodotto;
import com.xiaolong.repos.ProdottoDAO;

public interface ProdottoService {
	
	List<Prodotto> getProdotti();
	
	Prodotto getProdottoById(int id);
	
	Prodotto addProdotto(Prodotto p);
	Prodotto updateProdotto(Prodotto p);
	void deleteProdotto(int id);
}
