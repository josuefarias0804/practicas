import java.awt.List;
import java.sql.Date;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Calendar;

public class Persona {
	
	private String nombre;
	private String apellido;
	protected String fecha_nacimiento;
	protected static String profesion;
	private String padre;
	//private String[] hijos = new String[2];
	private String[] hijos;
		
	public Persona() {
		
	}

	
	public Persona(String nombre, String apellido, String fecha_nacimiento, String profesion, String padre, String[] hijos) {
		
		this.nombre = nombre;
		this.apellido = apellido;
		this.fecha_nacimiento = fecha_nacimiento;
		this.profesion = profesion;
		this.padre = padre;
		this.hijos = hijos;
		//this.hijos.add("olmedo");
				
	}
	
	public int edad(String fecha_nacimiento) {     
		   
	    Date fechaActual = new Date(0);
	    SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yyyy");
	    String hoy = formato.format(fechaActual);
	    String[] dat1 = fecha_nacimiento.split("/");
	    String[] dat2 = hoy.split("/");
	    int anos = Integer.parseInt(dat2[2]) - Integer.parseInt(dat1[2]);
	    int mes = Integer.parseInt(dat2[1]) - Integer.parseInt(dat1[1]);
	    if (mes < 0) {
	      anos = anos - 1;
	    } else if (mes == 0) {
	      int dia = Integer.parseInt(dat2[0]) - Integer.parseInt(dat1[0]);
	      if (dia > 0) {
	        anos = anos - 1;
	      }
	    }
	    return anos;
	  }
	
	
	public void agregarHijos() {
		
	}
	
	public String decirHola() {
		
		Profesional pr = new Profesional();	
		
		return "Hola!, soy una persona y me llamo ";
	}
	
	public String getNombreCompleto(Persona persona) {
		
		return persona.getNombre() + " " + persona.getApellido();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellido() {
		return apellido;
	}

	public void setApellido(String apellido) {
		this.apellido = apellido;
	}

	public String getFecha_nacimiento() {
		return fecha_nacimiento;
	}

	public void setFecha_nacimiento(String fecha_nacimiento) {
		this.fecha_nacimiento = fecha_nacimiento;
	}

	public String getProfesion() {
		return profesion;
	}

	public void setProfesion(String profesion) {
		this.profesion = profesion;
	}
	
	public String getPadre() {
		return padre;
	}

	public void setPadre(String padre) {
		this.padre = padre;
	}

	public String[] getHijos() {
		return hijos;
	}

	public void setHijos(String[] hijos) {
		this.hijos = hijos;
	}

}
