DROP TABLE IF EXISTS Matricula;
DROP TABLE IF EXISTS Pagamento;
DROP TABLE IF EXISTS Modalidade;
DROP TABLE IF EXISTS FichaTreino;
DROP TABLE IF EXISTS AvaliacaoFisica;
DROP TABLE IF EXISTS Aluno;
DROP TABLE IF EXISTS Frequencia ;
DROP TABLE IF EXISTS Antopometria;
DROP TABLE IF EXISTS DobraCultanea;
DROP TABLE IF EXISTS Diametro;
DROP TABLE IF EXISTS Circuferencia;
DROP TABLE IF EXISTS Funcao;

CREATE TABLE Modalidade (
id INT  NOT NULL PRIMARY KEY,
descricao VARCHAR(50) NOT NULL,
valor REAl NOT NULL);

CREATE TABLE Pagamento (
id INT  NOT NULL PRIMARY KEY,
id_matricula INT NOT NULL,
valor DOUBLE NOT NULL,
dataPagamento DATE,
formaPagamento VARCHAR(50),
FOREIGN KEY(id_matricula) REFERENCES Matricula(id));

CREATE TABLE Antopometria (
id INT  NOT NULL PRIMARY KEY,
antopometriaPescoco REAl,
antopometriaToraxica REAl,
antopometriaCintura REAl,
antopometriaQuadril REAl,
antopometriaBracoRelaxado REAl,
antopometriaContraido REAl,
antopometriaAnteBraco REAl,
antopometriaCoxaSuperior REAl,
antopometriaCoxaMedia REAl,
antopometriaCoxaInferior REAl,
antopometriaPerna REAl);

CREATE TABLE DobraCultanea (
id INT  NOT NULL PRIMARY KEY,
dobraCultaneaSubEscapular REAl,
dobraCultaneaTriceps REAl,
dobraCultaneaBiceps REAl,
dobraCultaneaPeitoral REAl,
dobraCultaneaAxilarMediaObliqua REAl,
dobraCultaneaAxilarMediaVertical REAl,
dobraCultaneaAbdominalVertical REAl,
dobraCultaneaAbdominalHorizontal REAl,
dobraCultaneaSupraIliacaObliqua REAl,
dobraCultaneaSupraIliacaVertical REAl,
dobraCultaneaSupraEspinhal REAl,
dobraCultaneaCoxa REAl );

CREATE TABLE Diametro (
id INT  NOT NULL PRIMARY KEY,
diametroRadioUlnar REAl,
diametroUmeral REAl,
diametroBiacromial REAl,
diametroToracicoTransversal REAl,
diametroToracicoAnterior REAl,
diametroToracicoPosterior REAl,
diametroBicristal REAl,
diametroBitroCanteriano REAl,
diametroFemular REAl,
diametroMaleonar REAl);

CREATE TABLE Circuferencia (
id INT  NOT NULL PRIMARY KEY,
circuferenciaGlutea REAl,
circuferenciaPanturrilha REAl,
circuferenciaMaleolar REAl,
circuferenciaTroncoIM REAl,
circuferenciaTroncoEM REAl);

CREATE TABLE AvaliacaoFisica (
id INT  NOT NULL PRIMARY KEY,
id_aluno NULL,
avaliador VARCHAR(50),
data DATE,
frequenciaCardiaca  INT,
pesoAluno REAl,
altura REAl,
abdominal int,
flexaoBracos int,
id_antopometria INT NOT NULL,
id_dobracultanea INT NOT NULL,
id_diametro INT NOT NULL,
id_circuferencia INT NOT NULL,
FOREIGN KEY(id_aluno) REFERENCES Aluno(id),
FOREIGN KEY(id_antopometria) REFERENCES Antopometria(id),
FOREIGN KEY(id_dobracultanea) REFERENCES DobraCultanea(id),
FOREIGN KEY(id_diametro) REFERENCES Diametro(id),
FOREIGN KEY(id_circuferencia) REFERENCES Circuferencia(id));

CREATE TABLE Frequencia  (
id INT  NOT NULL PRIMARY KEY,
id_aluno INT NULL,
dataEntrada DATE NOT NULL,
dataSaida DATE NOT NULL,
FOREIGN KEY(id_aluno) REFERENCES Aluno(id));

