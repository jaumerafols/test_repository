# Descripció de la Taula: `fact_horas_trabajadas`

## 1. Context i Propòsit
La taula **`fact_horas_trabajadas`** és una **taula de fets (*Fact Table*)** en un model dimensional de Recursos Humans (RRHH). El seu objectiu principal és enregistrar l'activitat diària de fitxatge, control horari, puntualitat i modalitat de treball de la plantilla de l'empresa RapidExpress

* **Granularitat:** Cada registre (fila) representa el resum diari de la jornada laboral d'un empleat concret en una data específica.

La taula conté actualment 104.570 registres, sent la primera data registrada el 19-01-2020 i la última el 06-09-2020. La taula consta de 30 camps que expliquem a continuació:

---

## 2. Estructura de Camps

### A. Claus Principals i Relacions (*Keys*)
* **`horas_trabajadas_id`** (`bigint unsigned`, Primary Key, Auto Increment): Identificador únic incremental de cada registre de jornada.
* **`empleado_key`** (`bigint unsigned`): Actua com clau forana lógica cap a la taula de dimensió `dim_empleado`, tot i no tenir la restricció FK explícita encara a la base de dades
* **`fecha_key`** (`int`): Clau forana amb format numèric de data (ex: `20240530`) que connecta amb la taula de dimensió `dim_fecha`.

### B. Mètriques de Durada Horària (`decimal(6,2)`)
* **Hores generals:** `horas_teoricas` (jornada contractual), `horas_trabajadas` (reals) i `horas_ordinarias`.
* **Hores especials / desglossament:** `horas_extra`, `horas_extra_pagadas`, `horas_extra_compensadas`, `horas_nocturnas`, `horas_festivas` i `horas_fin_semana`.
* **Modalitat de treball:** `horas_presenciales` i `horas_remotas`.

### C. Control de Fitxatge i Temps (`time`, `smallint`, `tinyint`)
* **Marcatges:** `hora_entrada_teorica`, `hora_salida_teorica`, `hora_entrada_real` i `hora_salida_real`.
* **Desviacions i pauses:** `minutos_retraso`, `minutos_salida_anticipada`, `minutos_pausa` i `numero_fichajes`.
* **Indicadors booleans (`tinyint(1)`):** `fichaje_incompleto`, `dia_trabajado`, `teletrabajo` i `incidencia_jornada`.

### D. Metadades i Auditoria
* `tipo_incidencia` (`varchar(100)`): Descripció textual de la incidència (si escau).
* `fecha_registro`, `fecha_carga` (`datetime`): Marca temporal d'inserció o càrrega d'ETL.
* `fuente_datos` (`varchar(100)`): Sistema d'origen del registre horari, on s'indica que "Sistema de fichaje sintético"



