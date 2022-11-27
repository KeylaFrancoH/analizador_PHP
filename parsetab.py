
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AND_SYMB ARRAY AS ASIG_CONCA ASIG_REFER BOOLEANO BREAK CADENA CALLABLE CASE CATH CLASS CLONE COMA COMENTARIO CONST CONTINUE CORCH_DER CORCH_IZQ COUNT CURRENT DECLARE DECREMENTO DEFAULT DIFERENTE DIVISION DIVISION_ENT DO ECHO ELSE ELSEIF ENDDECLARE ENDIF ENDSWITCH ENDWHILE ENTERO EXTENDS FINAL FINALLY FLECHA FLOTANTE FN FOR FOREACH FUNCTION GLOBAL IDENTICO IF IGUAL IMPLEMENTS INCLUDE INCREMENTO INTANCEOF INTEADOF INTERFACE INTERROG_CE LLAVE_DER LLAVE_IZQ MACHT MAYOR_IGUAL MAYOR_QUE MENOR_IGUAL MENOR_QUE MODULO MULTIPL NAMESPACE NEW OR OR_SYMB PAREN_DER PAREN_IZQ POP POTENCIA PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTODOBLE PUNTO_COMA PUSH QUEUE REQUIERE RESTA RETURN SALTO_LINEA SIGNO_DOLAR STACK STATIC STRING STRREV SUMA SWITCH TABULACION THROW TRAIT TRES_PUNTOS TRY USE VAR WHILEinstrucciones : valor\n                    | asignacion\n                    | salida \n                    | estructuras_control\n                    | estructuras_datos\n                    | funciones  \n                    | op_logica\n                    | op_pila\n  asignacion : SIGNO_DOLAR CADENA IGUAL valor PUNTO_COMAvalor : datos \n          | pila\n          | cola\n  datos : ENTERO\n          | FLOTANTE\n          | STRING \n          | BOOLEANO \n  salida : ECHO CADENA PUNTO_COMAsalida : PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMAsalida : PRINT STRING PUNTO_COMA estructuras_control : if_else \n                          | switch1\n                          | whileDeclaracion\n   estructuras_datos : pila \n                        | cola\n                        | arreglo\n  funciones : funcion_variable \n                | sinRetorno\n  operad_log : IDENTICO\n                | DIFERENTE\n                | MAYOR_QUE\n                | MAYOR_IGUAL\n                | MENOR_QUE\n                | MENOR_IGUAL\n   bloque : asignacion\n              | salida\n              | retorno\n   cola : NEW QUEUE PAREN_IZQ PAREN_DER switch1 : SWITCH PAREN_IZQ  SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ CASE ENTERO PUNTODOBLE  BREAK LLAVE_DER if_else : if_else_inicio if_else_fin if_else : if_else_inicio if_else_cuerpo if_else_finif_else_inicio : IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DERif_else_cuerpo : ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DERif_else_fin : ELSE LLAVE_IZQ salida LLAVE_DER op_logica : ENTERO operad_log ENTERO\n                | FLOTANTE operad_log FLOTANTE\n                | STRING operad_log STRING\n                | BOOLEANO\n   pila :  NEW STACK PAREN_IZQ PAREN_DER op_pila : SIGNO_DOLAR CADENA RESTA MAYOR_QUE operad_pila operad_pila : PUSH PAREN_IZQ datos PAREN_DER PUNTO_COMA \n                  | POP PAREN_IZQ PAREN_DER PUNTO_COMA\n                  | COUNT PAREN_IZQ PAREN_DER PUNTO_COMA\n                  | CURRENT PAREN_IZQ PAREN_DER PUNTO_COMA\n   funcion_variable : FUNCTION CADENA PAREN_IZQ TRES_PUNTOS SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ bloque LLAVE_DER retorno : RETURN SIGNO_DOLAR CADENAcontenido : bloque\n               | sinRetornowhileDeclaracion : WHILE PAREN_IZQ SIGNO_DOLAR CADENA operad_log valor PAREN_DER LLAVE_IZQ contenido LLAVE_DERvalores : valor repite_valores repite_valores : COMA valor\n                        | COMA valor repite_valores\n    arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valores PAREN_DER PUNTO_COMA valoresflecha : valor FLECHA valor repite_valores_f repite_valores_f : COMA valor FLECHA valor\n                        | COMA valor FLECHA valor repite_valores\n  arreglo : SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valoresflecha PAREN_DER PUNTO_COMAsinRetorno : FUNCTION CADENA PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ contenido LLAVE_DER'
    
