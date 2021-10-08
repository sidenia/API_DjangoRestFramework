from django.db import models

class TblAutores(models.Model):
    id_autor = models.SmallIntegerField(db_column='ID_autor', primary_key=True)  # Field name made lowercase.
    nome_autor = models.CharField(max_length=50, blank=True, null=True)
    sobrenome_autor = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.nome_autor

    class Meta:
        managed = True
        db_table = 'tbl_autores'


class TblEditoras(models.Model):
    id_editora = models.SmallAutoField(db_column='ID_editora', primary_key=True)  # Field name made lowercase.
    nome_editora = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_editora

    class Meta:
        managed = True
        db_table = 'tbl_editoras'


class TblLivro(models.Model):
    id_livro = models.SmallAutoField(db_column='ID_livro', primary_key=True)  # Field name made lowercase.
    nome_livro = models.CharField(max_length=50)
    isbn = models.IntegerField(db_column='ISBN')  # Field name made lowercase.
    data_pub = models.DateField()
    preco_livro = models.DecimalField(max_digits=10, decimal_places=0)
    id_autor = models.ForeignKey(TblAutores, models.DO_NOTHING, db_column='ID_autor')  # Field name made lowercase.
    id_editora = models.ForeignKey(TblEditoras, models.DO_NOTHING, db_column='ID_editora')  # Field name made lowercase.

    def __str__(self):
        return self.nome_livro

    class Meta:
        managed = True
        db_table = 'tbl_livro'


class TblImagefield(models.Model): 
    title = models.CharField(max_length = 200) 
    img = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "imageupload"