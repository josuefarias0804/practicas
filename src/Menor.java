import java.util.ArrayList;

public class Menor extends Persona {
	
	public Menor(String nombre, String apellido, String fecha_nacimiento, String padre, String[] hijos) {
		super(nombre, apellido, fecha_nacimiento, profesion, padre, hijos);
	}
	
	public void agregarHijos(Persona persona) {
		try {
			if(persona.edad(fecha_nacimiento) > 18) {
				
			}
			catch(Exception e){
				System.out.println("Un menor no puede tener hijos");
			}
		}
	}

}
