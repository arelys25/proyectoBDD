/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.5.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: emobility
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `bike`
--

DROP TABLE IF EXISTS `bike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bike` (
  `id_bike` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `voltajeVolts` int(11) NOT NULL,
  `peso_soporte_kg` decimal(2,2) NOT NULL,
  `velocidad_maxima_kmH` int(11) NOT NULL,
  `peso_kg` decimal(2,2) NOT NULL,
  `luces` tinyint(1) DEFAULT NULL,
  `accesorio_includ` varchar(100) DEFAULT NULL,
  `precio_renta_dls` decimal(4,2) NOT NULL,
  PRIMARY KEY (`id_bike`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bike`
--

LOCK TABLES `bike` WRITE;
/*!40000 ALTER TABLE `bike` DISABLE KEYS */;
/*!40000 ALTER TABLE `bike` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coche`
--

DROP TABLE IF EXISTS `coche`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coche` (
  `modelo` varchar(100) NOT NULL,
  `autonomia_km` int(11) NOT NULL,
  `potencia_hp` int(11) NOT NULL,
  `velocidad_maxima_kmH` int(11) NOT NULL,
  `tiempo_carga_cargadorN2_min` int(11) NOT NULL,
  `tiempo_carga_cargaRapida_min` int(11) DEFAULT NULL,
  `id_coche` int(11) NOT NULL AUTO_INCREMENT,
  `precio_renta_dls` decimal(4,2) NOT NULL,
  `lugares` int(11) NOT NULL,
  `maletas` int(11) NOT NULL,
  `seguro` tinyint(1) NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_coche`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coche`
--

LOCK TABLES `coche` WRITE;
/*!40000 ALTER TABLE `coche` DISABLE KEYS */;
/*!40000 ALTER TABLE `coche` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumo`
--

DROP TABLE IF EXISTS `consumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consumo` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `Distancia` decimal(10,2) NOT NULL,
  `ConsumoEnergia` decimal(10,2) NOT NULL,
  `EmisionesEvitadas` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `consumo_ibfk_1` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumo`
--

LOCK TABLES `consumo` WRITE;
/*!40000 ALTER TABLE `consumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `consumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distancias`
--

DROP TABLE IF EXISTS `distancias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `distancias` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `Usuario_ID` int(11) DEFAULT NULL,
  `Distancia` decimal(10,2) NOT NULL,
  `FechaViaje` datetime NOT NULL,
  `TiempoViaje` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  CONSTRAINT `distancias_ibfk_1` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`),
  CONSTRAINT `distancias_ibfk_2` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distancias`
--

LOCK TABLES `distancias` WRITE;
/*!40000 ALTER TABLE `distancias` DISABLE KEYS */;
/*!40000 ALTER TABLE `distancias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadisticasuso`
--

DROP TABLE IF EXISTS `estadisticasuso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estadisticasuso` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario_ID` int(11) DEFAULT NULL,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `TotalViajes` int(11) DEFAULT 0,
  `AhorroKWh` decimal(10,2) DEFAULT 0.00,
  `AhorroCO2` decimal(10,2) DEFAULT 0.00,
  `FechaRegistro` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `estadisticasuso_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`),
  CONSTRAINT `estadisticasuso_ibfk_2` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadisticasuso`
--

LOCK TABLES `estadisticasuso` WRITE;
/*!40000 ALTER TABLE `estadisticasuso` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadisticasuso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedbackusuarios`
--

