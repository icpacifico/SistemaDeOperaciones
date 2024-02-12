is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

# Activo-Inactivo
# etapa_estado_etapa
# modelo_estado_modelo
# torre_estado_torre
# condominio_estado_condominio
# vendedor_estado_vendedor
# bono_estado_bono
############################################################################################
disponible = 'Disponible'
no_disponible = 'No Disponible'

IS_DISPONIBLE_CHOICES = [(disponible, 'Disponible'),
                         (no_disponible, 'No Disponible'), ]

# Disponible - No Disponible
# estacionamiento_estado_estacionamiento
# vivienda_estado_vivienda
# bodega_estado_bodega
############################################################################################

masculino = 'Masculino'
femenino = 'Femenino'
sin_definir = 'Sin Definir'
otro = 'Otro'

SEXO_CHOICES = [(masculino, 'Masculino'),
                (femenino, 'Femenino'),
                (sin_definir, 'Sin Definir'),
                (otro, 'Otro'), ]
############################################################################################

soltero_a = 'Soltero/a'
casado_a = 'Casado/a'
divorciado_a = 'Divorciado/a'

ESTADO_CIVIL_CHOICES = [(soltero_a, 'Soltero/a'),
                        (casado_a, 'Casado/a'),
                        (divorciado_a, 'Divorciado/a'), ]
############################################################################################

ens_basica = 'Enseñanza Básica'
ens_media = 'Enseñanza Media'
tec_prof = 'Técnico Profesional'
tec_nvl_sup = 'Técnico Nivel Superior'
profesional = 'Profesional'

ENSENAGSA_CHOICES = [(ens_basica, 'Enseñanza Básica'),
                     (ens_media, 'Enseñanza Media'),
                     (tec_prof, 'Técnico Profesional'),
                     (tec_nvl_sup, 'Técnico Nivel Superior'),
                     (profesional, 'Profesional'), ]

############################################################################################
i_reg_tarapaca = 'I REGIÓN DE TARAPACÁ'
ii_reg_antofagasta = 'II REGIÓN DE ANTOFAGASTA'
iii_reg_atacama = 'III REGIÓN DE ATACAMA'
iv_reg_coquimbo = 'IV REGIÓN DE COQUIMBO'
v_reg_valparaiso = 'V REGIÓN DE VALPARAÍSO'
vi_reg_ohiggins = 'VI REGIÓN DE O´HIGGINS'
vii_reg_maule = 'VII REGIÓN DEL MAULE'
xvi_reg_nugble = 'XVI REGIÓN DEL ÑUBLE'
viii_reg_biobio = "VIII REGIÓN DEL BÍO-BÍO"
ix_reg_araucania = "IX REGIÓN DE LA ARAUCANÍA"
x_reg_lagos = "X REGIÓN DE LOS LAGOS"
xi_reg_aysen = "XI REGIÓN DE AYSÉN"
xii_reg_magallanes = "XII REGIÓN DE MAGALLANES"
reg_met = "REGIÓN METROPOLITANA"
xiv_reg_rios = "XIV DE LOS RÍOS"
xv_reg_arica = "XV REGIÓN DE ARICA Y PARINACOTA"
# Regiones
REGIONES_CHOICES = [(i_reg_tarapaca, 'I REGIÓN DE TARAPACÁ'),
                    (ii_reg_antofagasta, 'II REGIÓN DE ANTOFAGASTA'),
                    (iii_reg_atacama, 'III REGIÓN DE ATACAMA'),
                    (iv_reg_coquimbo, 'IV REGIÓN DE COQUIMBO'),
                    (v_reg_valparaiso, 'V REGIÓN DE VALPARAÍSO'),
                    (vi_reg_ohiggins, 'VI REGIÓN DE O´HIGGINS'),
                    (vii_reg_maule, 'VII REGIÓN DEL MAULE'),
                    (xvi_reg_nugble, 'XVI REGIÓN DEL ÑUBLE'),
                    (viii_reg_biobio, "VIII REGIÓN DEL BÍO-BÍO"),
                    (ix_reg_araucania, "IX REGIÓN DE LA ARAUCANÍA"),
                    (x_reg_lagos, "X REGIÓN DE LOS LAGOS"),
                    (xi_reg_aysen, "XI REGIÓN DE AYSÉN"),
                    (xii_reg_magallanes, "XII REGIÓN DE MAGALLANES"),
                    (reg_met, "REGIÓN METROPOLITANA"),
                    (xiv_reg_rios, "XIV DE LOS RÍOS"),
                    (xv_reg_arica, "XV REGIÓN DE ARICA Y PARINACOTA"), ]
