/*
 Navicat Premium Dump SQL

 Source Server         : MySQL 8.0
 Source Server Type    : MySQL
 Source Server Version : 80037 (8.0.37)
 Source Host           : localhost:3307
 Source Schema         : library

 Target Server Type    : MySQL
 Target Server Version : 80037 (8.0.37)
 File Encoding         : 65001

 Date: 05/07/2024 14:51:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `publisher` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `isbn` bigint NOT NULL,
  `published_year` bigint NULL DEFAULT NULL,
  `category_id` bigint NULL DEFAULT NULL,
  `cover` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `summary` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title` ASC) USING BTREE,
  UNIQUE INDEX `isbn`(`isbn` ASC) USING BTREE,
  UNIQUE INDEX `unique_title`(`title` ASC) USING BTREE,
  INDEX `books_category_id_1efdc3d3_fk_categories_id`(`category_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of books
-- ----------------------------
INSERT INTO `books` VALUES (1, 'MySQL数据库基础', '杜辉，李纲', '哈尔滨工程大学出版社', 9787566135094, 2022, 18, NULL, NULL);
INSERT INTO `books` VALUES (2, '高等数学·上册: 第七版', '同济大学数学系', '高等教育出版社', 9787040396638, 2014, 7, NULL, '《高等数学·上册》包括函数与极限、导数与微分、微分中值定理与导数的应用、不定积分、定积分及其应用、微分方程等内容，书末还附有二阶和三阶行列式简介、基本初等函数的图形、几种常用的曲线、积分表、习题答案与提示。');
INSERT INTO `books` VALUES (3, '围城 出版七十周年纪念版', '钱锺书', '人民文学出版社', 9787020127894, 2017, 9, NULL, '围城故事发生于1920到1940年代。主角方鸿渐是个从中国南方乡绅家庭走出的青年人，迫于家庭压力与同乡周家女子订亲。但在其上大学期间，周氏患病早亡。准岳父周先生被方所写的唁电感动，资助他出国求学。\r\n方鸿渐在欧洲游学期间，不理学业。为了给家人一个交待，方于毕业前购买了虚构的“克莱登大学”的博士学位证书，并随海外学成的学生回国。在船上与留学生鲍小姐相识并热恋，但被鲍小姐欺骗感情。同时也遇见了大学同学苏文纨。\r\n到达上海后，在已故未婚妻父亲周先生开办的银行任职。此时，方获得了同学苏文纨的青睐，又与苏的表妹唐晓芙一见钟情，整日周旋于苏、唐二人之间，期间并结识了追求苏文纨的赵辛楣。方最终与苏、唐二人感情终结，苏嫁与诗人曹元朗，而赵也明白方并非其情敌，从此与方惺惺相惜。方鸿渐逐渐与周家不和。\r\n抗战开始，方家逃难至上海的租界。在赵辛楣的引荐下，与赵辛楣、孙柔嘉、顾尔谦、李梅亭几人同赴位于内地的三闾大学任教。由于方鸿渐性格等方面的弱点，陷入了复杂的人际纠纷当中。后与孙柔嘉订婚，并离开三闾大学回到上海。在赵辛楣的帮助下，方鸿渐在一家报馆任职，与孙柔嘉结婚。\r\n婚后，方鸿渐夫妇与方家、孙柔嘉姑母家的矛盾暴露并激化。方鸿渐辞职并与孙柔嘉吵翻，逐渐失去了生活的希望。');
INSERT INTO `books` VALUES (4, '乡土中国(修订本)', '费孝通', '上海人民出版社', 9787208069428, 2007, 9, NULL, '著名社会学家费孝通教授，一生行行重行行，实地调查和考察总结中国农村经济发展的各种模式，写下了诸多不朽篇章。本书推出的是学界共认的中国乡土社会传统文化和社会结构理论研究的代表作《乡土中国》、《生育制度》、《乡土重建》和《皇权与绅权》四篇著作，可供社会学工作或教学、研究者参考。');
INSERT INTO `books` VALUES (5, '深入理解计算机系统', 'Randal E. Bryant，David R. O’Hallaron', '机械工业出版社', 9787111544937, 2016, 18, NULL, '本书从程序员的视角详细阐述计算机系统的本质概念，并展示这些概念如何实实在在地影响应用程序的正确性、性能和实用性。全书共12章，主要内容包括信息的表示和处理、程序的机器级表示、处理器体系结构、优化程序性能、存储器层次结构、链接、异常控制流、虚拟存储器、系统级I/O、网络编程、并发编程等。书中提供大量的例子和练习，并给出部分答案，有助于读者加深对正文所述概念和知识的理解。\r\n本书的最大优点是为程序员描述计算机系统的实现细节，帮助其在大脑中构造一个层次型的计算机系统，从最底层的数据在内存中的表示到流水线指令的构成，到虚拟存储器，到编译系统，到动态加载库，到最后的用户态应用。通过掌握程序是如何映射到系统上，以及程序是如何执行的，读者能够更好地理解程序的行为为什么是这样的，以及效率低下是如何造成的。\r\n本书适合那些想要写出更快、更可靠程序的程序员阅读，也适合作为高等院校计算机及相关专业本科生、研究生的教材。');
INSERT INTO `books` VALUES (6, '西游记', '吴承恩', '人民文学出版社', 9787020008735, 2010, 9, NULL, '《西游记》以唐朝高僧玄藏西去拜佛取经这一历史事实的基础，经过作者极具想象力的构思及描写，塑造了神勇忠心的孙悟空，迁腐的唐三藏，好吃懒惰的猪八戒以及勤恳的沙和尚的形象，通过西去取经的磨难与艰辛，从中反映出作者对现实的不满，深刻揭露批判了封建社会的黑暗，腐朽和统治阶级的昏庸凶暴。');
INSERT INTO `books` VALUES (7, '战争与和平', '刘辽逸 译，[俄罗斯] 列夫托尔斯泰', '人民文学出版社', 9787020102747, 2015, 9, NULL, '《战争与和平》(1866—1869)描写1812年俄法战争的全过程，以当时四大贵族家庭的人物活动为线索，反映了1805至1820年间许多重大的历史事件，以及各阶层的现实生活，抨击了那些谈吐优雅，但漠视祖国命运的贵族，歌颂了青年一代在战争中表现出来的爱国主义和英雄主义精神，是一部史诗般的鸿篇巨制。');
INSERT INTO `books` VALUES (8, '图灵程序设计丛书：Python 高手进阶之路（套装全10册）', 'Jan Erik Solem, 萨卡尔, 卢布诺维克, Robert Layton, 埃里克·马瑟斯, 赫曼塔·库玛·梅赫塔, BePROUD股份有限公司, 杰奎琳·凯泽尔, 凯瑟琳·贾缪尔, 普拉提克·乔西, 哈利·帕西瓦尔', '人民邮电出版社有限公司', 9780123456786, 2018, 18, NULL, '本套装共包含《Python计算机视觉编程》《Python网络编程攻略》《Python语言及其应用》《Python数据挖掘入门与实践》《Python编程：从入门到实践》《Python科学计算基础教程》《Python项目开发实战（第2版》《Python数据处理》《Python机器学习经典实例》《Python测试驱动开发：使用DjangoSelenium和JavaScript进行Web编程（第2版）》10本书。');
INSERT INTO `books` VALUES (9, 'GitHub入门与实践', '大塚弘记', '人民邮电出版社', 9787115394095, 2015, 18, NULL, '本书从Git的基本知识和操作方法入手，详细介绍了GitHub的各种功能，GitHub与其他工具或服务的协作，使用GitHub的开发流程以及如何将GitHub引入到企业中。在讲解GitHub的代表功能Pull\r\nRequest时，本书专门搭建了供各位读者实践的仓库，邀请各位读者进行Pull Request并共同维护。');
INSERT INTO `books` VALUES (10, '图解TCP/IP（第5版）', '竹下隆史, 村山公保, 荒井透, 苅田幸雄', '人民邮电出版社', 9787115318978, 2013, 18, NULL, '这是一本图文并茂的网络管理技术书籍，旨在让广大读者理解TCP/IP的基本知识、掌握TCP/IP的基本技能。\r\n\r\n书中讲解了网络基础知识、TCP/IP基础知识、数据链路、IP协议、IP协议相关技术、TCP与UDP、路由协议、应用协议、网络安全等内容，引导读者了解和掌握TCP/IP，营造一个安全的、使用放心的网络环境。\r\n\r\n本书适合计算机网络的开发、管理人员阅读，也可作为大专院校相关专业的教学参考书');
INSERT INTO `books` VALUES (11, '深入浅出MySQL: 数据库开发、优化与管理维护', '唐汉明, 翟振兴, 关宝军, 王洪权', '人民邮电出版社', 9787115335494, 2014, 18, NULL, '《深入浅出MySQL：数据库开发、优化与管理维护(第2版)》从数据库的基础、开发、优化、管理维护和架构5个方面对MySQL进行了详细的介绍，每一部分都独立成篇。基础篇主要适合于MySQL的初学者阅读，包括MySQL的安装与配置、SQL基础、MySQL支持的数据类型、MySQL中的运算符、常用函数、图形化工具的使用等内容。开发篇主要适合于MySQL的设计和开发人员阅读，内容包括表类型(存储引擎)的选择、选择合适的数据类型、字符集、索引的设计和使用、视图、存储过程和函数、触发器、事务控制和锁定语句、SQL中的安全问题、SQL Mode及相关问题、分区等。优化篇主要适合于开发人员和数据库管理员阅读，内容包括SQL优化、优化数据库对象、锁问题、优化MySQL Server、磁盘I/O问题、应用优化等。管理维护篇主要适合于数据库管理员阅读，内容包括MySQL高级安装和升级、MySQL中的常用工具、MySQL日志、备份与恢复、MySQL权限与安全、MySQL监控、MySQL常见问题和应用技巧等。架构篇主要适合高级数据库管理人员和数据库架构设计师阅读，包括MySQL复制、MySQL Cluster、高可用架构等内容。');
INSERT INTO `books` VALUES (12, '零信任网络', '埃文·吉尔曼，道格·巴斯', '人民邮电出版社', 9787115510020, 2019, 18, NULL, '本书分为10章，从介绍零信任的基本概念开始，描述了管理信任，网络代理，授权，建立设备信任、用户信任、应用信任以及流量信任，零信任网络的实现和攻击者视图等内容。本书主要展示了零信任如何让读者专注于构建强大的身份认证、授权和加密，同时提供分区访问和更好的操作敏捷性。通过阅读本书，读者将了解零信任网络的架构，包括如何使用当前可用的技术构建一个架构。 本书适合网络工程师、安全工程师、CTO以及对零信任技术感兴趣的读者阅读。');

SET FOREIGN_KEY_CHECKS = 1;
