-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 07, 2023 at 03:42 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `heart_rate`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `account_id` int(255) NOT NULL,
  `account_username` varchar(100) NOT NULL,
  `account_password` char(60) NOT NULL,
  `account_status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`account_id`, `account_username`, `account_password`, `account_status`) VALUES
(1, 'user', '$2b$12$LHO/vyPtCp6aT62UKyuseOKrc7vlGKYNkHjrSocnNFFWz/nwBgkqC', 0),
(2, 'admin', '$2b$12$0djC4DwPli9JxYGlCfSOXuxwIAHZbABPkhUrlJ8w5LnzO5a9T4j6K', 0),
(3, 'user1', '$2b$12$S5jjhr5mbARQz6N8NbKDh.GGWF4FemzUFiBshzl2YcoZEbOMkim/S', 0),
(4, 'user2', '$2b$12$zqYInHY8r7IYk27xFE.yjeHE/hi0S.eO8nq1XlC390fCEsHwwG7vG', 0),
(5, 'user3', '$2b$12$y.XYGpvJqgXwmzWJKcLa.uuTYKpnL3gH7BB8lCdpFEVsrdr.kz8Qq', 0),
(6, 'user4', '$2b$12$Y2cLT61AQMH8HwrSDNAbfeWCzpPhS1Xh83OS15WMUg6ufJQ5L5x8.', 0),
(7, 'user5', '$2b$12$tSBiAFXsWd.DkC7Uh3xCf.RJeCr.mC.6.ITmGnpwX0wbFmSwkGYn6', 0),
(8, 'user6', '$2b$12$G3FZW.oEvyw1n13GpgZtreDYvjiiBTKpP1ZE301YP/qGao4.PmLce', 0),
(9, 'user7', '$2b$12$smlKNM7hUVVJww87dpZ9/ODsrl5EWj/J3/Nd9syLwSL/G3A33POdi', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`account_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `account_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