############################################################################################

enero = "Enero"
febrero = "Febrero"
marzo = "Marzo"
abril = "Abril"
mayo = "Mayo"
junio = "Junio"
julio = "Julio"
agosto = "Agosto"
septiembre = "Septiembre"
octubre = "Octubre"
noviembre = "Noviembre"
diciembre = "Diciembre"
# Meses
MESES_CHOICES = [(enero, "Enero"),
                 (febrero, "Febrero"),
                 (marzo, "Marzo"),
                 (abril, "Abril"),
                 (mayo, "Mayo"),
                 (junio, "Junio"),
                 (julio, "Julio"),
                 (agosto, "Agosto"),
                 (septiembre, "Septiembre"),
                 (octubre, "Octubre"),
                 (noviembre, "Noviembre"),
                 (diciembre, "Diciembre"), ]
############################################################################################

activa = 'Activa'
inactiva = 'Inactiva'
desistimiento = 'Desestimiento'
promesa = 'Promesa'
venta = 'Venta'
escritura = 'Escritura'
venta_escriturada = 'Venta Escriturada'
# cotizacion_estado_cotizacion
EST_COTIZACION_CHOICES = [(activa, 'Activa'),
                          (inactiva, 'Inactiva'),
                          (desistimiento, 'Desestimiento'),
                          (promesa, 'Promesa'),
                          (venta, 'Venta'),
                          (escritura, 'Escritura'),
                          (venta_escriturada, 'Venta Escriturada'), ]
############################################################################################

realizado = 'Realizado'
pendiente = 'Pendiente'
protestado = 'Protestado'
# pago_estado_pago
EST_PAGO_CHOICES = [(realizado, 'Realizado'),
                          (pendiente, 'Pendiente'),
                          (protestado, 'Protestado'), ]
############################################################################################

activa = 'Activa'
inactiva = 'Inactiva'
desistimiento = 'Desestimiento'
promesa = 'Promesa'
venta_comisionada = 'Venta Comisionada'
en_escritura = 'En Escritura'
escriturada = 'Escriturada'
# venta_estado_venta
EST_VENTA_CHOICES = [(activa, 'Activa'),
                          (inactiva, 'Inactiva'),
                          (desistimiento, 'Desestimiento'),
                          (promesa, 'Promesa'),
                          (venta_comisionada, 'Venta Comisionada'),
                          (en_escritura, 'En Escritura'),
                          (escriturada, 'Escriturada'), ]
############################################################################################
activa = 'Activa'
inactiva = 'Inactiva'
desistimiento = 'Desestimiento'
promesa = 'Promesa'
venta_comisionada = 'Venta Comisionada'
en_escritura = 'En Escritura'
escriturada = 'Escriturada'
# venta_estado_etapa_venta
EST_ESTAPA_VENTA_CHOICES = [(activa, 'Activa'),
                          (inactiva, 'Inactiva'),
                          (desistimiento, 'Desestimiento'),
                          (promesa, 'Promesa'),
                          (venta_comisionada, 'Venta Comisionada'),
                          (en_escritura, 'En Escritura'),
                          (escriturada, 'Escriturada'), ]
############################################################################################
si = 'Si'
no = 'No'
# venta_pie_abono_venta
SI_NO_CHOICES = [(si, 'Si'),
                 (no, 'No')]
############################################################################################
bajo = 'Bajo'
medio = 'Medio'
alto = 'Ato'
# cotizacion_seguimiento_interes_cotizacion
SEG_INTERES_COTIZACION_CHOICES = [(bajo, 'Activa'),
                          (medio, 'Medio'),
                          (alto, 'Ato'), ]
