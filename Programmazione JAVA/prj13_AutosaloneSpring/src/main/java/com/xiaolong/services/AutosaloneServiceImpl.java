package com.xiaolong.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.xiaolong.entities.Automobile;
import com.xiaolong.entities.Moto;
import com.xiaolong.repos.AutomobileRepo;
import com.xiaolong.repos.MotoRepo;

@Service
public class AutosaloneServiceImpl implements AutosaloneService{
	
	@Autowired
	private AutomobileRepo repo;
	
	@Autowired
	private MotoRepo repoMoto;
	
	@Override
	public List<Automobile> getAutomobili(){
		
		return repo.findAll();
	}
	
	@Override
	public List<Moto> getMoto(){
		
		return repoMoto.findAll();
	}

	@Override
	public Automobile addAutomobile(Automobile a) {
		// TODO Auto-generated method stub
		return repo.save(a);
	}

	@Override
	public Moto addMoto(Moto m) {
		// TODO Auto-generated method stub
		return repoMoto.save(m);
	}
}

