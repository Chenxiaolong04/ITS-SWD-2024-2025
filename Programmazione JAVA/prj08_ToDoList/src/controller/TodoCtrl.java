package controller;

import java.util.ArrayList;
import java.util.List;

import model.Todo;

public class TodoCtrl {
	private List<Todo> todos =new ArrayList<>();
	public void addTodo(Todo t) {//chiamo qui
		todos.add(t);
	}
	//overload del metodo addTodo()
	public void addTodo(String desc) {
		Todo t = new Todo(desc);
		todos.add(t);
		addTodo(t);//da qui chiamo sopra
	}
	public List<Todo> getTodos() {
		return todos;
	} 
	public List<Todo> getTodosCompleti() {
		List<Todo> todoCompleti = new ArrayList<Todo>();//scatola vuota
		for(Todo t:todos) {
			if(t.isDone()) {
				todoCompleti.add(t);
			}
		}
		return todoCompleti;
	} 
}
