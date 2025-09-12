package com.xiaolong.repos;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.xiaolong.entities.Automobile;

@Repository
public interface AutomobileRepo extends JpaRepository<Automobile, Integer>{

}
