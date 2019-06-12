import java.util.ArrayList;

public class Profesional extends Persona {
	
	public String cuil;
	
	public Profesional() {
		
	}
	
	public Profesional(String nombre, String apellido, String fecha_nacimiento, String profesion, String padre, String[] hijos, String cuil) {
		super(nombre, apellido, fecha_nacimiento, profesion, padre, hijos);
	}

	public String getCuil() {
		return cuil;
	}

	public void setCuil(String cuil) {
		this.cuil = cuil;
	}

}
