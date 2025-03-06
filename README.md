# MANUAL TÉCNICO DE INSTALACIÓN
# SonicWall TZ270: Configuración de VPN y Cortafuegos
# English README in progress

## DOCUMENTO TÉCNICO DE REFERENCIA
**Versión**: 1.0  
**Dispositivo**: SonicWall TZ270  
**Fecha**: 06/03/2025  

---

## 1. PROPÓSITO Y ALCANCE

Este manual técnico proporciona las instrucciones detalladas para instalar y configurar el dispositivo SonicWall TZ270, centrándose específicamente en la implementación de servicios de VPN y cortafuegos. El documento está destinado al personal técnico cualificado responsable de implementar infraestructura de seguridad de red.

---

## 2. REQUISITOS PREVIOS

### 2.1 Hardware Necesario
- Dispositivo SonicWall TZ270
- Cable de alimentación
- Cable Ethernet RJ-45
- Ordenador para configuración con navegador web
- Conexión a Internet activa

### 2.2 Información Necesaria
- Credenciales de acceso al dispositivo
- Parámetros de red WAN proporcionados por el ISP
- Esquema de direccionamiento IP interno
- Topología de red completa
- Requisitos de acceso VPN
- Políticas de seguridad de la organización

---

## 3. INSTALACIÓN FÍSICA

### 3.1 Procedimiento de Instalación
1. Desembalar cuidadosamente el dispositivo SonicWall TZ270
2. Comprobar el contenido del paquete contra el listado de componentes
3. Montar el dispositivo en el rack o colocarlo en una superficie plana y estable
4. Conectar el cable de alimentación al dispositivo y a una toma eléctrica protegida
5. Conectar el puerto X1 (WAN) del SonicWall al dispositivo de acceso a internet
6. Conectar el puerto X0 (LAN) del SonicWall al conmutador de red interna
7. Conectar un ordenador de administración directamente al puerto X0 o al conmutador de red interna

## 4. CONFIGURACIÓN INICIAL

### 4.1 Acceso a la Interfaz de Administración
1. Configurar el ordenador para obtener una dirección IP automáticamente (DHCP)
2. Abrir un navegador web e introducir la URL: `https://192.168.168.168`
3. Aceptar la advertencia de seguridad relacionada con el certificado autofirmado
4. Introducir las credenciales de acceso predeterminadas:
   - Usuario: `admin`
   - Contraseña: `password`
5. Se debe cambiar inmediatamente la contraseña predeterminada

### 4.2 Configuración de Red WAN (X1)
1. Navegar a **Network → Interfaces**
2. Seleccionar la interfaz X1
3. Configurar el modo de asignación de IP según el ISP:
   - Para IP estática: Seleccionar "Static" e introducir dirección IP, máscara, pasarela
   - Para DHCP: Seleccionar "DHCP Client"
   - Para PPPoE: Seleccionar "PPPoE" e introducir credenciales del ISP
4. Establecer los servidores DNS primario y secundario
5. Hacer clic en "Aceptar" para guardar los cambios

### 4.3 Configuración de Red LAN (X0)
1. Navegar a **Network → Interfaces**
2. Seleccionar la interfaz X0
3. Establecer la dirección IP y máscara de subred (predeterminada: 192.168.168.168/24)
4. Navegar a **Network → DHCP Server**
5. Configurar el servicio DHCP para la interfaz X0:
   - Rango de direcciones IP (p.ej., 192.168.168.100 - 192.168.168.200)
   - Tiempo de concesión
   - Pasarela predeterminada
   - Servidores DNS
6. Hacer clic en "Aceptar" para guardar los cambios

## 5. CONFIGURACIÓN DEL CORTAFUEGOS

### 5.1 Crear Zonas de Seguridad
1. Acceder a **Network → Zones**
2. Hacer clic en "Agregar" para crear una nueva zona
3. Escribir un nombre descriptivo (p. ej., "Servidores_Internos")
4. Seleccionar el tipo de zona correspondiente
5. Configurar los parámetros de seguridad
6. Pulsar "Aceptar" para guardar
7. Repetir el proceso para cada zona necesaria

### 5.2 Crear Objetos de Red
1. Acceder a **Network → Address Objects**
2. Hacer clic en "Agregar" para crear objeto nuevo
3. Escribir nombre descriptivo
4. Seleccionar tipo de objeto:
   - Host
   - Rango
   - Subred
