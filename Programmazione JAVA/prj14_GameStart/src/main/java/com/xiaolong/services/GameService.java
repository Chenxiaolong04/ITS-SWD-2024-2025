package com.xiaolong.services;

import java.util.List;

import com.xiaolong.entities.Game;

public interface GameService {
	List<Game> getGames();
	List<Game> getGameByPublisher(String publisher);
	Game getGameById();
}
