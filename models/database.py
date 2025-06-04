from flask_sqlalchemy import SQLAlchemy

# carregando o SQLAlchemy na váriavel DB
db = SQLAlchemy()

# criando o model (classe)
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
        # metodo construtor da classe
    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
    
class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    fabricante = db.Column(db.String(100))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    

        
    def __init__(self, nome, fabricante, preco, quantidade):
        self.nome = nome
        self.fabricante = fabricante
        self.preco = preco
        self.quantidade = quantidade