############################################################################################
correo = 'Correo'
wsp = 'Whatsapp'
telefono = 'Teléfono'
# cotizacion_medio_cotizacion
MEDIO_COTIZACION_CHOICES = [(correo, 'Correo'),
                            (wsp, 'Whatsapp'),
                            (telefono, 'Teléfono'), ]
############################################################################################
sala_venta = 'sala de ventas'
pag_web = 'Página Web'
terreno = 'Terreno'
rrss = 'Redes Sociales - Inmobiliaria'
otros = 'Otros'
comercial_tv = 'Comercial TV Pabellón de la Construcción'
expovivienda = 'Expovivienda'
letreros = 'Letreros'
por_tv = 'Por la Televisión'
por_otro_medio = 'Por Otro Medio'
portal_inmo = 'Portal Inmobiliario Internet'
recomendacion = 'Recomendación'
vivienda = 'Vivienda y Decoración'
rrss_asesor = 'Redes Sociales - Gestión Asesor'
toc_toc = 'Toc-Toc'
enlace_inmo = 'Enlace Inmobiliario'
nueva_campagna = 'Nueva Campaña'

# cotizacion_canal_cotizacion

CANAL_COTIZACION_CHOICES = [
    (comercial_tv, 'Comercial TV Pabellón de la Construcción'),
    (enlace_inmo, 'Enlace Inmobiliario'),
    (expovivienda, 'Expovivienda'),
    (letreros, 'Letreros'),
    (nueva_campagna, 'Nueva Campaña'),
    (otros, 'Otros'),
    (pag_web, 'Página Web'),
    (por_otro_medio, 'Por Otro Medio'),
    (por_tv, 'Por la Televisión'),
    (portal_inmo, 'Portal Inmobiliario Internet'),
    (recomendacion, 'Recomendación'),
    (rrss, 'Redes Sociales - Inmobiliaria'),
    (rrss_asesor, 'Redes Sociales - Gestión Asesor'),
    (sala_venta, 'Sala de Ventas'),
    (terreno, 'Terreno'),
    (toc_toc, 'Toc-Toc'),
    (vivienda, 'Vivienda y Decoración')
]

# CANAL_COTIZACION_CHOICES = [(sala_venta, 'Sala de Ventas'),
#                           (pag_web, 'Página Web'),
#                           (terreno, 'Terreno'),
#                           (rrss, 'Redes Sociales - Inmobiliaria'),
#                           (otros, 'Otros'),
#                           (comercial_tv, 'Comercial TV Pabellón de la Construcción'),
#                           (expovivienda, 'Expovivienda'),
#                           (letreros, 'Letreros'),
#                           (por_tv, 'Por la Televisión'),
#                           (por_otro_medio, 'Por Otro Medio'),
#                           (portal_inmo, 'Portal Inmobiliario Internet'),
#                           (recomendacion, 'Recomendación'),
#                           (vivienda, 'Vivienda y Decoración'),
#                           (rrss_asesor, 'Redes Sociales - Gestión Asesor'),
#                           (toc_toc, 'Toc-Toc'),
#                           (enlace_inmo, 'Enlace Inmobiliario'),
#                           (nueva_campagna, 'Nueva Campaña'), ]
############################################################################################
rank_1 = '$0 a $499.999'
rank_2 = '$450.000 a $799.999'
rank_3 = '$750.000 a $1.299.999'
rank_4 = '$1.300.000 a $2.499.999'
rank_5 = '$2.500.000 a $2.999.999'
rank_6 = '$3.000.000 a $3.999.999'
rank_7 = '$4.000.000 a $4.999.999'
rank_8 = '$5.000.000 a $5.999.999'
rank_9 = '$6.000.000 a $6.999.999'
rank_10 = '> $7.000.000'
rank_11 = 'No definido'
# cotizacion_renta_cotizacion
RENTA_COTIZACION_CHOICES = [(rank_1, '$0 a $499.999'),
                            (rank_2, '$450.000 a $799.999'),
                            (rank_3, '$750.000 a $1.299.999'),
                            (rank_4, '$1.300.000 a $2.499.999'),
                            (rank_5, '$2.500.000 a $2.999.999'),
                            (rank_6, '$3.000.000 a $3.999.999'),
                            (rank_7, '$4.000.000 a $4.999.999'),
                            (rank_8, '$5.000.000 a $5.999.999'),
                            (rank_9, '$6.000.000 a $6.999.999'),
                            (rank_10, '> $7.000.000'),
                            (rank_11, 'No definido'), ]
