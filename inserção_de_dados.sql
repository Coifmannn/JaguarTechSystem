USE JaguarTech;

INSERT INTO tbl_clientes (nome_cliente, numero_cliente, logradouro_cliente, numero_casa, bairro, CEP) VALUES
('João da Silva', '(11) 99999-1001', 'Rua das Flores', 123, 'Centro', '01001-000'),
('Maria Oliveira', '(11) 98888-2002', 'Av. Paulista', 1500, 'Bela Vista', '01311-000'),
('Pedro Santos', '(21) 97777-3003', 'Rua do Ouvidor', 45, 'Centro', '20040-000'),
('Ana Costa', '(31) 96666-4004', 'Av. Afonso Pena', 300, 'Savassi', '30130-000'),
('Lucas Pereira', '(41) 95555-5005', 'Rua XV de Novembro', 10, 'Batel', '80020-000');

INSERT INTO tbl_estoque (nome_peca, descricao_peca, quantidade_estoque, custo_unitario) VALUES
('Tela iPhone 11', 'Display LCD completo original', 10, 250.00),
('Bateria Samsung S20', 'Bateria Li-Ion 4000mAh', 15, 120.50),
('SSD 480GB', 'SSD Kingston A400 SATA', 8, 180.00),
('Memória RAM 8GB', 'DDR4 2666MHz Notebook', 20, 150.00),
('Fonte ATX 500W', 'Fonte Real com selo 80 Plus', 5, 200.00);

INSERT INTO tbl_aparelhos (marca_aparelho, modelo_aparelho, id_cliente) VALUES
('Apple', 'iPhone 11', 1),         
('Samsung', 'Galaxy S20 FE', 2),   
('Dell', 'Inspiron 15', 3),      
('Xiaomi', 'Redmi Note 10', 4),     
('Lenovo', 'IdeaPad 3', 5);      

INSERT INTO tbl_servicos (tipo_servico, valor_servico, descricao_problema, status_servico, tempo_garantia, dt_entrada, previsao_entrega, id_aparelho, id_cliente) VALUES
('Troca de Tela', 450.00, 'Vidro quebrado após queda', 'Concluído', '2026-02-20', '2025-11-18', '2025-11-20', 1, 1),
('Troca de Bateria', 280.00, 'Bateria viciada, desliga com 20%', 'Em Andamento', NULL, '2025-11-20', '2025-11-22', 2, 2),
('Formatação', 120.00, 'Windows lento e travando', 'Pendente', NULL, '2025-11-21', '2025-11-22', 3, 3),
('Reparo Conector', 150.00, 'Não carrega', 'Aguardando Peça', NULL, '2025-11-19', '2025-11-25', 4, 4),
('Upgrade SSD', 300.00, 'Instalação de SSD e clonagem', 'Concluído', '2026-05-20', '2025-11-15', '2025-11-16', 5, 5);

SELECT 
    c.nome_cliente, 
    a.modelo_aparelho, 
    s.tipo_servico, 
    s.status_servico
FROM tbl_servicos s
INNER JOIN tbl_clientes c ON s.id_cliente = c.id_cliente
INNER JOIN tbl_aparelhos a ON s.id_aparelho = a.id_aparelho;