_lr_action_items = {'SIGNO_DOLAR':([0,51,52,70,92,136,148,149,158,174,],[13,68,69,93,107,151,151,151,169,93,]),'ECHO':([0,66,109,117,136,148,149,],[14,14,14,14,14,14,14,]),'PRINT':([0,66,109,117,136,148,149,],[15,15,15,15,15,15,15,]),'ENTERO':([0,37,38,39,40,41,42,43,54,55,67,96,106,113,126,127,133,160,175,177,],[23,-28,-29,-30,-31,-32,-33,61,72,80,72,80,80,80,80,80,147,80,80,80,]),'FLOTANTE':([0,37,38,39,40,41,42,44,54,55,67,96,106,113,126,127,160,175,177,],[24,-28,-29,-30,-31,-32,-33,62,73,81,73,81,81,81,81,81,81,81,81,]),'STRING':([0,15,34,36,37,38,39,40,41,42,54,55,67,96,106,113,126,127,160,175,177,],[16,35,58,60,-28,-29,-30,-31,-32,-33,74,82,74,82,82,82,82,82,82,82,82,]),'BOOLEANO':([0,37,38,39,40,41,42,54,55,67,96,106,113,126,127,160,175,177,],[25,-28,-29,-30,-31,-32,-33,75,83,75,83,83,83,83,83,83,83,83,]),'NEW':([0,37,38,39,40,41,42,55,96,106,126,127,160,175,177,],[26,-28,-29,-30,-31,-32,-33,26,26,26,26,26,26,26,26,]),'SWITCH':([0,],[28,]),'WHILE':([0,],[29,]),'FUNCTION':([0,136,148,],[30,150,150,]),'IF':([0,],[31,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,24,25,47,57,59,60,61,62,65,86,87,95,97,102,103,138,139,143,144,145,162,168,172,173,178,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-10,-11,-12,-15,-20,-21,-22,-25,-26,-27,-13,-14,-16,-39,-17,-19,-46,-44,-45,-40,-48,-37,-9,-49,-18,-43,-62,-66,-51,-52,-53,-50,-67,-58,-54,-38,]),'PUNTO_COMA':([10,33,35,76,78,79,80,81,82,83,85,86,87,123,124,129,130,131,142,],[-10,57,59,95,-11,-12,-13,-14,-15,-16,102,-48,-37,138,139,143,144,145,162,]),'FLECHA':([10,78,79,80,81,82,83,86,87,112,170,],[-10,-11,-12,-13,-14,-15,-16,-48,-37,126,177,]),'COMA':([10,78,79,80,81,82,83,86,87,112,140,141,179,],[-10,-11,-12,-13,-14,-15,-16,-48,-37,127,160,127,127,]),'PAREN_DER':([10,58,60,61,62,63,64,71,75,78,79,80,81,82,83,86,87,89,90,108,110,111,114,115,116,119,120,125,128,141,159,161,179,180,],[-10,85,-46,-44,-45,86,87,94,-47,-11,-12,-13,-14,-15,-16,-48,-37,104,105,121,123,124,129,130,131,134,135,-59,142,-60,-63,-61,-64,-65,]),'CADENA':([13,14,30,68,69,93,107,150,151,169,],[32,33,53,90,91,108,120,166,167,176,]),'PAREN_IZQ':([15,28,29,31,45,46,50,53,77,98,99,100,101,166,],[34,51,52,54,63,64,67,70,96,113,114,115,116,174,]),'IDENTICO':([16,23,24,72,73,74,91,],[37,37,37,37,37,37,37,]),'DIFERENTE':([16,23,24,72,73,74,91,],[38,38,38,38,38,38,38,]),'MAYOR_QUE':([16,23,24,56,72,73,74,91,],[39,39,39,84,39,39,39,39,]),'MAYOR_IGUAL':([16,23,24,72,73,74,91,],[40,40,40,40,40,40,40,]),'MENOR_QUE':([16,23,24,72,73,74,91,],[41,41,41,41,41,41,41,]),'MENOR_IGUAL':([16,23,24,72,73,74,91,],[42,42,42,42,42,42,42,]),'STACK':([26,],[45,]),'QUEUE':([26,],[46,]),'ELSE':([27,48,137,146,],[49,49,-41,-42,]),'ELSEIF':([27,137,],[50,-41,]),'IGUAL':([32,167,],[55,175,]),'RESTA':([32,],[56,]),'LLAVE_IZQ':([49,94,104,105,121,134,135,],[66,109,117,118,136,148,149,]),'ARRAY':([55,],[77,]),'LLAVE_DER':([57,59,88,95,102,122,132,152,153,154,155,156,157,164,165,168,171,176,],[-17,-19,103,-9,-18,137,146,168,-56,-57,-34,-35,-36,172,173,-67,178,-55,]),'TRES_PUNTOS':([70,],[92,]),'PUSH':([84,],[98,]),'POP':([84,],[99,]),'COUNT':([84,],[100,]),'CURRENT':([84,],[101,]),'CASE':([118,],[133,]),'RETURN':([136,148,149,],[158,158,158,]),'PUNTODOBLE':([147,],[163,]),'BREAK':([163,],[171,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'valor':([0,55,96,106,126,127,160,175,177,],[2,76,112,119,140,141,170,76,179,]),'asignacion':([0,136,148,149,],[3,155,155,155,]),'salida':([0,66,109,117,136,148,149,],[4,88,122,132,156,156,156,]),'estructuras_control':([0,],[5,]),'estructuras_datos':([0,],[6,]),'funciones':([0,],[7,]),'op_logica':([0,54,67,],[8,71,89,]),'op_pila':([0,],[9,]),'datos':([0,55,96,106,113,126,127,160,175,177,],[10,10,10,10,128,10,10,10,10,10,]),'pila':([0,55,96,106,126,127,160,175,177,],[11,78,78,78,78,78,78,78,78,]),'cola':([0,55,96,106,126,127,160,175,177,],[12,79,79,79,79,79,79,79,79,]),'if_else':([0,],[17,]),'switch1':([0,],[18,]),'whileDeclaracion':([0,],[19,]),'arreglo':([0,],[20,]),'funcion_variable':([0,],[21,]),'sinRetorno':([0,136,148,],[22,154,154,]),'if_else_inicio':([0,],[27,]),'operad_log':([16,23,24,72,73,74,91,],[36,43,44,43,44,36,106,]),'if_else_fin':([27,48,],[47,65,]),'if_else_cuerpo':([27,],[48,]),'operad_pila':([84,],[97,]),'valores':([96,],[110,]),'valoresflecha':([96,],[111,]),'repite_valores':([112,141,179,],[125,161,180,]),'contenido':([136,148,],[152,164,]),'bloque':([136,148,149,],[153,153,165,]),'retorno':([136,148,149,],[157,157,157,]),'repite_valores_f':([140,],[159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> valor','instrucciones',1,'p_instrucciones','main.py',7),
  ('instrucciones -> asignacion','instrucciones',1,'p_instrucciones','main.py',8),
  ('instrucciones -> salida','instrucciones',1,'p_instrucciones','main.py',9),
  ('instrucciones -> estructuras_control','instrucciones',1,'p_instrucciones','main.py',10),
  ('instrucciones -> estructuras_datos','instrucciones',1,'p_instrucciones','main.py',11),
  ('instrucciones -> funciones','instrucciones',1,'p_instrucciones','main.py',12),
  ('instrucciones -> op_logica','instrucciones',1,'p_instrucciones','main.py',13),
  ('instrucciones -> op_pila','instrucciones',1,'p_instrucciones','main.py',14),
  ('asignacion -> SIGNO_DOLAR CADENA IGUAL valor PUNTO_COMA','asignacion',5,'p_asignacion','main.py',18),
  ('valor -> datos','valor',1,'p_valor','main.py',23),
  ('valor -> pila','valor',1,'p_valor','main.py',24),
  ('valor -> cola','valor',1,'p_valor','main.py',25),
  ('datos -> ENTERO','datos',1,'p_datos','main.py',30),
  ('datos -> FLOTANTE','datos',1,'p_datos','main.py',31),
  ('datos -> STRING','datos',1,'p_datos','main.py',32),
  ('datos -> BOOLEANO','datos',1,'p_datos','main.py',33),
  ('salida -> ECHO CADENA PUNTO_COMA','salida',3,'p_salida_forma1','main.py',39),
  ('salida -> PRINT PAREN_IZQ STRING PAREN_DER PUNTO_COMA','salida',5,'p_salida_forma2','main.py',42),
  ('salida -> PRINT STRING PUNTO_COMA','salida',3,'p_salida_forma3','main.py',45),
  ('estructuras_control -> if_else','estructuras_control',1,'p_estructuras_control','main.py',52),
  ('estructuras_control -> switch1','estructuras_control',1,'p_estructuras_control','main.py',53),
  ('estructuras_control -> whileDeclaracion','estructuras_control',1,'p_estructuras_control','main.py',54),
  ('estructuras_datos -> pila','estructuras_datos',1,'p_estructuras_datos','main.py',58),
  ('estructuras_datos -> cola','estructuras_datos',1,'p_estructuras_datos','main.py',59),
  ('estructuras_datos -> arreglo','estructuras_datos',1,'p_estructuras_datos','main.py',60),
  ('funciones -> funcion_variable','funciones',1,'p_funciones','main.py',64),
  ('funciones -> sinRetorno','funciones',1,'p_funciones','main.py',65),
  ('operad_log -> IDENTICO','operad_log',1,'p_operad_log','main.py',70),
  ('operad_log -> DIFERENTE','operad_log',1,'p_operad_log','main.py',71),
  ('operad_log -> MAYOR_QUE','operad_log',1,'p_operad_log','main.py',72),
  ('operad_log -> MAYOR_IGUAL','operad_log',1,'p_operad_log','main.py',73),
  ('operad_log -> MENOR_QUE','operad_log',1,'p_operad_log','main.py',74),
  ('operad_log -> MENOR_IGUAL','operad_log',1,'p_operad_log','main.py',75),
  ('bloque -> asignacion','bloque',1,'p_bloque','main.py',79),
  ('bloque -> salida','bloque',1,'p_bloque','main.py',80),
  ('bloque -> retorno','bloque',1,'p_bloque','main.py',81),
  ('cola -> NEW QUEUE PAREN_IZQ PAREN_DER','cola',4,'p_cola','main.py',93),
  ('switch1 -> SWITCH PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ CASE ENTERO PUNTODOBLE BREAK LLAVE_DER','switch1',11,'p_switch1','main.py',97),
  ('if_else -> if_else_inicio if_else_fin','if_else',2,'p_if_else_corto','main.py',108),
  ('if_else -> if_else_inicio if_else_cuerpo if_else_fin','if_else',3,'p_if_else_extendido','main.py',112),
  ('if_else_inicio -> IF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER','if_else_inicio',7,'p_if_else_inicio','main.py',116),
  ('if_else_cuerpo -> ELSEIF PAREN_IZQ op_logica PAREN_DER LLAVE_IZQ salida LLAVE_DER','if_else_cuerpo',7,'p_if_else_cuerpo','main.py',120),
  ('if_else_fin -> ELSE LLAVE_IZQ salida LLAVE_DER','if_else_fin',4,'p_if_else_fin','main.py',124),
  ('op_logica -> ENTERO operad_log ENTERO','op_logica',3,'p_op_logica','main.py',128),
  ('op_logica -> FLOTANTE operad_log FLOTANTE','op_logica',3,'p_op_logica','main.py',129),
  ('op_logica -> STRING operad_log STRING','op_logica',3,'p_op_logica','main.py',130),
  ('op_logica -> BOOLEANO','op_logica',1,'p_op_logica','main.py',131),
  ('pila -> NEW STACK PAREN_IZQ PAREN_DER','pila',4,'p_pila','main.py',139),
  ('op_pila -> SIGNO_DOLAR CADENA RESTA MAYOR_QUE operad_pila','op_pila',5,'p_op_pila','main.py',144),
  ('operad_pila -> PUSH PAREN_IZQ datos PAREN_DER PUNTO_COMA','operad_pila',5,'p_operad_pila','main.py',148),
  ('operad_pila -> POP PAREN_IZQ PAREN_DER PUNTO_COMA','operad_pila',4,'p_operad_pila','main.py',149),
  ('operad_pila -> COUNT PAREN_IZQ PAREN_DER PUNTO_COMA','operad_pila',4,'p_operad_pila','main.py',150),
  ('operad_pila -> CURRENT PAREN_IZQ PAREN_DER PUNTO_COMA','operad_pila',4,'p_operad_pila','main.py',151),
  ('funcion_variable -> FUNCTION CADENA PAREN_IZQ TRES_PUNTOS SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ bloque LLAVE_DER','funcion_variable',10,'p_funcion_variable','main.py',159),
  ('retorno -> RETURN SIGNO_DOLAR CADENA','retorno',3,'p_retorno','main.py',165),
  ('contenido -> bloque','contenido',1,'p_contenido','main.py',172),
  ('contenido -> sinRetorno','contenido',1,'p_contenido','main.py',173),
  ('whileDeclaracion -> WHILE PAREN_IZQ SIGNO_DOLAR CADENA operad_log valor PAREN_DER LLAVE_IZQ contenido LLAVE_DER','whileDeclaracion',10,'p_whileDeclaracion','main.py',177),
  ('valores -> valor repite_valores','valores',2,'p_valoresSeparadosComa','main.py',182),
  ('repite_valores -> COMA valor','repite_valores',2,'p_repite_valoresSeparadosComa','main.py',185),
  ('repite_valores -> COMA valor repite_valores','repite_valores',3,'p_repite_valoresSeparadosComa','main.py',186),
  ('arreglo -> SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valores PAREN_DER PUNTO_COMA','arreglo',8,'p_arreglo_parentesis','main.py',194),
  ('valoresflecha -> valor FLECHA valor repite_valores_f','valoresflecha',4,'p_valoresArregloAsociativo','main.py',199),
  ('repite_valores_f -> COMA valor FLECHA valor','repite_valores_f',4,'p_repite_valoresSeparados_flecha','main.py',203),
  ('repite_valores_f -> COMA valor FLECHA valor repite_valores','repite_valores_f',5,'p_repite_valoresSeparados_flecha','main.py',204),
  ('arreglo -> SIGNO_DOLAR CADENA IGUAL ARRAY PAREN_IZQ valoresflecha PAREN_DER PUNTO_COMA','arreglo',8,'p_arreglo_asociativo','main.py',208),
  ('sinRetorno -> FUNCTION CADENA PAREN_IZQ SIGNO_DOLAR CADENA PAREN_DER LLAVE_IZQ contenido LLAVE_DER','sinRetorno',9,'p_sinretorno','main.py',212),
]