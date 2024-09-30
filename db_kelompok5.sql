-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 30 Des 2023 pada 02.06
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_kelompok5`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `transaction_id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `vcd_id` int(11) NOT NULL,
  `vcd` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `image` text NOT NULL,
  `active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`transaction_id`, `email`, `customer_name`, `vcd_id`, `vcd`, `date`, `price`, `image`, `active`) VALUES
(41, 'tuyul123@mail.com', 'Tuyul Film', 31, 'Barbie', '29 December 2023', 35000, 'barbie.jpg', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`email`, `name`, `password`, `role`) VALUES
('admin@gmail.com', 'admin', 'admin', 'admin'),
('audi.hagi2002@gmail.com', 'Audi', 'audi', 'admin'),
('axel.rham.rus@gmail.com', 'Axel Rhamadani Rusdiansyah', 'axel1234', 'user'),
('turndownforwhat@mail.com', 'Turn Down for What', '1234', 'user'),
('tuyul123@mail.com', 'Tuyul Film', 'tuyul123', 'user'),
('user@gmail.com', 'user', 'user', 'user'),
('vickyfrans1@gmail.com', 'Vicky', 'vicky', 'admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `vcd`
--

CREATE TABLE `vcd` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `image` text DEFAULT NULL,
  `price` int(11) NOT NULL,
  `genre` enum('COMEDY','FANTASY','HORROR') NOT NULL,
  `stock` int(11) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `vcd`
--

INSERT INTO `vcd` (`id`, `title`, `image`, `price`, `genre`, `stock`, `description`) VALUES
(25, 'Five Nights at Freddy\'s', 'fnaf.jpg', 5000, 'HORROR', 6, 'Recently fired and desperate for work, a troubled young man named Mike agrees to take a position as a night security guard at an abandoned theme restaurant: Freddy Fazbear\'s Pizzeria. But he soon discovers that nothing at Freddy\'s is what it seems.'),
(26, 'Loki', 'loki.jpg', 10000, 'FANTASY', 2, 'After stealing the Tesseract during the events of “Avengers: Endgame,” an alternate version of Loki is brought to the mysterious Time Variance Authority, a bureaucratic organization that exists outside of time and space and monitors the timeline. They give Loki a choice: face being erased from existence due to being a “time variant” or help fix the timeline and stop a greater threat.'),
(27, 'Pluto', 'pluto.jpg', 15000, 'COMEDY', 7, 'When the world’s seven most advanced robots and their human allies are murdered one by one, Inspector Gesicht soon discovers that he’s also in danger.'),
(28, 'Family Guy', 'fg.jpg', 20000, 'COMEDY', 4, 'Sick, twisted, politically incorrect and Freakin\' Sweet animated series featuring the adventures of the dysfunctional Griffin family. Bumbling Peter and long-suffering Lois have three kids. Stewie (a brilliant but sadistic baby bent on killing his mother and taking over the world), Meg (the oldest, and is the most unpopular girl in town) and Chris (the middle kid, he\'s not very bright but has a passion for movies). The final member of the family is Brian - a talking dog and much more than a pet, he keeps Stewie in check whilst sipping Martinis and sorting through his own life issues.'),
(29, 'Expend4bles', 'expend4bles.jpg', 25000, 'HORROR', 4, 'Armed with every weapon they can get their hands on and the skills to use them, The Expendables are the world’s last line of defense and the team that gets called when all other options are off the table. But new team members with new styles and tactics are going to give “new blood” a whole new meaning.'),
(30, 'Saw X', 'saw.jpg', 30000, 'HORROR', 5, 'Between the events of \'Saw\' and \'Saw II\', a sick and desperate John Kramer travels to Mexico for a risky and experimental medical procedure in hopes of a miracle cure for his cancer, only to discover the entire operation is a scam to defraud the most vulnerable. Armed with a newfound purpose, the infamous serial killer returns to his work, turning the tables on the con artists in his signature visceral way through devious, deranged, and ingenious traps.'),
(31, 'Barbie', 'barbie.jpg', 35000, 'FANTASY', 7, 'Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.'),
(32, 'The Doorman', 'thedoorman.jpg', 40000, 'COMEDY', 8, 'Waldisney works as a doorman in a building where confusion is constant. However, the employee is great at maintaining a certain order. When wrongly accused of stealing something, he will need to prove that he is anything but a thief.'),
(33, 'Scooby-Doo! And Krypto, Too!', 'ScoobyDoo.jpg', 45000, 'COMEDY', 8, 'When the Justice League goes missing and villains overrun Metropolis, there\'s only one team that can solve this mystery: Scooby-Doo and the gang! But wait, there\'s a new dog in town – Krypto – Superman\'s Superdog with Super Powers. Mystery Inc. will need all the help it can get when phantoms menace the Justice League\'s headquarters.'),
(34, 'Elemental', 'elemental.jpg', 50000, 'FANTASY', 10, 'In a city where fire, water, land and air residents live together, a fiery young woman and a go-with-the-flow guy will discover something elemental: how much they have in common.'),
(35, 'Coco', 'coco.jpg', 55000, 'FANTASY', 11, 'Despite his family’s baffling generations-old ban on music, Miguel dreams of becoming an accomplished musician like his idol, Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events. Along the way, he meets charming trickster Hector, and together, they set off on an extraordinary journey to unlock the real story behind Miguel\'s family history.'),
(36, 'The Nun II', 'nun.jpg', 60000, 'HORROR', 11, 'In 1956 France, a priest is violently murdered, and Sister Irene begins to investigate. She once again comes face-to-face with a powerful evil.'),
(37, 'Wonka', 'wonkaaa.jpg', 60000, 'FANTASY', 7, 'Armed with nothing but a hatful of dreams, young chocolatier Willy Wonka manages to change the world, one delectable bite at a time.');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`transaction_id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`email`);

--
-- Indeks untuk tabel `vcd`
--
ALTER TABLE `vcd`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT untuk tabel `vcd`
--
ALTER TABLE `vcd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;