DROP TABLE IF EXISTS `feedbackusuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedbackusuarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario_ID` int(11) DEFAULT NULL,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `Calificacion` int(11) DEFAULT NULL CHECK (`Calificacion` between 1 and 5),
  `Comentarios` text DEFAULT NULL,
  `Fecha` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `feedbackusuarios_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`),
  CONSTRAINT `feedbackusuarios_ibfk_2` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedbackusuarios`
--

LOCK TABLES `feedbackusuarios` WRITE;
/*!40000 ALTER TABLE `feedbackusuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedbackusuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `login_ID` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_ID` int(11) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `login_time` datetime DEFAULT current_timestamp(),
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_ID`),
  UNIQUE KEY `username` (`username`),
  KEY `usuario_ID` (`usuario_ID`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuarios` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES
(1,1,'admin@example.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2024-10-10 22:28:20','exitoso'),
(2,3,'6699182085','fafd3d12eda13d9ecd18c11401f576839c9f36249d6ada79151f580be233c25e','2024-10-18 22:29:21','particular'),
(3,4,'1234567890','938fa967265e035d262078154ba4c5d7f73971f4f0e7c02e231f036067b3479e','2024-10-18 22:36:55','particular'),
(4,5,'axel@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2024-10-18 22:42:18','particular'),
(5,6,'arely@example.com','bf034ae358554ed9c3108e24da257bfe0a7befd3f2a34593f2dc09888a5eacd1','2024-10-24 12:11:37','particular'),
(6,8,'sinai@emaple.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2024-11-03 09:38:42','particular');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimiento`
--

DROP TABLE IF EXISTS `mantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mantenimiento` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `TipoMantenimiento` varchar(100) DEFAULT NULL,
  `Fecha` datetime NOT NULL,
  `Descripcion` text DEFAULT NULL,
  `Costo` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `mantenimiento_ibfk_1` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimiento`
--

LOCK TABLES `mantenimiento` WRITE;
/*!40000 ALTER TABLE `mantenimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Renta_ID` int(11) DEFAULT NULL,
  `Monto` decimal(10,2) NOT NULL,
  `FechaPago` datetime DEFAULT current_timestamp(),
  `MetodoPago` enum('tarjeta','efectivo','app') NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Renta_ID` (`Renta_ID`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`Renta_ID`) REFERENCES `rentas` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rentas`
--

DROP TABLE IF EXISTS `rentas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rentas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario_ID` int(11) DEFAULT NULL,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `FechaInicio` datetime NOT NULL,
  `FechaFin` datetime NOT NULL,
  `DistanciaRecorrida` decimal(10,2) DEFAULT NULL,
  `CostoTotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `rentas_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`),
  CONSTRAINT `rentas_ibfk_2` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentas`
--

LOCK TABLES `rentas` WRITE;
/*!40000 ALTER TABLE `rentas` DISABLE KEYS */;
/*!40000 ALTER TABLE `rentas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Usuario_ID` int(11) DEFAULT NULL,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `FechaReserva` datetime NOT NULL,
  `HoraReserva` time NOT NULL,
  `EstadoReserva` enum('confirmada','cancelada') DEFAULT 'confirmada',
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`),
  CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scooter`
--

DROP TABLE IF EXISTS `scooter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scooter` (
  `marca` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `id_scooter` int(11) NOT NULL AUTO_INCREMENT,
  `tamano` varchar(50) NOT NULL,
  `peso_kg` decimal(2,2) NOT NULL,
  `voltajeVolts` int(11) NOT NULL,
  `tiempo_carga_hrs` int(11) NOT NULL,
  `velocidad_maxima_kmH` int(11) NOT NULL,
  `peso_soporte_kg` decimal(2,2) NOT NULL,
  `plegable` tinyint(1) DEFAULT NULL,
  `personas` int(11) NOT NULL,
  `seguro` tinyint(1) DEFAULT NULL,
  `precio_renta_dls` decimal(4,2) NOT NULL,
  PRIMARY KEY (`id_scooter`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scooter`
--

LOCK TABLES `scooter` WRITE;
/*!40000 ALTER TABLE `scooter` DISABLE KEYS */;
/*!40000 ALTER TABLE `scooter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `TipoUsuario` enum('particular','empresa') NOT NULL,
  `FechaRegistro` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES
(1,'Admin','admin@example.com','1234567890','particular','2024-10-10 22:28:20'),
(3,'Axel','6699182085','1234','particular','2024-10-18 22:29:21'),
(4,'Josue','1234567890','1234','particular','2024-10-18 22:36:55'),
(5,'Axel','axel@gmail.com','6699182085','particular','2024-10-18 22:42:18'),
(6,'arely','arely@example.com','3315257812','particular','2024-10-24 12:11:37'),
(8,'sinai','sinai@emaple.com','12341234','particular','2024-11-03 09:38:42');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculos`
--

DROP TABLE IF EXISTS `vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehiculos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TipoVehiculo` enum('carro','bicicleta','patineta') NOT NULL,
  `Modelo` varchar(100) DEFAULT NULL,
  `CapacidadBateria` int(11) NOT NULL,
  `ConsumoEnergiaKM` decimal(10,2) NOT NULL,
  `PrecioHora` decimal(10,2) NOT NULL,
  `Estado` enum('disponible','en mantenimiento','reservado') DEFAULT 'disponible',
  `id_tipo` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_scooter` (`id_tipo`),
  CONSTRAINT `fk_bike` FOREIGN KEY (`id_tipo`) REFERENCES `bike` (`id_bike`),
  CONSTRAINT `fk_coche` FOREIGN KEY (`id_tipo`) REFERENCES `coche` (`id_coche`),
  CONSTRAINT `fk_scooter` FOREIGN KEY (`id_tipo`) REFERENCES `scooter` (`id_scooter`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculos`
--

LOCK TABLES `vehiculos` WRITE;
/*!40000 ALTER TABLE `vehiculos` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehiculos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2024-11-05 19:26:53
