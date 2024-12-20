-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 20, 2024 at 04:26 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bitcoin_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `bitcoin_prices`
--

CREATE TABLE `bitcoin_prices` (
  `id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  `usd_rate` float NOT NULL,
  `low` float NOT NULL,
  `high` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bitcoin_prices`
--

INSERT INTO `bitcoin_prices` (`id`, `timestamp`, `usd_rate`, `low`, `high`) VALUES
(1, '2024-12-19 03:37:15', 102623, 97492, 107754),
(2, '2024-12-19 03:39:48', 102490, 97365.8, 107615),
(3, '2024-12-19 03:40:49', 102454, 97331.6, 107577),
(4, '2024-12-19 03:43:23', 102426, 97304.8, 107547),
(5, '2024-12-19 04:21:55', 102309, 97193.6, 107425),
(6, '2024-12-19 05:47:20', 102704, 97568.9, 107839),
(7, '2024-12-19 05:54:28', 102728, 97591.8, 107865),
(8, '2024-12-19 07:57:04', 102975, 97826, 108123),
(9, '2024-12-19 08:57:40', 102872, 97728.3, 108015),
(10, '2024-12-19 09:40:29', 102824, 97682.7, 107965),
(11, '2024-12-19 14:51:46', 102284, 97169.6, 107398);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bitcoin_prices`
--
ALTER TABLE `bitcoin_prices`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bitcoin_prices`
--
ALTER TABLE `bitcoin_prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
