package com.xiaolong.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.xiaolong.services.ProdottoService;

@Controller
public class ProdottiMVC {
	@Autowired
	private ProdottoService service;
	@GetMapping("prodotti")
	public String prodotti(Model m) {
		m.addAttribute("prodotti",service.getProdotti());
		return "prodotti";
	}
	@GetMapping("prodotti/categoria/{categoria}")
	public String proottiByCat(@PathVariable String categoria) {
		
		return "prodotti";
	}
	
}
