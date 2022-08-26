-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proyecto_dojo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_dojo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto_dojo` DEFAULT CHARACTER SET utf8 ;
USE `proyecto_dojo` ;

-- -----------------------------------------------------
-- Table `proyecto_dojo`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(255) NULL,
  `perfil` TINYINT(2) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_dojo`.`postulantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`postulantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `identificacion` VARCHAR(45) NULL,
  `telefono1` VARCHAR(45) NULL,
  `telefono2` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_dojo`.`produccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`produccion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_p` DATE NULL,
  `cantidad_p` FLOAT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_dojo`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`ventas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_v` DATE NULL,
  `cantidad_v` FLOAT NULL,
  `valor_kilo` FLOAT NULL,
  `total_venta` FLOAT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_dojo`.`gastos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`gastos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_g` DATE NULL,
  `concepto` TEXT NULL,
  `valor` FLOAT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_dojo`.`insumos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_dojo`.`insumos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_in` VARCHAR(45) NULL,
  `und_medida` VARCHAR(20) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `gasto_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_insumos_gastos_idx` (`gasto_id` ASC) VISIBLE,
  CONSTRAINT `fk_insumos_gastos`
    FOREIGN KEY (`gasto_id`)
    REFERENCES `proyecto_dojo`.`gastos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
