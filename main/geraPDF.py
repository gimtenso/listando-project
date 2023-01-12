import pymongo
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import cm


def buscar_questoes(assunto, quantidade):
    client = pymongo.MongoClient(
        "mongodb://user:user@ac-zvbacnb-shard-00-00.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-01.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('EngSoft-Projeto')
    db_questoes = db.questões

    lista_questoes = db_questoes.aggregate([{
        "$match": {
            "assunto": assunto
        }
    }, {
        "$sample": {
            "size": quantidade
        }
    }])

    return lista_questoes


def get_temas():
    client = pymongo.MongoClient(
        "mongodb://user:user@ac-zvbacnb-shard-00-00.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-01.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('EngSoft-Projeto')
    db_questoes = db.questões

    temas = {}

    lista_questoes = db_questoes.find()
    for q in lista_questoes:
        if q['assunto'] not in temas.keys():
            temas[q['assunto']] = 1
        else:
            temas[q['assunto']] += 1

    ret = [(k, v) for k, v in temas.items()]

    return sorted(ret)


def gerarPDF(data, buffer):
    pdf = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    itens = []

    itens.append(Paragraph('LISTA DE EXERCÍCIOS PERSONALIZADA<br/><br/>'))

    gabarito = []
    q_no = 1
    for assunto, quantidade in data.items():
        if quantidade == 0:
            continue
        questoes = buscar_questoes(assunto, quantidade)
        itens.append(Paragraph(assunto))
        gabarito.append(Paragraph(assunto))

        for objeto in questoes:
            questao = objeto["questão"].lstrip("\n0123456789.- ")
            itens.append(
                Paragraph(f'\nQUESTÃO {q_no}\n\n{questao}\n'.replace("\n", "<br />")))
            gabarito.append(
                Paragraph(f"\n{q_no}-{objeto['resposta']}".replace("\n", "<br />")))
            q_no += 1

        itens.append(Paragraph("_"*40 + "<br />"*2))
        gabarito.append(Paragraph("_"*40 + "<br />"*2))

    itens.append(Paragraph('GABARITO<br /><br />'))

    itens += gabarito

    pdf.build(itens)


if __name__ == "__main__":
    client = pymongo.MongoClient(
        "mongodb://user:user@ac-zvbacnb-shard-00-00.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-01.n4s7ayo.mongodb.net:27017,ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('EngSoft-Projeto')
    db_questoes = db.questões
    print("a")
