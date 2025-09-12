package com.xiaolong.services;

import java.util.List;

import com.xiaolong.entities.Automobile;
import com.xiaolong.entities.Moto;

public interface AutosaloneService {
	//crud
	//create
	List<Automobile> getAutomobili();
	//read
	Automobile addAutomobile(Automobile a);
	//update
	
	//delete
	
	List<Moto> getMoto();
	Moto addMoto(Moto m);
}
