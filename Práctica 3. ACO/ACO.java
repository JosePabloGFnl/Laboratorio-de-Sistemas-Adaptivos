/* Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Laboratorio de Programacion de Sistemas Adaptativos
 Ant Colont Optimization */
import java.util.*;

public class ACO
{
    int numCiudades;
    int numHormigas;
    int iteraciones;
    
    double tasaEvaporacion;
    
    int[][] costos={{0,20,10,33,2,8},{20,0,6,15,3,5},{10,6,0,24,13,23},{33,15,24,0,7,17},{2,3,13,7,0,22},{8,5,23,17,22,0}};
    
    String[] labels={"VR","IB","H","F","S","K"};
    
    double[][] feromona;
    int[][] aristasRecorridas; //Cuantas veces pasa cada hormiga por una arista
    
    Vector visitadas; //ciudades que han sido visitadas
    int ciudadInicialRecorrido;
    
    String mejorRecorrido;
    double mejorCosto;
	
   /* Constructor */
  public ACO(int numHormigas, double tasaEvaporacion, int iteraciones)
    {
        this.numHormigas=numHormigas;
        this.tasaEvaporacion=tasaEvaporacion;
        this.iteraciones=iteraciones;
        
        numCiudades=costos.length;
        inicializaFeromona();
        inicializaAristasRecorridas();
        
        mejorRecorrido="";
        mejorCosto=Double.MAX_VALUE; //Asignamos a costo un numero muy grande
    }
    
    
    public void inicializaFeromona()
    {
        int i, j;
        
        feromona=new double[numCiudades][numCiudades];
        
        for(i=0;i<feromona.length;i++)
            for(j=0;j<feromona.length;j++)
                feromona[i][j]=1.0;
    }
    
    public void inicializaAristasRecorridas()
    {
        
        aristasRecorridas=new int[numCiudades][numCiudades];
        
        limpiaAristasRecorridas();
        
    }
    
    public void limpiaAristasRecorridas()
    {
        int i, j;

        for(i=0;i<aristasRecorridas.length;i++)
            for(j=0;j<aristasRecorridas.length;j++)
                aristasRecorridas[i][j]=0;

    }
    
    /* Evaporacion y deposito de feromona */
    public void actualizaFeromona()
    {
        int i,j;
        
        for(i=0;i<feromona.length;i++)
            for(j=0;j<feromona.length;j++)
                feromona[i][j]=feromona[i][j]*(1-tasaEvaporacion)+aristasRecorridas[i][j]*(1.0/numCiudades);
    }
    
    public void realizaRecorrido()
    {
        int i, ciudadInicial, ciudadDestino;
        double costo, costoTotal;
        Vector candidatas;
        String recorrido="";
        
        visitadas=new Vector();
        
        ciudadInicialRecorrido=Utils.obtenAleatorio(0,numCiudades-1);
        
        costoTotal=0.0;
        
        ciudadInicial=ciudadInicialRecorrido;
        System.out.println("Ciudad inicial: " + labels[ciudadInicial]);
        
		//Mientras que no se haya completado el recorrido...
        while(visitadas.size()<numCiudades+1)
        {
			
			//System.out.println("Agregando " + labels[ciudadInicial] + " a visitadas");
            recorrido+=String.valueOf(labels[ciudadInicial] + " ");
			
            candidatas=new Vector();
            visitadas.add(ciudadInicial);
        
            for(i=0;i<costos.length;i++)
                if(!visitadas.contains(i))
                {
                    candidatas.add(i);
                    //System.out.println(labels[i]);
                }
        
            if(candidatas.size()==0) //no quedan ciudades por visitar, volver a ciudad inicial (cerrar recorrido)
                ciudadDestino=ciudadInicialRecorrido;
            else if(candidatas.size()==1) //solo queda una opcion disponible (no es necesario hacer seleccion)
                ciudadDestino=((Integer)candidatas.get(0)).intValue();
            else
                ciudadDestino=seleccionarArista(ciudadInicial, candidatas);
            
            costo=costos[ciudadInicial][ciudadDestino];
            costoTotal+=costo;
            
		if(ciudadInicial!=ciudadDestino)
		{
            aristasRecorridas[ciudadInicial][ciudadDestino]++;
            aristasRecorridas[ciudadDestino][ciudadInicial]++;
		}
			
			//System.out.println(ciudadInicial + "," + ciudadDestino);
        
            ciudadInicial=ciudadDestino;
        }
        
        System.out.println("Recorrido: " + recorrido);
        System.out.println("Costo: " + costoTotal);
        
        if(costoTotal<mejorCosto)
        {
            mejorCosto=costoTotal;
            mejorRecorrido=recorrido;
            System.out.println("++ Se logro mejorar el costo ++");
        }
        
        System.out.println("==========");
        System.out.println();
    }
    
