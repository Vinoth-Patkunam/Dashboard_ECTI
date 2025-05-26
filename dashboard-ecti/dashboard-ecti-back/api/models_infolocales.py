# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class Cv(models.Model):

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    modifpar = models.IntegerField(db_column='modifPar')  # Field name made lowercase.

    dateinser = models.DateTimeField(db_column='dateInser', blank=True, null=True)  # Field name made lowercase.

    datemodif = models.DateTimeField(db_column='dateModif', blank=True, null=True)  # Field name made lowercase.

    typedoc = models.CharField(db_column='typeDoc', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    nomfichier = models.CharField(db_column='nomFichier', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    nbtelecharge = models.IntegerField(db_column='nbTelecharge', blank=True, null=True)  # Field name made lowercase.

    langue = models.IntegerField(blank=True, null=True)



    class Meta:
        app_label = 'infolocales'

        managed = False

        db_table = 'cv'





class Cvnew(models.Model):

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    langue = models.IntegerField(blank=True, null=True)

    dateinser = models.DateTimeField(db_column='dateInser', blank=True, null=True)  # Field name made lowercase.

    typedoc = models.CharField(db_column='typeDoc', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nomfichier = models.CharField(db_column='nomFichier', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nouvelleadhesion = models.IntegerField(db_column='NouvelleAdhesion', blank=True, null=True)  # Field name made lowercase.

    validation = models.IntegerField(blank=True, null=True)

    commentairerefus = models.CharField(db_column='commentaireRefus', max_length=255, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'infolocales'

        managed = False

        db_table = 'cvnew'





class Langues(models.Model):

    nom = models.CharField(max_length=50, blank=True, null=True)

    suffixe = models.CharField(max_length=50, blank=True, null=True)

    repertoire = models.CharField(max_length=50, blank=True, null=True)



    class Meta:
        app_label = 'infolocales'

        managed = False

        db_table = 'langues'





class Parametres(models.Model):

    nom = models.CharField(max_length=50, blank=True, null=True)

    valeur = models.CharField(max_length=50, blank=True, null=True)



    class Meta:
        app_label = 'infolocales'

        managed = False

        db_table = 'parametres'





class Telechargement(models.Model):

    numexp = models.IntegerField(db_column='NumExp', primary_key=True)  # Field name made lowercase.

    lastdate = models.DateTimeField(db_column='lastDate', blank=True, null=True)  # Field name made lowercase.

    nbcvjour = models.IntegerField(db_column='nbCvJour', blank=True, null=True)  # Field name made lowercase.

    nbcvtotal = models.IntegerField(db_column='nbCvTotal', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'infolocales'

        managed = False

        db_table = 'telechargement'



