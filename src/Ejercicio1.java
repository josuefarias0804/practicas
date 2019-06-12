import java.time.Period;
import java.util.ArrayList;
import java.util.Arrays;

public class Ejercicio1 {

	public static void main(String[] args) {
		
		Persona per = new Persona();
		
		String[] hijos = {"Thomas","Emiliano","Patricio"};
		
		Persona p = new Persona("Carlos", "Sanchez", "12/12/1980", "carpintero", "yo", hijos);
		
		Persona saludar = new Persona();
		Profesional pr = new Profesional();	
		pr.setCuil("20343219262");
				
		System.out.println("La profesión de " + p.getNombreCompleto(p) + " es " + p.getProfesion() + " y tiene " + p.edad(p.getFecha_nacimiento()) + " años de edad " + p.getHijos());
		System.out.println(saludar.decirHola() + p.getNombreCompleto(p) + " y mi CUIL es " + pr.getCuil());
	}

}
