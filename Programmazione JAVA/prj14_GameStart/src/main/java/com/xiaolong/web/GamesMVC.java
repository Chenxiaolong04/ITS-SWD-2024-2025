package com.xiaolong.web;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.xiaolong.entities.Game;
import com.xiaolong.services.GameService;

@Controller
public class GamesMVC {
	@Autowired
	private GameService service;
	
	@GetMapping("games")//nome di un file che deve trovarsi dentro templates
	public String giochi(Model m) {
		List<Game> games = service.getGames();
		m.addAttribute("games",games);
		return"giochi"; // questo è il nome di un file html dentro templates
	}
}
