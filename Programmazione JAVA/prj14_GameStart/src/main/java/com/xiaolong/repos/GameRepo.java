package com.xiaolong.repos;

import org.springframework.data.jpa.repository.JpaRepository;

import com.xiaolong.entities.Game;

public interface GameRepo extends JpaRepository<Game, Integer>{

}
