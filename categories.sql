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

 Date: 05/07/2024 14:50:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for categories
-- ----------------------------
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `code`(`code` ASC) USING BTREE,
  UNIQUE INDEX `unique_code`(`code` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of categories
-- ----------------------------
INSERT INTO `categories` VALUES (1, 'A', '马克思主义、列宁主义、毛泽东思想、邓小平理论');
INSERT INTO `categories` VALUES (2, 'B', '哲学、宗教');
INSERT INTO `categories` VALUES (3, 'C', '社会科学总论');
INSERT INTO `categories` VALUES (4, 'D', '政治、法律');
INSERT INTO `categories` VALUES (5, 'E', '军事');
INSERT INTO `categories` VALUES (6, 'F', '经济');
INSERT INTO `categories` VALUES (7, 'G', '文化、科学、教育、体育');
INSERT INTO `categories` VALUES (8, 'H', '语言、文字');
INSERT INTO `categories` VALUES (9, 'I', '文学');
INSERT INTO `categories` VALUES (10, 'J', '艺术');
INSERT INTO `categories` VALUES (11, 'K', '历史、地理');
INSERT INTO `categories` VALUES (12, 'N', '自然科学总论');
INSERT INTO `categories` VALUES (13, 'O', '数理科学和化学');
INSERT INTO `categories` VALUES (14, 'P', '天文学、地球科学');
INSERT INTO `categories` VALUES (15, 'Q', '生物科学');
INSERT INTO `categories` VALUES (16, 'R', '医药、卫生');
INSERT INTO `categories` VALUES (17, 'S', '农业科学');
INSERT INTO `categories` VALUES (18, 'T', '工业技术');
INSERT INTO `categories` VALUES (19, 'U', '交通运输');
INSERT INTO `categories` VALUES (20, 'V', '航空、航天');
INSERT INTO `categories` VALUES (21, 'X', '环境科学、安全科学');
INSERT INTO `categories` VALUES (22, 'Z', '综合性图书');

SET FOREIGN_KEY_CHECKS = 1;
