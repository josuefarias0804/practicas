import java.time.Period;

public class Ejercicio1 {

	public static void main(String[] args) {
		
		Persona p = new Persona("Carlos", "Sanchez", "12/12/1980", "carpintero");
				
		System.out.println("La profesi�n de " + p.getNombreCompleto(p) + " es " + p.getProfesion() + " y tiene " + p.edad(p.getFecha_nacimiento()) + " a�os de edad");
		
	}

}