	/* Seleccion de arista por la hormiga */
    public int seleccionarArista(int ciudadInicial, Vector candidatas)
    {
        int i, candidata;
        double aptitud, aptitudTotal, probabilidadSeleccion, aleatorio, rango;
        Hashtable aptitudes=new Hashtable();
        
        aptitudTotal=0.0;
        
		/* CALCULAR APTITUD Y APTITUD TOTAL */
        for(i=0;i<candidatas.size();i++)
        {
            candidata=((Integer)candidatas.get(i)).intValue();
            aptitud=feromona[ciudadInicial][candidata]*(1.0/costos[ciudadInicial][candidata]);
            
            //System.out.println(ciudadInicial + "," + candidata);
            //System.out.println(labels[candidata] + "," + feromona[ciudadInicial][candidata] + "," + costos[ciudadInicial][candidata] + "," + 1.0/costos[ciudadInicial][candidata] + "," + aptitud);
            
            aptitudTotal+=aptitud;
            
            aptitudes.put(candidata,aptitud);
        }
        
        Enumeration keys=aptitudes.keys();
        
		/* CALCULAR PROBABILIDAD DE SELECCION */
        while(keys.hasMoreElements())
        {
            candidata=((Integer)keys.nextElement()).intValue();
            aptitud=((Double)aptitudes.get(candidata)).doubleValue();
            aptitud=aptitud/aptitudTotal;
            
            //System.out.println(labels[candidata] + " " + String.valueOf(aptitud));
            
            aptitudes.put(candidata,aptitud);
        }
        
		//RULETA DE SELECCION
        aleatorio=Math.random();
        rango=0;
        
		/* GIRO DE RULETA */
		/* Voy a llegar hasta el limite de la porcion que le toca a la arista.
		 Si el aleatorio cae en ese rango (menor o igual a), escogo la candidata, si no, le sumo la aptitud de la siguiente arista y se repite el proceso con una nueva candidata. */
        for(i=0;i<candidatas.size();i++)
        {
            candidata=((Integer)candidatas.get(i)).intValue();
            aptitud=((Double)aptitudes.get(candidata)).doubleValue();
            
            rango+=aptitud;
            
            if(aleatorio<=rango)
            {
                //System.out.println(aleatorio + "," + rango + "," + labels[candidata]);

                return candidata;
            }
                
        }
        
        return 0;
    }
    
    public void correr()
    {
        int i,j;
        
        imprimeMatrices();
        
        for(j=0;j<iteraciones;j++)
        {
            System.out.println("********** ITERACION " + j + " **********");
            
            for(i=0;i<numHormigas;i++)
            {
                System.out.println("===== Hormiga " + i + "=====");
                realizaRecorrido();
            }
            
            actualizaFeromona();
            
            imprimeMatrices();
            
            limpiaAristasRecorridas();
            
            System.out.println("********************");
        }
        
    }

    
    public String obtenMejorRecorrido()
    {
        return mejorRecorrido;
    }
    
    public double obtenMejorCosto()
    {
        return mejorCosto;
    }
    
    public void imprimeMatrices()
    {
        System.out.println("** MATRIZ DE FEROMONA **");
        
        Utils.imprimir(feromona);
        
        System.out.println("** MATRIZ DE ARISTAS RECORRIDAS **");
        
        Utils.imprimir(aristasRecorridas);
    }
    
    public static void main(String args[])
    {
        int numeroHormigas=2;
        double tasaEvaporacion=0.5;
        int numeroIteraciones=5;
        
        String mejorRecorrido;
        double mejorCosto;
        
        ACO a=new ACO(numeroHormigas,tasaEvaporacion,numeroIteraciones);
        a.correr();
        mejorRecorrido=a.obtenMejorRecorrido();
        mejorCosto=a.obtenMejorCosto();
        
        System.out.println("MEJOR RECORRIDO ENCONTRADO: " + mejorRecorrido);
        System.out.println("MEJOR COSTO ENCONTRADO: " + mejorCosto);
    }
}