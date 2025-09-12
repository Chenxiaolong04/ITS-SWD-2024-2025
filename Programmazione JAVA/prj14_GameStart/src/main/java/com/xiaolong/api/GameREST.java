package com.xiaolong.api;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.xiaolong.entities.Game;
import com.xiaolong.services.GameService;

@RestController
@RequestMapping("api")
public class GameREST {
	@Autowired
	private GameService service;
	
	public List<Game> games(){
		return service.getGames();
	}
}
