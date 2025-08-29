# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class Filieres(models.Model):

    filire = models.CharField(db_column='Filire', primary_key=True, max_length=3)  # Field name made lowercase.

    libell_filire = models.CharField(db_column='Libell_Filire', max_length=60, blank=True, null=True)  # Field name made lowercase.

    validfil = models.CharField(db_column='Validfil', max_length=1, blank=True, null=True)  # Field name made lowercase.

    oprationnel = models.DateTimeField(db_column='Oprationnel', blank=True, null=True)  # Field name made lowercase.

    clotur = models.DateTimeField(db_column='Clotur', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'filieres'





class Fonction(models.Model):

    code_fonction = models.CharField(db_column='Code_Fonction', primary_key=True, max_length=2)  # Field name made lowercase.

    fonction = models.CharField(db_column='Fonction', max_length=50, blank=True, null=True)  # Field name made lowercase.

    validfon = models.CharField(db_column='Validfon', max_length=1, blank=True, null=True)  # Field name made lowercase.

    operationnel = models.DateTimeField(db_column='Operationnel', blank=True, null=True)  # Field name made lowercase.

    clotur = models.DateTimeField(db_column='Clotur', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'fonction'





class Naf24(models.Model):

    cod_div   = models.CharField(db_column='Cod_div',   max_length=2)

    naf_group = models.CharField(db_column='NAF_Group', max_length=2)

    libel4    = models.CharField(db_column='Libel4', max_length=100, blank=True, null=True)

    cod_div_pk = models.CharField(db_column='Cod_div', max_length=2, primary_key=True, editable=False)


    class Meta:
        app_label = 'tstatic'
        managed = False
        db_table = 'naf_24'
        unique_together = (('cod_div', 'naf_group'),)




class Naf25(models.Model):

    cod_div   = models.CharField(db_column='Cod_div',   max_length=2)

    naf_group = models.CharField(db_column='NAF_Group', max_length=2)

    naf_naf   = models.CharField(db_column='NAF_NAF',   max_length=1)

    libel5    = models.CharField(db_column='Libel5', max_length=130, blank=True, null=True)

    codnaf    = models.CharField(db_column='CodNAF', max_length=5, blank=True, null=True, primary_key=True)


    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'naf_25'





class NafCode1(models.Model):

    cod_sect = models.CharField(db_column='Cod_Sect', primary_key=True, max_length=1)  # Field name made lowercase.

    intitulsect = models.CharField(db_column='IntitulSect', max_length=255, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'naf_code1'





class NafCode2(models.Model):

    code2 = models.CharField(db_column='Code2', primary_key=True, max_length=2)  # Field name made lowercase.

    intitul2 = models.CharField(db_column='Intitul2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    cod_sect = models.CharField(db_column='Cod_Sect', max_length=1, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'naf_code2'





class NafRev2(models.Model):

    code = models.CharField(db_column='Code', primary_key=True, max_length=6)  # Field name made lowercase.

    section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

    intitul = models.CharField(db_column='Intitul', max_length=255, blank=True, null=True)  # Field name made lowercase.

    niveau = models.FloatField(db_column='Niveau', blank=True, null=True)  # Field name made lowercase.

    granddomaine = models.CharField(db_column='GrandDomaine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    commentaire = models.FloatField(db_column='Commentaire', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'naf_rev2'





class TContact(models.Model):

    numpm       = models.IntegerField(db_column='NumPM')

    numcor      = models.IntegerField(db_column='NumCor')

    datecontact = models.DateTimeField(db_column='DateContact')

    rsum        = models.TextField(db_column='Rsum')

    numpm_pk = models.IntegerField(db_column='NumPM', primary_key=True, editable=False)


    class Meta:

        app_label = 'tstatic'

        managed = False

        db_table = 't_contact'

        unique_together = (('numpm', 'numcor', 'datecontact'),)




class TServicescourriels(models.Model):

    codeserv  = models.CharField(db_column='CodeServ', max_length=4)

    exten     = models.CharField(db_column='Exten',    max_length=2)

    envoyeur  = models.CharField(db_column='Envoyeur', max_length=50, blank=True, null=True)

    stopenvoi = models.IntegerField(db_column='StopEnvoi', blank=True, null=True)

    codeserv_pk = models.CharField(db_column='CodeServ', max_length=4, primary_key=True, editable=False)

    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 't_servicescourriels'





class TcAdress(models.Model):

    val = models.CharField(db_column='Val', primary_key=True, max_length=1)  # Field name made lowercase.

    libvalidit = models.CharField(db_column='LibValidit', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_adress'





class TcBank(models.Model):

    codbank = models.CharField(db_column='CodBank', primary_key=True, max_length=4)  # Field name made lowercase.

    libelb = models.CharField(db_column='LibelB', max_length=30)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_bank'





class TcCatgorie(models.Model):

    catgorie = models.CharField(db_column='Catgorie', primary_key=True, max_length=3)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=100, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_catgorie'





class TcCodpostal(models.Model):

    cp    = models.CharField(db_column='Cp',    max_length=5)

    ville = models.CharField(db_column='Ville', max_length=35)

    cp_pk = models.CharField(db_column='Cp', max_length=5, primary_key=True, editable=False)

    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_codpostal'

        unique_together = (('cp', 'ville'),)





class TcConnu(models.Model):

    codconnu = models.CharField(db_column='CodConnu', primary_key=True, max_length=2)  # Field name made lowercase.

    libel = models.CharField(db_column='Libel', max_length=25)  # Field name made lowercase.

    typ = models.CharField(max_length=1)



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_connu'





class TcCotis(models.Model):

    typecotis = models.CharField(db_column='TypeCotis', primary_key=True, max_length=2)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=35, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_cotis'





class TcDep(models.Model):

    codpay = models.CharField(db_column='CodPay', max_length=3)

    coddep = models.CharField(db_column='CodDep', max_length=2)

    nomdep = models.CharField(db_column='NomDep', max_length=50, blank=True, null=True)

    codreg = models.CharField(db_column='CodReg', max_length=2, blank=True, null=True)

    codpay_pk = models.CharField(db_column='CodPay', max_length=3, primary_key=True, editable=False)

    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_dep'
        
        unique_together = (('codpay', 'coddep'),)




class TcDure(models.Model):

    coddure = models.CharField(db_column='CodDure', primary_key=True, max_length=1)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_dure'





class TcInfor(models.Model):

    codinfor = models.CharField(db_column='CodInfor', primary_key=True, max_length=2)  # Field name made lowercase.

    libell = models.CharField(db_column='Libell', max_length=20, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_infor'





class TcNatvers(models.Model):

    natvers = models.CharField(db_column='NatVers', primary_key=True, max_length=50)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=120, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_natvers'





class TcPayeur(models.Model):

    codepayeur = models.CharField(db_column='CodePayeur', primary_key=True, max_length=1)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=80, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_payeur'





class TcPos(models.Model):

    position = models.CharField(db_column='Position', primary_key=True, max_length=1)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=70, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_pos'





class TcSuivi(models.Model):

    codsuivi = models.PositiveIntegerField(db_column='CodSuivi', primary_key=True)  # Field name made lowercase.

    libell = models.CharField(db_column='Libell', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_suivi'





class TcTranca(models.Model):

    tranca = models.CharField(db_column='TranCA', primary_key=True, max_length=2)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_tranca'





class TcTypserv(models.Model):

    codtypser = models.CharField(db_column='CodTypSer', primary_key=True, max_length=1)  # Field name made lowercase.

    libtypser = models.CharField(db_column='LibTypSer', max_length=60, blank=True, null=True)  # Field name made lowercase.

    abrev = models.CharField(db_column='Abrev', max_length=4, blank=True, null=True)  # Field name made lowercase.

    niveau = models.PositiveIntegerField(db_column='Niveau', blank=True, null=True)  # Field name made lowercase.

    rseau = models.CharField(db_column='Rseau', max_length=1, blank=True, null=True)  # Field name made lowercase.

    affgeo = models.IntegerField(db_column='AffGeo')  # Field name made lowercase.

    attachinf = models.IntegerField(db_column='AttachInf', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tstatic'

        managed = False

        db_table = 'tc_typserv'

