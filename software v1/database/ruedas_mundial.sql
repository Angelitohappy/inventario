-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2024 a las 23:19:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ruedas_mundial`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen`
--

CREATE TABLE `almacen` (
  `idAlmacen` int(11) NOT NULL,
  `cod_almacen` varchar(20) NOT NULL,
  `nombre_almacen` varchar(45) NOT NULL,
  `ubicacion` varchar(20) NOT NULL,
  `nro_almacen` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `almacen`
--

INSERT INTO `almacen` (`idAlmacen`, `cod_almacen`, `nombre_almacen`, `ubicacion`, `nro_almacen`) VALUES
(1, 'A1', 'Pirelli', 'Maracaibo', '+584146852690'),
(2, 'A2', 'Goodyear Almacen', 'Maracaibo', '+584146852690');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idProducto` int(11) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `marca` varchar(45) NOT NULL,
  `tipo_neumatico` varchar(25) NOT NULL,
  `anchura` float NOT NULL,
  `perfil` float NOT NULL,
  `radio` float NOT NULL,
  `indice_carga` varchar(45) NOT NULL,
  `indice_velocidad` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idProducto`, `codigo`, `marca`, `tipo_neumatico`, `anchura`, `perfil`, `radio`, `indice_carga`, `indice_velocidad`) VALUES
(1, 'C1', 'Pirelli', 'Pista', 13, 13, 13, '13kg', '13km/h');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_almacen`
--

CREATE TABLE `producto_almacen` (
  `idPro` int(11) NOT NULL,
  `idAl` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto_almacen`
--

INSERT INTO `producto_almacen` (`idPro`, `idAl`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_acceso`
--

CREATE TABLE `registro_acceso` (
  `idMovimiento` int(11) NOT NULL,
  `tipo_movimiento` varchar(20) NOT NULL,
  `timeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Id_usuario_registro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_acceso`
--

INSERT INTO `registro_acceso` (`idMovimiento`, `tipo_movimiento`, `timeStamp`, `Id_usuario_registro`) VALUES
(1, 'Modificar Almacen', '2024-07-14 20:52:25', 1),
(2, 'Modificar Almacen', '2024-07-14 20:52:30', 1),
(3, 'Agregar Producto', '2024-07-14 20:52:44', 1),
(4, 'Modificar Producto', '2024-07-14 20:53:06', 1),
(5, 'Movimiento', '2024-07-14 20:53:24', 1),
(6, 'Movimiento', '2024-07-14 20:53:29', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `username` varchar(15) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `direccion` text NOT NULL,
  `clave` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `cedula`, `nombre`, `username`, `correo`, `telefono`, `direccion`, `clave`) VALUES
(1, '29730013', 'Angel Machado', 'Angelitohappy', 'angelandresmachadofernandez@gmail.com', '+584146852690', 'AV 148A-02 CASA NRO 51-114 BARRIO VENEZUELA ES PRIMERO SUR AMERICA ZULIA ZONA POSTAL 4004', 'Cedula2011.'),
(7, 'V-123456789', 'Angel', 'Angelo', 'Angelo@gmail.com', '+58123456789', 'hola\n', 'Cedula2011.'),
(8, 'V-28370302', 'Gerardo', 'gera', 'dqwoidd', '+5804246468434', 'aAAA AAsass adsda\n', 'aA12345678.'),
(10, 'V-31060063', 'jose', 'swordans', 'reyesferrerjose@gmail.com', '+584126757896', 'mi casa cerca de urbe\n', '12832964Zx.'),
(11, 'V-29749146', 'Aleyne', 'Ariosg03', 'Ale03@gmial.com', '+584246251109', 'hola\n', 'Cedula2011.'),
(14, 'V-15749407', 'Ramon Fernandez', 'Elpoli', 'Ramon@gmail.com', '+584146642036', 'sur america\n', 'Matias2lian.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `almacen`
--
ALTER TABLE `almacen`
  ADD PRIMARY KEY (`idAlmacen`),
  ADD UNIQUE KEY `almacen` (`nombre_almacen`),
  ADD UNIQUE KEY `cod` (`cod_almacen`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idProducto`),
  ADD UNIQUE KEY `cod` (`codigo`);

--
-- Indices de la tabla `producto_almacen`
--
ALTER TABLE `producto_almacen`
  ADD UNIQUE KEY `id_almacen_producto` (`idAl`) USING BTREE,
  ADD KEY `id_producto_almacen` (`idPro`);

--
-- Indices de la tabla `registro_acceso`
--
ALTER TABLE `registro_acceso`
  ADD PRIMARY KEY (`idMovimiento`),
  ADD KEY `id_usuario_registro` (`Id_usuario_registro`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `almacen`
--
ALTER TABLE `almacen`
  MODIFY `idAlmacen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `registro_acceso`
--
ALTER TABLE `registro_acceso`
  MODIFY `idMovimiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `producto_almacen`
--
ALTER TABLE `producto_almacen`
  ADD CONSTRAINT `producto_almacen_ibfk_1` FOREIGN KEY (`idPro`) REFERENCES `producto` (`idProducto`) ON DELETE CASCADE,
  ADD CONSTRAINT `producto_almacen_ibfk_2` FOREIGN KEY (`idAl`) REFERENCES `almacen` (`idAlmacen`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `registro_acceso`
--
ALTER TABLE `registro_acceso`
  ADD CONSTRAINT `registro_acceso_ibfk_1` FOREIGN KEY (`Id_usuario_registro`) REFERENCES `usuario` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
