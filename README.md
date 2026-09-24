# Registro de Auxilios — Semana 15

## Descripción
Sistema de gestión y registro de auxilios de seguridad ciudadana, desarrollado en Python. Permite registrar, consultar, modificar, eliminar y generar estadísticas de atenciones.

## Características
- 🔐 Inicio de sesión (usuario: `policia` / contraseña: `1234`)
- 📝 Registro automático con código secuencial (AT001, AT002...)
- 💾 Persistencia de datos en `datos.json`
- 🔍 Búsqueda por código y por lugar
- ✏️ Modificación de motivo de atención
- 📊 Estadísticas por motivo y por lugar
- 📋 28 motivos de atención disponibles

## Archivos
- `Registros_auxilios.py` → Código principal
- `datos.json` → Base de datos con registros

## Menú
1. Registrar persona atendida
2. Mostrar todos los registros
3. Buscar por código
4. Buscar por lugar
5. Eliminar registro
6. Salir
7. Modificar motivo
8. Estadísticas

## Autor
Richard Girón
