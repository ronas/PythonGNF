

-- create database LojaDB;

create table `LojaDB`.`Produtos` (
	`Codigo` varchar(10) not null,
    `Nome` varchar(50),
    `UnidadedeMedida` varchar(03),
    `Peso`  decimal(07,2),
	`CodigoEAN`  varchar(13),
    `CodigoMoeda`  varchar(03),
    `PrecoCompra`  decimal(11,2),
    `ValorVenda`  decimal(11,2),
    primary key(`Codigo`)
     );
     
