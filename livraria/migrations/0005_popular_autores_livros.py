from django.db import migrations


AUTORES = [
    ("Machado de Assis", "contato@machadodeassis.com.br"),
    ("Clarice Lispector", "contato@claricelispector.com.br"),
    ("George Orwell", "contato@georgeorwell.co.uk"),
    ("J.R.R. Tolkien", "contato@jrrtolkien.co.uk"),
    ("Stephen King", "contato@stephenking.com"),
    ("Yuval Noah Harari", "contato@yuvalnoahharari.com"),
    ("Paulo Coelho", "contato@paulocoelho.com.br"),
    ("Monteiro Lobato", "contato@monteirolobato.com.br"),
]

LIVROS = [
    (
        "Dom Casmurro",
        "9788535910663",
        15,
        "39.90",
        "Romance",
        "Companhia das Letras",
    ),
    (
        "A Hora da Estrela",
        "9788532530808",
        10,
        "34.50",
        "Romance",
        "Editora Rocco",
    ),
    (
        "1984",
        "9788535914849",
        20,
        "44.90",
        "Ficção Científica",
        "Companhia das Letras",
    ),
    (
        "O Hobbit",
        "9788595084742",
        12,
        "54.90",
        "Fantasia",
        "Editora Rocco",
    ),
    (
        "It: A Coisa",
        "9788560088699",
        8,
        "69.90",
        "Terror",
        "Editora Record",
    ),
    (
        "Sapiens: Uma Breve História da Humanidade",
        "9788525432186",
        18,
        "59.90",
        "História",
        "Editora Record",
    ),
    (
        "O Alquimista",
        "9788576653836",
        25,
        "42.00",
        "Autoajuda",
        "Editora Sextante",
    ),
    (
        "Sítio do Picapau Amarelo",
        "9788525061118",
        14,
        "29.90",
        "Infantil",
        "Editora Globo",
    ),
]


def popular_dados(apps, schema_editor):
    Autor = apps.get_model("livraria", "Autor")
    Categoria = apps.get_model("livraria", "Categoria")
    Editora = apps.get_model("livraria", "Editora")
    Livro = apps.get_model("livraria", "Livro")

    for nome, email in AUTORES:
        Autor.objects.get_or_create(nome=nome, defaults={"email": email})

    for titulo, isbn, quantidade, preco, categoria_nome, editora_nome in LIVROS:
        categoria, _ = Categoria.objects.get_or_create(descricao=categoria_nome)
        editora, _ = Editora.objects.get_or_create(nome=editora_nome)
        Livro.objects.get_or_create(
            titulo=titulo,
            defaults={
                "isbn": isbn,
                "quantidade": quantidade,
                "preco": preco,
                "categoria": categoria,
                "editora": editora,
            },
        )


def remover_dados(apps, schema_editor):
    Autor = apps.get_model("livraria", "Autor")
    Livro = apps.get_model("livraria", "Livro")

    Livro.objects.filter(titulo__in=[titulo for titulo, *_ in LIVROS]).delete()
    Autor.objects.filter(nome__in=[nome for nome, _ in AUTORES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("livraria", "0004_autor_livro"),
    ]

    operations = [
        migrations.RunPython(popular_dados, remover_dados),
    ]
