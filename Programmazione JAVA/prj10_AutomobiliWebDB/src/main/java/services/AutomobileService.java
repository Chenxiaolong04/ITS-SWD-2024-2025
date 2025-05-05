package services;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import model.Automobile;
import repos.AutomobileDAO;

public class AutomobileService {

    private AutomobileDAO dao = new AutomobileDAO(); // CORRETTO

    public List<Automobile> getAutomobili() {
        Map<Integer, Automobile> automobili = dao.getAutomobili();
        Collection<Automobile> values = automobili.values();
        
        // Aggiungi gli elementi della collection alla lista
        List<Automobile> auto = new ArrayList<>(values); // Utilizza il costruttore ArrayList che accetta una collezione
        
        return auto;
    }
}
