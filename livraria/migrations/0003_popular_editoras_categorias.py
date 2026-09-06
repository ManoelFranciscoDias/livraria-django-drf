from django.db import migrations


def popular_dados(apps, schema_editor):
    Categoria = apps.get_model("livraria", "Categoria")
    Editora = apps.get_model("livraria", "Editora")

    categorias = [
        "Romance",
        "Ficção Científica",
        "Fantasia",
        "Terror",
        "Biografia",
        "História",
        "Autoajuda",
        "Tecnologia",
        "Infantil",
        "Poesia",
    ]
    for descricao in categorias:
        Categoria.objects.get_or_create(descricao=descricao)

    editoras = [
        ("Companhia das Letras", "https://www.companhiadasletras.com.br"),
        ("Editora Rocco", "https://www.rocco.com.br"),
        ("Editora Record", "https://www.record.com.br"),
        ("Editora Globo", "https://www.editoraglobo.com.br"),
        ("Editora Sextante", "https://www.sextante.com.br"),
        ("Editora Intrínseca", "https://www.intrinseca.com.br"),
        ("Editora Aleph", "https://www.editoraaleph.com.br"),
        ("Editora Moderna", "https://www.moderna.com.br"),
        ("Editora Ática", "https://www.atica.com.br"),
        ("Editora Saraiva", "https://www.editorasaraiva.com.br"),
    ]
    for nome, site in editoras:
        Editora.objects.get_or_create(nome=nome, defaults={"site": site})


def remover_dados(apps, schema_editor):
    Categoria = apps.get_model("livraria", "Categoria")
    Editora = apps.get_model("livraria", "Editora")

    categorias = [
        "Romance",
        "Ficção Científica",
        "Fantasia",
        "Terror",
        "Biografia",
        "História",
        "Autoajuda",
        "Tecnologia",
        "Infantil",
        "Poesia",
    ]
    Categoria.objects.filter(descricao__in=categorias).delete()

    editoras = [
        "Companhia das Letras",
        "Editora Rocco",
        "Editora Record",
        "Editora Globo",
        "Editora Sextante",
        "Editora Intrínseca",
        "Editora Aleph",
        "Editora Moderna",
        "Editora Ática",
        "Editora Saraiva",
    ]
    Editora.objects.filter(nome__in=editoras).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("livraria", "0002_editora"),
    ]

    operations = [
        migrations.RunPython(popular_dados, remover_dados),
    ]
