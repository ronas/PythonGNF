#aqui esta meu banco  de dados do programa cadastrodeprodutos.py  
create database `LojaDB`

 create table `LojaDB`.`Produtos`(
    `Codigo`varchar(10) NOT NULL,
    `Nome`  varchar(50) ,
    `UnidadeMedida` varchar(3) ,
    `Peso` decimal(7,2) ,
    `CodigoEAN` varchar(13) ,
    `CodigoMoeda` varchar(3) ,
    `PrecoCompra` decimal(11,2) ,
    `ValorVenda` decimal(11,2) ,
    PRIMARY KEY (`Codigo`)
    )