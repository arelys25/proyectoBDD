/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.5.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: eMobility
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
  `velocidad_maxima_kmH` int(11) NOT NULL,
  `accesorio_includ` varchar(100) DEFAULT NULL,
  `precio_renta_dls` decimal(4,2) NOT NULL,
  `seguro` tinyint(1) NOT NULL,
  `peso_soporte_kg` decimal(5,2) NOT NULL,
  `peso_kg` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id_bike`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bike`
--

LOCK TABLES `bike` WRITE;
/*!40000 ALTER TABLE `bike` DISABLE KEYS */;
INSERT INTO `bike` VALUES
(1,'Brompton','Electric C Line',36,25,'Bolsa de transporte',12.00,1,105.00,13.70),
(2,'Specialized','Turbo Vado SL 4.0',36,45,'Portaequipaje',15.00,1,120.00,14.90),
(3,'Xiaomi','Himo C26',48,25,'Pantalla LCD',6.00,1,100.00,25.00),
(4,'Ancheer','Power Plus',36,25,'Guardabarros',7.00,1,120.00,23.00),
(5,'Riese & Müller','Supercharger2',36,45,'Pantalla Bosch Kiox',20.00,1,140.00,28.00),
(6,'VanMoof','S3',36,32,'Bloqueo inteligente',14.00,1,120.00,19.00),
(7,'Trek','Allant7',36,32,'Portaequipaje',16.00,1,136.00,23.50),
(8,'Fiido','D11',36,25,'Portaequipaje',8.00,1,120.00,12.90);
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
  `precio_renta_dls` decimal(6,2) DEFAULT NULL,
  `lugares` int(11) NOT NULL,
  `maletas` int(11) NOT NULL,
  `seguro` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_coche`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coche`
--