############################################################################################
si = 'Sí'
no = 'No'
contado = 'Contado'
# cotizacion_preaprobacion_cotizacion
PREAPROBACION_COTIZACION_CHOICES = [(si, 'Sí'),
                                    (no, 'No'),
                                    (contado, 'Contado'), ]
############################################################################################
x_rang_en_periodo = 'Por Rango en Período'
x_fecha_sin_modelo = 'Por Fecha sin Modelo'
x_fecha_con_modelo = 'Por Fecha con Modelo'
termino_vnts = 'Término Ventas'
timg_rec_ls = 'Timing Recuperación La Serena'
timg_rec_stgo = 'Timing Recuperación Santiago'
timg_rec_ctdo = 'Timing Recuperación Contados'
# bono_categoria_bono
CATEGORIA_BONO_CHOICES = [(x_rang_en_periodo, 'Por Rango en Período'),
                          (x_fecha_sin_modelo, 'Por Fecha sin Modelo'),
                          (x_fecha_con_modelo, 'Por Fecha con Modelo'),
                          (termino_vnts, 'Término Ventas'),
                          (timg_rec_ls, 'Timing Recuperación La Serena'),
                          (timg_rec_stgo, 'Timing Recuperación Santiago'),
                          (timg_rec_ctdo, 'Timing Recuperación Contados'), ]
############################################################################################
jefe_vnts = 'Jefe de Ventas'
supervisor_vnts = 'Supervisor de Ventas'
vendedor = 'Vendedor'
jefe_oopp = 'Jefe de Operaciones'
# bono_tipo_bono
TIPO_BONO_CHOICES = [
    (jefe_oopp, 'Jefe de Operaciones'),
    (jefe_vnts, 'Jefe de Ventas'),
    (supervisor_vnts, 'Supervisor de Ventas'),
    (vendedor, 'Vendedor')
]
# TIPO_BONO_CHOICES = [(jefe_vnts, 'Jefe de Ventas'),
#                      (supervisor_vnts, 'Supervisor de Ventas'),
#                      (vendedor, 'Vendedor'),
#                      (jefe_oopp, 'Jefe de Operaciones'), ]
############################################################################################
junior = 'Junior'
advance = 'Advance'
senior = 'Senior'
# vendedor_categoria_vendedor
CAT_VENDEDOR_CHOICES = [(junior, 'Junior'),
                     (advance, 'Advance'),
                     (senior, 'Senior'),]
############################################################################################
cierre_negocio = 'Cierre de Negocio'
detalle_pie = 'Detalle Pie'
saldo_contado = 'Saldo Contado'

# pago_categoria_pago
CATEGORIA_PAGO_CHOICES = [(cierre_negocio, 'Cierre de Negocio'),
                     (detalle_pie, 'Detalle Pie'),
                     (saldo_contado, 'Saldo Contado'),]
############################################################################################
# forma_pago
credito = 'Crédito'
contado = 'Contado'
transferencia_bancaria = 'Transferencia Bancaria'
cheque_a_fecha = 'Cheque a fecha'
deposito = 'Depósito'
pago_firma_escritura = 'Pago Firma Escritura'
traspaso_de_saldo = 'Traspaso de Saldo'
cheque_al_dia = 'Cheque al día'
vale_vista = 'Vale Vista'
beneficio_empleador = 'Beneficio Empleador'
pago_con_tarj_credito = 'Pago con tarj. Crédito'
promocion_abono_inmobiliario = 'Promoción Abono Inmobiliario'

