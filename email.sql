/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.19 : Database - email
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`email` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `email`;

/*Table structure for table `content` */

DROP TABLE IF EXISTS `content`;

CREATE TABLE `content` (
  `id` int NOT NULL AUTO_INCREMENT,
  `source` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4 DEFAULT NULL COMMENT '发件人',
  `to` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '收件人',
  `title` varchar(256) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '标题',
  `text` varchar(4096) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '内容',
  `sendTime` datetime DEFAULT NULL COMMENT '发送时间',
  `status` int DEFAULT '0' COMMENT '0-未读 1-已读',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

/*Data for the table `content` */

insert  into `content`(`id`,`source`,`to`,`title`,`text`,`sendTime`,`status`) values (1,'12@qq.com','123@qq.com','你好','你好','2023-05-07 10:14:48',1),(2,'12@qq.com','123@qq.com','我是续航三','《绝句》是唐代诗人杜甫创作的组诗作品，共有两首。这是一组咏物诗，第一首用自然流畅的语言写出了一派生意盎然的春色，表达了诗人热爱大自然的愉快心情；第二首则在春色秀丽的美景上涂了一层羁旅异乡的愁思和伤感，春色和乡思交相辉映，增添了诗的韵味。这两首诗极生动地、自然地描','2023-05-07 10:48:11',1),(3,'123@qq.com','123','123','123213','2023-05-07 13:48:25',0),(4,'123@qq.com','12@qq.com','12你好','12你好 ，我是123','2023-05-07 13:57:46',0),(5,'123@qq.com','12@qq.com','[回复“你好”] 你也好','谢谢你，12','2023-05-07 14:40:43',0),(6,'123@qq.com','456@qq.com','周五晚上去打羽毛球','你好，456，我是123，下周五晚上去打羽毛球吗','2023-05-07 14:42:20',0),(7,'123@qq.com','123123','123123','12321312','2023-05-07 14:43:48',0),(8,'123@qq.com','2718006248@qq.com','你好','你好，我在测试','2023-05-07 15:00:53',1),(9,'123@qq.com','2718006248@qq.com','213213','123213123','2023-05-07 15:04:34',1),(10,'123@qq.com','2718006248@qq.com','123','213123','2023-05-07 15:27:11',0),(11,'123@qq.com','2718006248@qq.com','2131','123213','2023-05-07 15:28:05',0),(12,'123@qq.com','2718006248@qq.com','123','123','2023-05-07 15:29:20',0),(13,'123@qq.com','2718006248@qq.com','123','1232132131','2023-05-07 15:31:29',0),(15,'2718006248@qq.com','123@qq.com','[回复“你好”]','已收到你的来信','2023-05-07 15:52:44',0),(16,'2718006248@qq.com','2718006248@qq.com','123','123213213','2023-05-07 15:53:01',0),(17,'2718006248@qq.com','2718006248@qq.com','明天是周一','明天是周一明天是周一明天是周一','2023-05-07 15:54:41',0),(18,'123@qq.com','12@qq.com','[回复“你好”]','12312','2023-05-07 16:07:16',0);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `account` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '邮箱账号',
  `password` varchar(32) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`id`,`account`,`password`) values (1,'123@qq.com','123'),(2,'12@qq.com','123'),(4,'271800@qq.com','123'),(5,'1232@qq.com','1232'),(7,'2718006248@qq.com','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