5. Especificar parámetros de dirección IP
6. Pulsar "Aceptar" para guardar

### 5.3 Configurar Reglas de Acceso
1. Acceder a **Firewall → Access Rules**
2. Hacer clic en "Agregar" para crear regla nueva
3. Configurar parámetros:
   - Zona de origen
   - Zona de destino
   - Servicio (puerto/protocolo)
   - Acción (Permitir/Denegar)
   - Opciones de registro
4. Pulsar "Aceptar" para guardar
5. Ordenar reglas (específicas a generales)

#### Reglas Fundamentales Recomendadas
- Permitir LAN → WAN (acceso a Internet)
- Denegar WAN → LAN (protección red interna)
- Reglas específicas para servicios expuestos

### 5.4 Implementar Servicios de Seguridad Avanzada
1. Acceder a **Security Services**
2. Configurar y activar servicios:
   - Gateway Anti-Virus
   - Anti-Spyware
   - Prevención de Intrusiones
   - Filtrado de Contenido
3. Configurar políticas por zonas
4. Especificar acciones:
   - Alertar
   - Prevenir
   - Bloquear
5. Configurar notificaciones de eventos críticos

## 6. CONFIGURACIÓN DE VPN SITE-TO-SITE

### 6.1 Preparación Previa
1. Verificar conectividad a Internet en ambos dispositivos SonicWall
2. Determinar redes locales y remotas para comunicación VPN
3. Obtener direcciones IP públicas (estáticas) de ambos dispositivos
4. Verificar disponibilidad de puertos UDP 500 y 4500

### 6.2 Configuración General VPN
1. Acceder a **VPN → Settings**
2. Habilitar opción VPN
3. Configurar parámetros globales según necesidades

### 6.3 Crear Túnel VPN Site-to-Site
1. Acceder a **VPN → Site-to-Site**
2. Hacer clic en "Agregar"
3. Configurar sección "General":
   - Nombre de conexión (p. ej., "Sede-Central-Sucursal")
   - Habilitar: Sí
   - Versión IKE: IKEv2
   - Gateway primario: IP pública del SonicWall remoto
   - Shared Secret: Clave precompartida (mín. 16 caracteres)

4. Configurar sección "Network":
   - Redes locales: Seleccionar objetos de red local
   - Redes remotas: Seleccionar objetos de red remota

5. Configurar "Proposals" (Fase 1 IKE):
   - Authentication: SHA2-256
   - Encryption: AES-256
   - DH Group: 14 o superior
   - Lifetime: 28800 segundos

6. Configurar "Proposals" (Fase 2 IPsec):
   - Authentication: SHA2-256
   - Encryption: AES-256
   - Lifetime: 3600 segundos
   - Perfect Forward Secrecy: Habilitado, Grupo DH 14

7. Pulsar "Aceptar" para guardar

## 7. CONFIGURACIÓN SSL-VPN

### 7.1 Configuración General
1. Acceder a **VPN → SSL-VPN → Settings**
2. Habilitar servicio SSL-VPN
3. Configurar puerto de escucha (pred.: 443)
4. Seleccionar interfaces para conexiones SSL-VPN

### 7.2 Configuración Autenticación
1. Acceder a **VPN → SSL-VPN → Authentication**
2. Seleccionar método:
   - Base de usuarios local
   - RADIUS
   - LDAP
   - Active Directory
3. Configurar parámetros del servidor de autenticación
4. Crear/importar usuarios y grupos VPN

### 7.3 Configuración Portal
1. Acceder a **VPN → SSL-VPN → Portal Settings**
2. Configurar rango IP para clientes
3. Especificar máscara de subred, DNS y WINS
4. Configurar tiempo de inactividad
5. Personalizar apariencia del portal

### 7.4 Configuración NetExtender
1. Acceder a **VPN → SSL-VPN → Client Settings**
2. Habilitar NetExtender
3. Configurar políticas de acceso:
   - Rutas para división de túnel
   - Restricciones horarias
   - Tiempo máximo de conexión
   - Opciones de cliente

## 8. VERIFICACIÓN Y PRUEBAS

### 8.1 Verificar Conectividad Básica
1. Acceder a **System → Status**
2. Verificar estado de interfaces:
   - Estado: Activo
   - Configuración IP correcta
   - Velocidad/duplex adecuados
