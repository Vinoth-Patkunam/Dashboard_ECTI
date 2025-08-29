from django.db import models

class Cv(models.Model):
    numexp       = models.IntegerField(db_column='NumExp')
    modifpar     = models.IntegerField(db_column='modifPar')
    dateinser    = models.DateTimeField(db_column='dateInser', blank=True, null=True)
    datemodif    = models.DateTimeField(db_column='dateModif', blank=True, null=True)
    typedoc      = models.CharField(db_column='typeDoc', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    nomfichier   = models.CharField(db_column='nomFichier', max_length=50, db_collation='utf8_general_ci', primary_key=True)  # PK technique
    nbtelecharge = models.IntegerField(db_column='nbTelecharge', blank=True, null=True)
    langue       = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'infolocales'
        managed   = False
        db_table  = 'cv'


class Cvnew(models.Model):
    numexp            = models.IntegerField(db_column='NumExp')
    langue            = models.IntegerField(blank=True, null=True)
    dateinser         = models.DateTimeField(db_column='dateInser', blank=True, null=True)
    typedoc           = models.CharField(db_column='typeDoc', max_length=50, blank=True, null=True)
    nomfichier        = models.CharField(db_column='nomFichier', max_length=50, primary_key=True)  # PK technique
    nouvelleadhesion  = models.IntegerField(db_column='NouvelleAdhesion', blank=True, null=True)
    validation        = models.IntegerField(blank=True, null=True)
    commentairerefus  = models.CharField(db_column='commentaireRefus', max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'infolocales'
        managed   = False
        db_table  = 'cvnew'


class Langues(models.Model):
    nom        = models.CharField(max_length=50, blank=True, null=True)
    suffixe    = models.CharField(max_length=50, primary_key=True)  # PK technique (souvent 'fr', 'en', ...)
    repertoire = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'infolocales'
        managed   = False
        db_table  = 'langues'


class Parametres(models.Model):
    nom    = models.CharField(max_length=50, primary_key=True)  # PK technique
    valeur = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'infolocales'
        managed   = False
        db_table  = 'parametres'


class Telechargement(models.Model):
    numexp     = models.IntegerField(db_column='NumExp', primary_key=True)
    lastdate   = models.DateTimeField(db_column='lastDate', blank=True, null=True)
    nbcvjour   = models.IntegerField(db_column='nbCvJour', blank=True, null=True)
    nbcvtotal  = models.IntegerField(db_column='nbCvTotal', blank=True, null=True)

    class Meta:
        app_label = 'infolocales'
        managed   = False
        db_table  = 'telechargement'
