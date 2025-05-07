CREATE TABLE LinhaMetro (
    id_linhaMetro NUMBER PRIMARY KEY,
    nome VARCHAR2(50) NOT NULL,
    extensao NUMBER NOT NULL,
    numero NUMBER,
    descricao VARCHAR2(200),
    tipo VARCHAR2(30),
    responsavel VARCHAR2(100)
);

CREATE TABLE Estacao (
    id_estacao NUMBER PRIMARY KEY,
    nome VARCHAR2(30) NOT NULL,
    localizacao VARCHAR2(50) NOT NULL,
    passageirosSimulados NUMBER NOT NULL,
    id_linhaMetro NUMBER NOT NULL,
    CONSTRAINT fk_estacao FOREIGN KEY (id_linhaMetro) REFERENCES LinhaMetro (id_linhaMetro),
    CONSTRAINT chk_pax_simulados CHECK (passageirosSimulados >= 0),
    CONSTRAINT uq_nome_estacao UNIQUE (nome)
);

CREATE TABLE Usuario_Challenge (
    id_usuario NUMBER PRIMARY KEY,
    nome VARCHAR2(30) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    senha VARCHAR2(255) NOT NULL
);