3. Realizar pruebas desde **System → Diagnostics**:
   - Ping a puerta de enlace ISP
   - Ping a 8.8.8.8
   - Resolución DNS
   
### 8.2 Verificar el Cortafuegos
1. Acceder a **System → Logs → Firewall**
2. Comprobar registros de actividad:
   - Tráfico permitido
   - Tráfico denegado
3. Realizar pruebas de conectividad:
   - Acceso a Internet desde LAN
   - Funcionamiento de reglas específicas
   - Bloqueo de tráfico no autorizado

### 8.3 Verificar VPN Site-to-Site
1. Acceder a **VPN → Site-to-Site → Status**
2. Comprobar estado del túnel:
   - Estado: Up
   - Estadísticas de tráfico
3. Realizar pruebas de conectividad:
   - Ping entre redes conectadas
   - Acceso a servicios
4. Revisar registros en **System → Logs → VPN**

### 8.4 Verificar SSL-VPN
1. Preparar equipo de prueba:
   - Instalar NetExtender
   - Configurar conexión al SonicWall
2. Probar conexión remota:
   - Autenticación de usuario
   - Asignación de IP
   - Acceso a recursos internos
3. Verificar registros:
   - Conexiones exitosas
   - Intentos fallidos
   - Uso de recursos
   
## 9. MANTENIMIENTO Y MEJORES PRÁCTICAS

### 9.1 Actualización de Firmware
1. Acceder a **System → Settings**
2. Comprobar la versión actual del firmware
3. Descargar la última versión del firmware desde el portal de soporte de SonicWall
4. Acceder a **System → Settings → Firmware Management**
5. Seleccionar el archivo de firmware descargado
6. Iniciar el proceso de actualización
7. Programar actualizaciones durante ventanas de mantenimiento

### 9.2 Copias de Seguridad de Configuración
1. Acceder a **System → Settings → Backup & Restore**
2. Hacer clic en "Create Backup" para generar un archivo de copia de seguridad
3. Descargar el archivo a una ubicación segura
4. Programar copias de seguridad periódicas, especialmente antes de cambios importantes

### 9.3 Supervisión y Alertas
1. Acceder a **System → Notifications**
2. Configurar notificaciones por correo electrónico para eventos críticos:
   - Intentos de intrusión
   - Fallos de VPN
   - Cambios de estado de interfaces
   - Problemas de hardware

### 9.4 Mejores Prácticas de Seguridad
1. Mantener actualizado el firmware del dispositivo
2. Cambiar periódicamente las contraseñas de administración
3. Utilizar autenticación de dos factores cuando sea posible
4. Revisar regularmente los registros de seguridad
5. Documentar todas las configuraciones y cambios
6. Implementar el principio de mínimo privilegio para todas las reglas
7. Segmentar la red utilizando VLANs y zonas

---

## 10. RESOLUCIÓN DE PROBLEMAS

### 10.1 Problemas de Conectividad WAN
1. Verificar el estado físico de las conexiones
2. Comprobar la configuración de la interfaz WAN
3. Verificar conectividad con la pasarela del ISP
4. Contactar con el ISP si es necesario

### 10.2 Problemas de Cortafuegos
1. Revisar las reglas de acceso para detectar conflictos o errores
2. Verificar los registros del cortafuegos para tráfico bloqueado
3. Utilizar la herramienta "Monitor de Paquetes" para analizar el tráfico en tiempo real

### 10.3 Problemas de VPN Site-to-Site
1. Verificar que ambos dispositivos tengan conectividad a Internet
2. Confirmar que las configuraciones de IKE e IPsec coincidan en ambos extremos
3. Verificar que los puertos UDP 500 y 4500 estén abiertos
4. Comprobar la validez de la clave precompartida
5. Revisar los registros VPN para mensajes de error específicos

## 12. NOTAS DE LA VERSIÓN

### 12.1 Historial de Cambios
- Versión 1.0 (06/03/2025)
  - Documento inicial
  - Incluir configuración básica del cortafuegos
  - Añadir sección de VPN Site-to-Site
  - Incorporar configuración SSL-VPN

### 12.2 Control del Documento
- Autor: Javier Fuertes
- Revisor: xxxxx
- Aprobado por: XXXXX
- Próxima revisión: 06/03/2026

---
