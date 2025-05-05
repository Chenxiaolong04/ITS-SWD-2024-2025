package repos;

import java.util.HashMap;
import java.util.Map;
import model.Automobile;

public class AutomobileDAO {

    public Map<Integer, Automobile> getAutomobili() {

        Map<Integer, Automobile> mappa = new HashMap<>(); // creo la mappa 

        Automobile auto1 = new Automobile(); // creo oggetto auto1 tipo Automobile

        // inizializzo le proprietà
        auto1.setId(1);
        auto1.setMarca("bmw");
        auto1.setModello("25");
        auto1.setCilindrata(3500);  // Correzione qui
        auto1.setPosti(5);
        auto1.setPrezzo(12000);

        mappa.put(auto1.getId(), auto1);

        return mappa;
    }
}
