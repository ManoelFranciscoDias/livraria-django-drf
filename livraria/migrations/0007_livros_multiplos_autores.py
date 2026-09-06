# Generated manually to popular livros com mais de um autor

from django.db import migrations


LIVROS = [
    (
        "Grandes Contos Brasileiros",
        "9788500000001",
        20,
        "49.90",
        "Romance",
        "Companhia das Letras",
        ["Machado de Assis", "Clarice Lispector", "Monteiro Lobato"],
    ),
    (
        "Antologia da Ficção Especulativa",
        "9788500000002",
        16,
        "64.90",
        "Ficção Científica",
        "Editora Rocco",
        ["George Orwell", "J.R.R. Tolkien", "Stephen King"],
    ),
    (
        "Sabedoria e Ação",
        "9788500000003",
        22,
        "39.90",
        "Autoajuda",
        "Editora Sextante",
        ["Paulo Coelho", "Yuval Noah Harari"],
    ),
]


def popular_dados(apps, schema_editor):
    Autor = apps.get_model("livraria", "Autor")
    Categoria = apps.get_model("livraria", "Categoria")
    Editora = apps.get_model("livraria", "Editora")
    Livro = apps.get_model("livraria", "Livro")

    for titulo, isbn, quantidade, preco, categoria_nome, editora_nome, autores_nomes in LIVROS:
        categoria, _ = Categoria.objects.get_or_create(descricao=categoria_nome)
        editora, _ = Editora.objects.get_or_create(nome=editora_nome)
        livro, _ = Livro.objects.get_or_create(
            titulo=titulo,
            defaults={
                "isbn": isbn,
                "quantidade": quantidade,
                "preco": preco,
                "categoria": categoria,
                "editora": editora,
            },
        )
        autores = Autor.objects.filter(nome__in=autores_nomes)
        livro.autores.set(autores)


def remover_dados(apps, schema_editor):
    Livro = apps.get_model("livraria", "Livro")
    Livro.objects.filter(titulo__in=[titulo for titulo, *_ in LIVROS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("livraria", "0006_livro_autores"),
    ]

    operations = [
        migrations.RunPython(popular_dados, remover_dados),
    ]
