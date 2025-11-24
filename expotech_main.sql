CREATE DATABASE JaguarTech;

USE JaguarTech;

CREATE TABLE tbl_clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    numero_cliente VARCHAR(17) UNIQUE NOT NULL,
    logradouro_cliente VARCHAR(100),
    numero_casa INT,
    bairro VARCHAR(100),
    CEP VARCHAR(9)
);

CREATE TABLE tbl_aparelhos (
    id_aparelho INT AUTO_INCREMENT PRIMARY KEY,
    marca_aparelho VARCHAR(100) NOT NULL,
    modelo_aparelho VARCHAR(100) NOT NULL,
    id_cliente INT NOT NULL,
    CONSTRAINT FOREIGN KEY (id_cliente) REFERENCES tbl_clientes(id_cliente)
);

CREATE TABLE tbl_servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    tipo_servico VARCHAR(100) NOT NULL,
    valor_servico DECIMAL(10,2) NOT NULL,
    descricao_problema VARCHAR(255),
    status_servico VARCHAR(20),
    tempo_garantia DATE,
    dt_entrada DATE,
    previsao_entrega DATE,
    id_aparelho INT NOT NULL,
    id_cliente INT NOT NULL,
    CONSTRAINT FOREIGN KEY (id_aparelho) REFERENCES tbl_aparelhos(id_aparelho),
    CONSTRAINT FOREIGN KEY (id_cliente) REFERENCES tbl_clientes(id_cliente)
);

CREATE TABLE tbl_estoque (
    id_peca INT AUTO_INCREMENT PRIMARY KEY,
    nome_peca VARCHAR(150) NOT NULL,
    descricao_peca VARCHAR(255),
    quantidade_estoque INT DEFAULT 0,
    custo_unitario DECIMAL(10,2)
);


SELECT * FROM tbl_aparelhos;
SELECT * FROM tbl_clientes;
SELECT * FROM tbl_estoque;
SELECT * FROM tbl_servicos;