FORMA_PAGO_CHOICES = [
    (beneficio_empleador, 'Beneficio Empleador'),
    (cheque_a_fecha, 'Cheque a fecha'),
    (cheque_al_dia, 'Cheque al día'),
    (contado, 'Contado'),
    (credito, 'Crédito'),
    (deposito, 'Depósito'),
    (pago_con_tarj_credito, 'Pago con tarj. Crédito'),
    (pago_firma_escritura, 'Pago Firma Escritura'),
    (promocion_abono_inmobiliario, 'Promoción Abono Inmobiliario'),
    (transferencia_bancaria, 'Transferencia Bancaria'),
    (traspaso_de_saldo, 'Traspaso de Saldo'),
    (vale_vista, 'Vale Vista')
]
# FORMA_PAGO_CHOICES = [(credito, 'Crédito'),
#                       (contado, 'Contado'),
#                       (transferencia_bancaria, 'Transferencia Bancaria'),
#                       (cheque_a_fecha, 'Cheque a fecha'),
#                       (deposito, 'Depósito'),
#                       (pago_firma_escritura, 'Pago Firma Escritura'),
#                       (traspaso_de_saldo, 'Traspaso de Saldo'),
#                       (cheque_al_dia, 'Cheque al día'),
#                       (vale_vista, 'Vale Vista'),
#                       (beneficio_empleador, 'Beneficio Empleador'),
#                       (pago_con_tarj_credito, 'Pago con tarj. Crédito'),
#                       (promocion_abono_inmobiliario, 'Promoción Abono Inmobiliario')]
############################################################################################
# tipo_campo_etapa
texto = 'Texto'
numero = 'Numero'
fecha = 'Fecha'

TIPO_CAMPO_ETAPA = [(texto, 'Texto'),
                    (numero, 'Número'),
                    (fecha, 'Fecha')]
############################################################################################
# orientacion_vivienda
norte = 'Norte'
sur = 'Sur'
oriente = 'ORIENTE'
poniente = 'PONIENTE'
nor_oriente = 'NOR ORIENTE'
sur_poniente = 'SUR PONIENTE'
nor_poniente = 'NOR PONIENTE'
sur_oriente = 'SUR ORIENTE'

ORIENTACION_VIVIENDA = [(norte, 'Norte'),
                        (sur, 'Sur'),
                        (oriente, 'ORIENTE'),
                        (poniente, 'PONIENTE'),
                        (nor_oriente, 'NOR ORIENTE'),
                        (sur_poniente, 'SUR PONIENTE'),
                        (nor_poniente, 'NOR PONIENTE'),
                        (sur_oriente, 'SUR ORIENTE')]
############################################################################################
# tipo_vivienda
departamento = 'Departamento'
casa = 'Casa'

TIPO_VIVIENDA = [(departamento, 'Departamento'),
                 (casa, 'Casa')]
############################################################################################
# piso
uno = '1'
dos = '2'
tres = '3'
cuatro = '4'
cinco = '5'
seis = '6'
siete = '7'
ocho = '8'
nueve = '9'
dies = '10'
once = '11'
doce = '12'
trece = '13'
catorce = '14'
quince = '15'
dieciseis = '16'
diecisiete = '17'
dieciocho = '18'
diecinueve = '19'
veinte = '20'

PISO = [(uno, '1'),
        (dos, '2'),
        (tres, '3'),
        (cuatro, '4'),
        (cinco, '5'),
        (seis, '6'),
        (siete, '7'),
        (ocho, '8'),
        (nueve, '9'),
        (dies, '10'),
        (once, '11'),
        (doce, '12'),
        (trece, '13'),
        (catorce, '14'),
        (quince, '15'),
        (dieciseis, '16'),
        (diecisiete, '17'),
        (dieciocho, '18'),
        (diecinueve, '19'),
        (veinte, '20')]
############################################################################################
#TODO: Revisar redundancia con FORMA_PAGO y si es necesario juntarlas
# tipo_pago
vale_vista_2 = 'Vale Vista'
vale_vista_notaria = 'Vale Vista Notaría'
deposito_2 = 'Depósito'




TIPO_PAGO = [(vale_vista_2, 'Vale Vista'),
                    (vale_vista_notaria, 'Vale Vista Notaría'),
                    (deposito_2, 'Depósito')]
############################################################################################