CREATE TABLE Aluno (
id INT  NOT NULL PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
endereco VARCHAR(50) NOT NULL,
bairro VARCHAR(50) NOT NULL,
cep VARCHAR(50) NOT NULL,
cidade VARCHAR(50) NOT NULL,
estado VARCHAR(50) NOT NULL,
fone VARCHAR(50) NOT NULL,
celular VARCHAR(50) NOT NULL,
sexo CHAR(1) NOT NULL,
cpf VARCHAR(45) NOT NULL,
nascimento DATE NOT NULL,
email VARCHAR(50) NOT NULL,
estadoCivil VARCHAR(45) NOT NULL,
profissao VARCHAR(50) NOT NULL,
empresa VARCHAR(50) NOT NULL,
objetivo VARCHAR(50),
debito DOUBLE NOT NULL,
matriculado BOOLEAN NOT NULL);

CREATE TABLE Funcao (
id INT  NOT NULL PRIMARY KEY,
descricao VARCHAR(50) NOT NULL);

CREATE TABLE Funcionario (
id INT  NOT NULL PRIMARY KEY,
id_funcao INT NOT NULL,
nome VARCHAR(50) NOT NULL,
endereco VARCHAR(50) NOT NULL,
bairro VARCHAR(50) NOT NULL,
cep VARCHAR(50) NOT NULL,
cidade VARCHAR(50) NOT NULL,
estado VARCHAR(50) NOT NULL,
fone VARCHAR(50) NOT NULL,
celular VARCHAR(50) NOT NULL,
sexo CHAR(1) NOT NULL,
cpf VARCHAR(45) NOT NULL,
nascimento DATE NOT NULL,
email VARCHAR(50) NOT NULL,
estadoCivil VARCHAR(45) NOT NULL,
dataAdmissao Date,
salario DOUBLE,
dataDemissao Date,
usuario VARCHAR(50)  NOT NULL,
senha VARCHAR(50) NOT NULL, 
FOREIGN KEY(id_funcao) REFERENCES Funcao(id)
);


CREATE TABLE FichaTreino (
id INT  NOT NULL PRIMARY KEY,
-- cardinalidade 0
id_aluno NULL,
nome VARCHAR (50) NOT NULL,
data DATE NOT NULL,
professor VARCHAR (50),
treinoA VARCHAR(50),
diaA VARCHAR(50),
treinoB VARCHAR(50),
diaB VARCHAR(50),
treinoC VARCHAR(50),
diaC VARCHAR(50),
treinoD VARCHAR(50),
diaD VARCHAR(50),
treinoE VARCHAR(50),
diaE VARCHAR(50),
treinoF VARCHAR(50),
diaF VARCHAR(50)
);



CREATE TABLE Matricula (
id INT  NOT NULL PRIMARY KEY,
-- cardinalidade 0
id_aluno INT NULL,
id_modalidade INT NOT NULL,
dataVigencia DATE NOT NULL,
plano VARCHAR (50) NOT NULL,
dataVencimento DATE NOT NULL,
desconto DOUBLE NOT NULL,
valorFinal DOUBLE NOT NULL,
situacao  VARCHAR(50) NOT NULL,
dataFim DATE NOT NULL,
FOREIGN KEY(id_aluno) REFERENCES Aluno(id),
FOREIGN KEY(id_modalidade) REFERENCES Modalidade(id));










-- DROP TABLE Matricula;
-- DROP TABLE  Pagamento;
-- DROP TABLE Modalidade;
-- DROP TABLE FichaTreino;
-- DROP TABLE AvaliacaoFisica;
-- DROP TABLE Aluno;
-- DROP TABLE Frequencia ;
-- DROP TABLE  Antopometria;
-- DROP TABLE  DobraCultanea;
-- DROP TABLE  Diametro;
-- DROP TABLE Circuferencia;
-- DROP TABLE Funcao;
-- DROP TABLE Funcionario;

-- SELECT Vaga.descricao, Condutor.nome, Veiculo.descricao, tabela_de_preco.descricao as preco
-- FROM Locacao
-- INNER JOIN Vaga on Locacao.id_vaga = Vaga.id
-- INNER JOIN Condutor on Locacao.id_cliente = Condutor.id
-- INNER JOIN tabela_de_preco on Locacao.id_tabela_preco = tabela_de_preco.id
-- INNER JOIN Veiculo on Locacao.id_veiculo = Veiculo.id
