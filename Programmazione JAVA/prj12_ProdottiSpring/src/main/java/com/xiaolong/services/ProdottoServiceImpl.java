package com.xiaolong.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.xiaolong.entities.Prodotto;
import com.xiaolong.repos.ProdottoDAO;

@Service
public class ProdottoServiceImpl implements ProdottoService{
	@Autowired
	private ProdottoDAO dao;
	
	@Override
	public List getProdotti() {
	    return dao.findAll();
	}


	@Override
	public Prodotto getProdottoById(int id) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Prodotto addProdotto(Prodotto p) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Prodotto updateProdotto(Prodotto p) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void deleteProdotto(int id) {
		// TODO Auto-generated method stub
		
	}
	List<Prodotto> listaList= new Arraylist<>();
	
}