LOCK TABLES `coche` WRITE;
/*!40000 ALTER TABLE `coche` DISABLE KEYS */;
INSERT INTO `coche` VALUES
('Renault Zoe',395,135,140,480,60,9,45.00,5,338,1),
('Tesla Model 3 Standard Range Plus',438,283,225,540,15,10,128.00,5,425,1),
('Volkswagen ID.4',418,201,150,450,38,11,125.00,5,543,1),
('Tesla Model 3 Long Range AWD',576,346,233,480,15,12,130.00,5,425,1),
('Nissan Leaf',240,147,144,450,NULL,13,85.00,5,435,1),
('Mazda MX-30',161,143,140,300,36,14,120.00,5,366,1),
('Kia Soul EV',383,201,167,540,60,15,65.00,5,315,1),
('Chevrolet Bolt EV',416,200,150,540,60,16,90.00,5,381,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
(6,8,'sinai@emaple.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2024-11-03 09:38:42','particular'),
(7,9,'are@example.com','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','2024-11-06 06:02:00','particular'),
(8,10,'alexis@example.com','5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5','2024-11-06 11:34:28','particular'),
(9,11,'donova@example.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2024-11-12 10:15:46','particular');
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
-- Table structure for table `pago`
--

DROP TABLE IF EXISTS `pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pago` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `monto` decimal(10,2) DEFAULT NULL,
  `fechaPago` datetime DEFAULT current_timestamp(),
  `reserva_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `reserva_ID` (`reserva_ID`),
  CONSTRAINT `pago_ibfk_1` FOREIGN KEY (`reserva_ID`) REFERENCES `reservas` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pago`
--

LOCK TABLES `pago` WRITE;
/*!40000 ALTER TABLE `pago` DISABLE KEYS */;
INSERT INTO `pago` VALUES
(1,80.00,'2024-11-12 16:25:11',1),
(2,112.00,'2024-11-12 18:21:54',2),
(3,80.00,'2024-11-12 21:13:51',3),
(4,160.00,'2024-11-12 21:15:16',4),
(5,16.00,'2024-11-12 21:21:02',5),
(6,64.00,'2024-11-12 21:38:57',6),
(7,72.00,'2024-11-13 00:37:06',7),
(8,540.00,'2024-11-13 01:16:14',8),
(9,768.00,'2024-11-13 01:38:14',9),
(10,72.00,'2024-11-13 01:55:05',10),
(11,78.00,'2024-11-13 02:21:36',11);
/*!40000 ALTER TABLE `pago` ENABLE KEYS */;
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
  `EstadoReserva` enum('confirmada','cancelada') DEFAULT 'confirmada',
  `sucursalID` int(11) DEFAULT NULL,
  `fechaSalida` date DEFAULT NULL,
  `fechaLlegada` date DEFAULT NULL,
  `dias` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  KEY `sucursalID` (`sucursalID`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuarios` (`ID`),
  CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`),
  CONSTRAINT `reservas_ibfk_3` FOREIGN KEY (`sucursalID`) REFERENCES `sucursal` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
INSERT INTO `reservas` VALUES
(1,11,16,'confirmada',NULL,'2024-11-26','2024-11-30',NULL),
(2,11,16,'confirmada',2,'2024-12-01','2024-12-08',7),
(3,11,16,'confirmada',1,'2025-06-25','2025-06-30',5),
(4,11,16,'confirmada',3,'2025-09-15','2025-09-25',10),
(5,11,16,'confirmada',2,'2024-07-25','2024-07-26',1),
(6,11,16,'confirmada',3,'2025-03-10','2025-03-13',3),
(7,11,10,'confirmada',1,'2025-06-25','2025-06-30',5),
(8,11,9,'confirmada',3,'2025-06-25','2025-06-30',5),
(9,11,3,'confirmada',1,'2025-06-25','2025-06-30',5),
(10,11,24,'confirmada',2,'2025-06-25','2025-06-30',5),
(11,11,19,'confirmada',1,'2025-06-25','2025-06-30',5);
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
  `voltajeVolts` int(11) NOT NULL,
  `tiempo_carga_hrs` int(11) NOT NULL,
  `velocidad_maxima_kmH` int(11) NOT NULL,
  `plegable` tinyint(1) DEFAULT NULL,
  `seguro` tinyint(1) DEFAULT NULL,
  `precio_renta_dls` decimal(4,2) NOT NULL,
  `peso_kg` decimal(5,2) NOT NULL,
  `peso_soporte_kg` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id_scooter`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scooter`
--

LOCK TABLES `scooter` WRITE;
/*!40000 ALTER TABLE `scooter` DISABLE KEYS */;
INSERT INTO `scooter` VALUES
('Hiboy','S2 Pro',1,'1180x480x1190 mm',36,6,30,1,1,9.00,16.50,120.00),
('Inokim','OX Super',2,'1200x600x1300 mm',60,8,45,1,1,13.00,28.00,120.00),
('Segway','Ninebot KickScooter MAX G30',3,'1167x472x1203 mm',36,6,25,1,1,10.00,18.70,100.00),
('Mi','Electric Pro 2',4,'1130x430x1180 mm',36,9,25,1,1,8.00,14.20,100.00),
('Kugoo','G-Booster',5,'1200x620x1300 mm',48,10,55,1,1,14.00,30.00,150.00),
('Razor','E300',6,'1040x420x950 mm',24,12,24,1,1,7.00,19.50,100.00),
('Dualtron','Thunder',7,'1238x609x1210 mm',60,15,80,1,1,15.00,43.00,150.00),
('Apollo','City',8,'1210x620x1240 mm',48,8,40,1,1,12.00,18.00,120.00);
/*!40000 ALTER TABLE `scooter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursal`
--

DROP TABLE IF EXISTS `sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sucursal` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `ubicacion` varchar(150) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `horaApertura` time NOT NULL,
  `horaCierre` time NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursal`
--

LOCK TABLES `sucursal` WRITE;
/*!40000 ALTER TABLE `sucursal` DISABLE KEYS */;
INSERT INTO `sucursal` VALUES
(1,'eMobility Guadalajara','Calz. Lázaro Cárdenas 3067, Chapalita, 44500 Guadalajara, Jal.','3347995834','04:00:00','23:59:00'),
(2,'eMobility Zapopan','Av Manuel J. Clouthier 476, Lomas del Seminario, 45020 Zapopan, Jal.','3371469235','04:00:00','23:59:00'),
(3,'eMobility Tonala','Av Río Nilo 9000, Loma Dorada (Ejidal), 45402 Tonalá, Jal.','3315257812','04:00:00','23:59:00');
/*!40000 ALTER TABLE `sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjeta`
--

DROP TABLE IF EXISTS `tarjeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tarjeta` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nomTitular` varchar(100) NOT NULL,
  `numTarjeta` varchar(16) NOT NULL,
  `cvv` int(11) NOT NULL,
  `expiracion` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjeta`
--

LOCK TABLES `tarjeta` WRITE;
/*!40000 ALTER TABLE `tarjeta` DISABLE KEYS */;
INSERT INTO `tarjeta` VALUES
(1,'Arely','5555555555555555',123,'2032-02-01'),
(2,'Arely','6666666666666666',123,'2032-02-01'),
(3,'Alexis','9999999999999999',321,'2025-01-01');
/*!40000 ALTER TABLE `tarjeta` ENABLE KEYS */;
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
  `tarjeta_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `tarjeta_ID` (`tarjeta_ID`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`tarjeta_ID`) REFERENCES `tarjeta` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES
(1,'Admin','admin@example.com','1234567890','particular','2024-10-10 22:28:20',NULL),
(3,'Axel','6699182085','1234','particular','2024-10-18 22:29:21',NULL),
(4,'Josue','1234567890','1234','particular','2024-10-18 22:36:55',NULL),
(5,'Axel','axel@gmail.com','6699182085','particular','2024-10-18 22:42:18',NULL),
(6,'arely','arely@example.com','3315257812','particular','2024-10-24 12:11:37',NULL),
(8,'sinai','sinai@emaple.com','12341234','particular','2024-11-03 09:38:42',NULL),
(9,'ARELY','are@example.com','12345','particular','2024-11-06 06:02:00',NULL),
(10,'alexis','alexis@example.com','3314789654','particular','2024-11-06 11:34:28',NULL),
(11,'Donovan','donova@example.com','3317587158','particular','2024-11-12 10:15:46',3);
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
  `Estado` enum('disponible','en mantenimiento','reservado') DEFAULT 'disponible',
  `id_coche` int(11) DEFAULT NULL,
  `id_bike` int(11) DEFAULT NULL,
  `id_scooter` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `id_coche` (`id_coche`),
  KEY `id_bike` (`id_bike`),
  KEY `id_scooter` (`id_scooter`),
  CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`id_coche`) REFERENCES `coche` (`id_coche`),
  CONSTRAINT `vehiculos_ibfk_2` FOREIGN KEY (`id_bike`) REFERENCES `bike` (`id_bike`),
  CONSTRAINT `vehiculos_ibfk_3` FOREIGN KEY (`id_scooter`) REFERENCES `scooter` (`id_scooter`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculos`
--

LOCK TABLES `vehiculos` WRITE;
/*!40000 ALTER TABLE `vehiculos` DISABLE KEYS */;
INSERT INTO `vehiculos` VALUES
(2,'carro','reservado',9,NULL,NULL),
(3,'carro','reservado',10,NULL,NULL),
(4,'carro','reservado',11,NULL,NULL),
(5,'carro','reservado',12,NULL,NULL),
(6,'carro','reservado',13,NULL,NULL),
(7,'carro','reservado',14,NULL,NULL),
(8,'carro','reservado',15,NULL,NULL),
(9,'carro','reservado',16,NULL,NULL),
(10,'bicicleta','reservado',NULL,1,NULL),
(11,'bicicleta','reservado',NULL,2,NULL),
(12,'bicicleta','reservado',NULL,3,NULL),
(13,'bicicleta','reservado',NULL,4,NULL),
(14,'bicicleta','reservado',NULL,5,NULL),
(15,'bicicleta','reservado',NULL,6,NULL),
(16,'bicicleta','reservado',NULL,7,NULL),
(17,'bicicleta','reservado',NULL,8,NULL),
(18,'patineta','reservado',NULL,NULL,1),
(19,'patineta','reservado',NULL,NULL,2),
(20,'patineta','reservado',NULL,NULL,3),
(21,'patineta','reservado',NULL,NULL,4),
(22,'patineta','reservado',NULL,NULL,5),
(23,'patineta','reservado',NULL,NULL,6),
(24,'patineta','reservado',NULL,NULL,7),
(25,'patineta','reservado',NULL,NULL,8);
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

-- Dump completed on 2024-11-13  2:32:27
