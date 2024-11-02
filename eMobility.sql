-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.5.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para emobility
CREATE DATABASE IF NOT EXISTS `emobility` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `emobility`;

-- Volcando estructura para tabla emobility.consumo
CREATE TABLE IF NOT EXISTS `consumo` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vehiculo_ID` int(11) DEFAULT NULL,
  `Distancia` decimal(10,2) NOT NULL,
  `ConsumoEnergia` decimal(10,2) NOT NULL,
  `EmisionesEvitadas` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Vehiculo_ID` (`Vehiculo_ID`),
  CONSTRAINT `consumo_ibfk_1` FOREIGN KEY (`Vehiculo_ID`) REFERENCES `vehiculos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla emobility.consumo: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.distancias
CREATE TABLE IF NOT EXISTS `distancias` (
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

-- Volcando datos para la tabla emobility.distancias: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.estadisticasuso
CREATE TABLE IF NOT EXISTS `estadisticasuso` (
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

-- Volcando datos para la tabla emobility.estadisticasuso: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.feedbackusuarios
CREATE TABLE IF NOT EXISTS `feedbackusuarios` (
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

-- Volcando datos para la tabla emobility.feedbackusuarios: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.login
CREATE TABLE IF NOT EXISTS `login` (
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla emobility.login: ~3 rows (aproximadamente)
INSERT INTO `login` (`login_ID`, `usuario_ID`, `username`, `password`, `login_time`, `status`) VALUES
	(1, 1, 'admin@example.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '2024-10-10 22:28:20', 'exitoso'),
	(2, 3, '6699182085', 'fafd3d12eda13d9ecd18c11401f576839c9f36249d6ada79151f580be233c25e', '2024-10-18 22:29:21', 'particular'),
	(3, 4, '1234567890', '938fa967265e035d262078154ba4c5d7f73971f4f0e7c02e231f036067b3479e', '2024-10-18 22:36:55', 'particular'),
	(4, 5, 'axel@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '2024-10-18 22:42:18', 'particular');

-- Volcando estructura para tabla emobility.mantenimiento
CREATE TABLE IF NOT EXISTS `mantenimiento` (
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

-- Volcando datos para la tabla emobility.mantenimiento: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.pagos
CREATE TABLE IF NOT EXISTS `pagos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Renta_ID` int(11) DEFAULT NULL,
  `Monto` decimal(10,2) NOT NULL,
  `FechaPago` datetime DEFAULT current_timestamp(),
  `MetodoPago` enum('tarjeta','efectivo','app') NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Renta_ID` (`Renta_ID`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`Renta_ID`) REFERENCES `rentas` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla emobility.pagos: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.rentas
CREATE TABLE IF NOT EXISTS `rentas` (
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

-- Volcando datos para la tabla emobility.rentas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.reservas
CREATE TABLE IF NOT EXISTS `reservas` (
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

-- Volcando datos para la tabla emobility.reservas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla emobility.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `TipoUsuario` enum('particular','empresa') NOT NULL,
  `FechaRegistro` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla emobility.usuarios: ~3 rows (aproximadamente)
INSERT INTO `usuarios` (`ID`, `Nombre`, `Email`, `telefono`, `TipoUsuario`, `FechaRegistro`) VALUES
	(1, 'Admin', 'admin@example.com', '1234567890', 'particular', '2024-10-10 22:28:20'),
	(3, 'Axel', '6699182085', '1234', 'particular', '2024-10-18 22:29:21'),
	(4, 'Josue', '1234567890', '1234', 'particular', '2024-10-18 22:36:55'),
	(5, 'Axel', 'axel@gmail.com', '6699182085', 'particular', '2024-10-18 22:42:18');

-- Volcando estructura para tabla emobility.vehiculos
CREATE TABLE IF NOT EXISTS `vehiculos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TipoVehiculo` enum('carro','bicicleta','patineta') NOT NULL,
  `Modelo` varchar(100) DEFAULT NULL,
  `CapacidadBateria` int(11) NOT NULL,
  `ConsumoEnergiaKM` decimal(10,2) NOT NULL,
  `PrecioHora` decimal(10,2) NOT NULL,
  `Estado` enum('disponible','en mantenimiento','reservado') DEFAULT 'disponible',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla emobility.vehiculos: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
