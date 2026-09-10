# Descripció de la Taula: `fact_horas_trabajadas`

## 1. Descripció
La taula **`fact_horas_trabajadas`** és una **taula de fets (*Fact Table*)** en un model dimensional de Recursos Humans (RRHH). El seu objectiu principal és enregistrar l'activitat diària de fitxatge, control horari, puntualitat i modalitat de treball de la plantilla de l'empresa RapidExpress

* **Granularitat:** Cada registre (fila) representa el resum diari de la jornada laboral d'un empleat concret en una data específica.

---


## 2. Estructura de Camps

### 2.1. Claus primària i forànies (*Keys*)
Aquests camps s'encarreguen d'identificar de manera unívoca cada registre i d'establir les relacions amb les taules de dimensió

| Columna | Tipus | Null |Clau / Restricció | Descripció |
| :--- | :--- | :--- | :--- | :--- |
| `` `horas_trabajadas_id` `` | `bigint unsigned` | No | **PRI** (Primary Key) | Identificador únic incremental de cada registre de jornada. |
| `` `empleado_key` `` | `bigint unsigned` | No | — | Actua com clau forana lógica cap a la taula de dimensió `dim_empleado`, tot i no tenir la restricció FK explícita encara a la base de dades |
| `` `fecha_key` `` | `int` | No | **MUL** (Index) | Clau forana amb format numèric de data (ex: `20240530`) que connecta amb la dimensió de temps (`dim_fecha`). |

### 2.2. Altres Camps
#### A. Mètriques de Durada Horària
Camps de tipus numèric decimal dedicats a quantificar el volum d'hores registrades, tant les teòriques com les desglossades per tipologies especials.

| Columna | Tipus | Null | Descripció |
| :--- | :--- | :--- | :--- |
| `` `horas_teoriques` `` | `decimal(6,2)` | No | Hores teòriques o contractuals que li pertocava treballar a l'empleat. |
| `` `horas_trabajadas` `` | `decimal(6,2)` | No | Hores totals reals registrades per l'empleat durant la jornada. |
| `` `horas_ordinarias` `` | `decimal(6,2)` | No | Hores ordinàries efectives treballades dins de la jornada regular. |
| `` `horas_extra` `` | `decimal(6,2)` | No | Hores extraordinàries realitzades per damunt de la jornada ordinària. |
| `` `horas_extra_pagadas` `` | `decimal(6,2)` | No | Desglossament d'hores extra que seran remunerades econòmicament. |
| `` `horas_extra_compensadas` `` | `decimal(6,2)` | No | Desglossament d'hores extra compensades en hores de descans. |
| `` `horas_nocturnas` `` | `decimal(6,2)` | No | Hores realitzades en franja horària nocturna. |
| `` `horas_festivas` `` | `decimal(6,2)` | No | Hores treballades en dies festius o de librança assenyalats. |
| `` `horas_fin_semana` `` | `decimal(6,2)` | No | Hores realitzades durant dissabtes i diumenges. |
| `` `horas_presenciales` `` | `decimal(6,2)` | No | Hores realitzades presencialment al centre de treball. |
| `` `horas_remotas` `` | `decimal(6,2)` | No | Hores realitzades sota la modalitat de teletreball. |

#### B. Control de Fitxatge i Desviacions Temporals
Registres horaris detallats d'entrada i sortida, juntament càrrec d'indicadors de puntualitat, pauses i incidències operatives.

| Columna | Tipus | Null | Descripció |
| :--- | :--- | :--- | :--- |
| `` `hora_entrada_teorica` `` | `time` | Sí | Hora oficial d'entrada fixada per horari o contracte. |
| `` `hora_salida_teorica` `` | `time` | Sí | Hora oficial de sortida fixada per horari o contracte. |
| `` `hora_entrada_real` `` | `time` | Sí | Hora real en què l'empleat ha fitxat l'entrada. |
| `` `hora_salida_real` `` | `time` | Sí | Hora real en què l'empleat ha fitxat la sortida. |
| `` `minutos_retraso` `` | `smallint unsigned` | No | Minuts de retard acumulats respecte a l'hora d'entrada teòrica. |
| `` `minutos_salida_anticipada` `` | `smallint unsigned` | No | Minuts de sortida abans de l'horari previst. |
| `` `minutos_pausa` `` | `smallint unsigned` | No | Temps total en minuts dedicat a pauses o descansos durant la jornada. |
| `` `numero_fichajes` `` | `tinyint unsigned` | No | Nombre total de marcatges o fitxatges fets durant el dia. |
| `` `fichaje_incompleto` `` | `tinyint(1)` | No | Indicador boleà (0/1) de si falta algun fitxatge obligatori. |
| `` `dia_trabajado` `` | `tinyint(1)` | No | Indicador boleà (0/1) que confirma si el dia s'ha considerat laborable efectiu. |
| `` `teletrabajo` `` | `tinyint(1)` | No | Indicador boleà (0/1) de si la jornada s'ha realitzat en modalitat de teletreball. |
| `` `incidencia_jornada` `` | `tinyint(1)` | No | Indicador boleà (0/1) si hi ha hagut alguna anomalia o incidència en el registre. |
| `` `tipo_incidencia` `` | `varchar(100)` | No | Descripció textual o tipologia de la incidència esdevinguda. |

#### C. Metadades i Auditoria
Camps destinats a registrar la traçabilitat tècnica del procés d'ETL i la inserció de les dades al magatzem.

| Columna | Tipus | Null | Descripció |
| :--- | :--- | :--- | :--- |
| `` `fecha_registro` `` | `datetime` | No | Marca temporal del moment en què es crea el registre a la taula. |
| `` `fecha_carga` `` | `datetime` | No | Data i hora de l'execució del procés de càrrega de dades. |
| `` `fuente_datos` `` | `varchar(100)` | Sí | Sistema d'origen del registre horari. La font usada principalment "Sistema de fichaje sintético" |


## 3. Índexs

La taula disposa dels següents índexs:

| Índex | Camps | Finalitat |
| :--- | :--- | :--- |
| `` `PRIMARY` `` | `` `horas_trabajadas_id` `` | Identificar de forma única cada registre. |
| `` `idx_horas_fecha` `` | `` `fecha_key` `` | Facilitar consultes, unions i filtres per data. |