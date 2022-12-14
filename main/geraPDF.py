import PyPDF2
import pymongo
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


def buscar_questoes(assunto):
    client = pymongo.MongoClient(
        "mongodb://user:user@ac-zvbacnb-shard-00-00.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-01.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('EngSoft-Projeto')
    db_questoes = db.questões

    lista_questoes = db_questoes.find({"assunto": assunto}).limit(3)
    return lista_questoes


def gerarPDF(assunto):
    questoes = buscar_questoes(assunto)

    pdf = SimpleDocTemplate("lista_personalizada.pdf", pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    itens = []

    itens.append(Paragraph('LISTA DE EXERCÍCIOS PERSONALIZADA'))

    for objeto in questoes:
        itens.append(Paragraph(objeto["questão"].replace("\n", "<br />")))

    itens.append(Paragraph('GABARITO'))

    for objeto in questoes:
        itens.append(Paragraph(objeto["resposta"]))

    pdf.build(itens)
