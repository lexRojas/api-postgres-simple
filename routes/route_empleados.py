import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_sectores = APIRouter()


@route_sectores.get("/empleados")
def get_empleados(presupuesto=''):
   with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select codigo_empleado,"+
                       "concat( nombre1,' ',nombre2,' ',apellido1,' ',apellido2) as nombre_completo " + 
                       "from payroll.empleado e " +
                       "inner join payroll.persona p on e.persona_idpersona = p.idpersona " +
                       "where fecha_salida is null " +
                       "and funcion = 'C-Campo' " +
                       "and proyecto_presupuesto = '"+ presupuesto+"'")
      result = dict_cur.fetchall()
   return result

