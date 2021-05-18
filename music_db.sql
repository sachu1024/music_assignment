-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2021 at 04:01 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `music_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio`
--

CREATE TABLE `audio` (
  `id` int(11) NOT NULL,
  `audio_id` varchar(100) NOT NULL,
  `audio_title` varchar(225) NOT NULL,
  `narrator` varchar(100) NOT NULL,
  `duration` int(100) NOT NULL,
  `upload_time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `audio`
--

INSERT INTO `audio` (`id`, `audio_id`, `audio_title`, `narrator`, `duration`, `upload_time`) VALUES
(3, '12345', '\"BOSS Title Song\"', 'Honey Singh', 5, '5/13/2021, 8:02:37 PM'),
(4, '12346', 'Dare You (Title Track)', 'Dare', 6, '5/13/2021, 8:03:47 PM');

-- --------------------------------------------------------

--
-- Table structure for table `music_table`
--

CREATE TABLE `music_table` (
  `id` int(11) NOT NULL,
  `song_id` bigint(10) NOT NULL,
  `song_name` varchar(100) NOT NULL,
  `duration` float NOT NULL,
  `created_date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `music_table`
--

INSERT INTO `music_table` (`id`, `song_id`, `song_name`, `duration`, `created_date`) VALUES
(7, 1234, 'We use cookies  ', 4, '18/05/2021 12:33:03'),
(8, 1235, 'We use cookies  ', 8, '18/05/2021 12:21:31');

-- --------------------------------------------------------

--
-- Table structure for table `podcast`
--

CREATE TABLE `podcast` (
  `id` int(11) NOT NULL,
  `pod_id` varchar(100) NOT NULL,
  `pod_name` varchar(100) NOT NULL,
  `duration` bigint(20) NOT NULL,
  `upload_time` varchar(10) NOT NULL,
  `host` varchar(100) NOT NULL,
  `participant` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `podcast`
--

INSERT INTO `podcast` (`id`, `pod_id`, `pod_name`, `duration`, `upload_time`, `host`, `participant`) VALUES
(1, '1234', 'ABC', 3, '2pm', 'https://www.google.com/', 'text'),
(3, '1236', 'Test', 3, '2pm', 'https://www.google.com/', 'text');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio`
--
ALTER TABLE `audio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `audio_id` (`audio_id`);

--
-- Indexes for table `music_table`
--
ALTER TABLE `music_table`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `song _id` (`song_id`);

--
-- Indexes for table `podcast`
--
ALTER TABLE `podcast`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pod_id` (`pod_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audio`
--
ALTER TABLE `audio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `music_table`
--
ALTER TABLE `music_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `podcast`
--
ALTER TABLE `podcast`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
