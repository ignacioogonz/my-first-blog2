$(function()
{
    var soloNumero= '+0123456789';
    var soloLetras= 'qwertyuiopasdfghjklñzxcvbnm'+
                    'QWERTYUIOPASDFGHJKLÑZXCVBNM'+
                    'áéíóúÁÉÍÓÚ ' +
                    "'";
    $('.soloNumero').keypress (function(e)
    {
        var caracterPresionado = String.fromCharCode(e.which);
        if(soloNumero.indexOf(caracterPresionado)<0)
            return false;

    });

    $('.soloLetras').keypress (function(e)
    {
        var caracterPresionado = String.fromCharCode(e.which);
        if(soloLetras.indexOf(caracterPresionado)<0)
            return false;

    });
});

function validar_email( email ) 
{
    var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email) ? true : false;

   
}

var opt_1 = new Array ("Seleccione una ciudad", "Arica");
        var opt_2 = new Array ("Seleccione una ciudad", "Iquique","Alto Hospicio", "Pozo Almonte");
        var opt_3 = new Array ("Seleccione una ciudad", "Antofagasta", "Calama", "Tocopilla", "Taltal","Mejillones","Maria Elena");
        var opt_4 = new Array ("Seleccione una ciudad", "Copiapó", "Caldera", "Tierra Amarilla", "Chañaral","Diego de Almagro","El Salvador","Vallenar","Huasco");
        var opt_5 = new Array ("Seleccione una ciudad", "La Serena","Coquimbo", "Puntaqui", "Andacollo", "Vicuña","Illapel","Los Vios","Salamnca","Ovalle","Combarbála","Monte Patria","El Palqui");
        var opt_6 = new Array ("Seleccione una ciudad", "Valparaiso","Concón","Viña del Mar","Villa Alemana","Quilpué","Placilla de Peñuelas", "San Antonio","Santo Domingo","Cartagena", "Quillota","Hijuelas","La Calera","La Cruz", "San Felipe", "Casablanca", "Las Ventanas", "Quintero", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Limache", "Nogales", "El Melón", "Olmué", "Algarrobo", "El Quisco", "El Tabo", "Catemu", "Llaillay", "Putaendo", "Villa Los Almendros", "Santa María");
        var opt_7 = new Array ("Seleccione una ciudad", "Rancagua","Machalí","Gultro", "Codegua", "Doñihue", "Lo Miranda", "Graneros", "Las Cabras", "San Francisco de Mostazal", "Peumo", "Punta Diamante", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente de Tagua Tagua", "Pichilemu", "San Fernando", "Chimbarongo", "Nancagua", "Palmilla", "Santa Cruz");
        var opt_8 = new Array ("Seleccione una ciudad", "Talca", "Curicó", "Linares", "Constitución", "San Clemente", "Cauquenes", "Hualañé", "Molina", "Teno", "Longaví", "Parral", "San Javier", "Villa Alegre");
        var opt_9 = new Array ("Seleccione una ciudad", "Concepción","Talcahuano","Chiguayante","Coronel","Hualqui","Lota","Penco","","Tomé","Hualpén","San Pedro de la Paz", "Santa Juana", "Chillán","Chillán Viejo", "Los Ángeles", "Lebu", "Arauco", "Cañete", "Curanilahue", "Los Álamos", "Cabrero", "Monte Águila", "La Laja", "San Rosendo", "Mulchén", "Nacimiento", "Santa Bárbara", "Huépil", "Yumbel", "Bulnes", "Coelemu", "Coihueco", "Quillón", "Quirihue", "San Carlos", "Yungay");
        var opt_10 = new Array ("Seleccione una ciudad", "Temuco", "Padre Las Casas", "Labranza", "Carahue", "Cunco", "Freire", "Gorbea", "Lautaro", "Loncoche", "Nueva Imperial", "Pitrufquén", "Pucón", "Villarrica", "Angol", "Collipulli", "Curacautín", "Purén", "Renaico", "Traiguén", "Victoria");
        var opt_11 = new Array ("Seleccione una ciudad", "Valdivia", "Futrono", "La Unión", "Lanco", "Los Lagos", "San José de la Mariquina", "Paillaco", "Panguipulli", "Río Bueno");
        var opt_12 = new Array ("Seleccione una ciudad", "Puerto Montt", "Puerto Varas", "Calbuco", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Castro", "Ancud", "Quellón", "Osorno", "Purranque", "Río Negro");
        var opt_13 = new Array ("Seleccione una ciudad", "Coyhaique", "Puerto Aysén");
        var opt_14 = new Array ("Seleccione una ciudad", "Punta Arenas", "Puerto Natales");
        var opt_15 = new Array ("Seleccione una ciudad", "Santiago", "Cerrillos", "Cerro Navia", " Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "San Bernardo", "Padre Hurtado", "Pirque", "San José de Maipo", "Colina", "Lampa", "Batuco", "Tiltil", "Buin", "Alto Jahuel", "Bajos de San Agustín", "Paine", "Hospital", "Melipilla", "Curacaví", "Calera de Tango", "Talagante", "El Monte", "Isla de Maipo", "La Islita", "Peñaflor");

        
        function cambia(){
            var cosa;

            cosa = document.formulario1.cosa[document.formulario1.cosa.selectedIndex].value;

            if(cosa!=0){

                mis_opts=eval("opt_" + cosa);

                num_opts=mis_opts.length;

                document.formulario1.opt.length = num_opts;

                for(i=0; i<num_opts; i++){
                    document.formulario1.opt.options[i].value=mis_opts[i];
                    document.formulario1.opt.options[i].text=mis_opts[i];
                }
                }else{

                    document.formulario1.opt.length = 1;

                    document.formulario1.opt.options[0].value="-";
                    document.formulario1.opt.options[0].text="-";
                }

                document.formulario1.opt.options[0].selected = true;
                
            }



            function checkRut(rut) {

                var valor = rut.value.replace('.','');

                valor = valor.replace('-','');
                

                cuerpo = valor.slice(0,-1);
                dv = valor.slice(-1).toUpperCase();

                rut.value = cuerpo + '-'+ dv
                

                if(cuerpo.length < 7) { rut.setCustomValidity("RUT Incompleto"); return false;}
                

                suma = 0;
                multiplo = 2;
                

                for(i=1;i<=cuerpo.length;i++) {
                

                    index = multiplo * valor.charAt(cuerpo.length - i);
                    
                    // Sumar al Contador General
                    suma = suma + index;
                    
                    // Consolidar Múltiplo dentro del rango [2,7]
                    if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
              
                }
                
                // Calcular Dígito Verificador en base al Módulo 11
                dvEsperado = 11 - (suma % 11);
                
                // Casos Especiales (0 y K)
                dv = (dv == 'K')?10:dv;
                dv = (dv == 0)?11:dv;
                
                // Validar que el Cuerpo coincide con su Dígito Verificador
                if(dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }
                
                // Si todo sale bien, eliminar errores (decretar que es válido)
                rut.setCustomValidity('');
            }