package controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.Automobile;
import services.AutomobileService;

import java.io.IOException;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Servlet implementation class AutosaloneREST
 */
@WebServlet("/api")
public class AutosaloneREST extends HttpServlet {
	
	private AutomobileService service = new AutomobileService();

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		List<Automobile> automobili = service.getAutomobili();
		
		JSONArray array = new JSONArray();
		for (Automobile auto : automobili) {
			JSONObject obj = new JSONObject();
			obj.put("id", auto.getId());
			obj.put("marca", auto.getMarca());
			obj.put("modello", auto.getModello());
			obj.put("cilindrata", auto.getCilindrata());
			obj.put("posti", auto.getPosti());
			obj.put("prezzo", auto.getPrezzo());
			array.put(obj);
		}
		
		// Impostazione corretta del tipo di contenuto
		response.setContentType("application/json");
		response.getWriter().print(array.toString());
	}
}
