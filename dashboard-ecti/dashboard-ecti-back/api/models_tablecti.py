

from django.db import models





class Affectations(models.Model):

    pk = models.CompositePrimaryKey('CodeServA', 'ExtenA', 'Code3A', 'Depar', 'CodPos', 'DatOuvL')

    codeserva = models.CharField(db_column='CodeServA', max_length=4)  # Field name made lowercase.

    extena = models.CharField(db_column='ExtenA', max_length=2)  # Field name made lowercase.

    indicea = models.SmallIntegerField(db_column='IndiceA', blank=True, null=True)  # Field name made lowercase.

    code3a = models.CharField(db_column='Code3A', max_length=3)  # Field name made lowercase.

    depar = models.CharField(db_column='Depar', max_length=2)  # Field name made lowercase.

    codpos = models.CharField(db_column='CodPos', max_length=5)  # Field name made lowercase.

    datouvl = models.DateTimeField(db_column='DatOuvL')  # Field name made lowercase.

    datouvaff = models.DateTimeField(db_column='DatOuvAff')  # Field name made lowercase.

    datclotaff = models.DateTimeField(db_column='DatClotAff', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'affectations'

        unique_together = (('codeserva', 'extena', 'code3a', 'depar', 'codpos', 'datouvl'),)





class Depdel(models.Model):

    dep = models.CharField(db_column='Dep', max_length=2, blank=True, null=True)  # Field name made lowercase.

    com = models.CharField(db_column='Com', max_length=3, blank=True, null=True)  # Field name made lowercase.

    dl_reg = models.CharField(db_column='Dl_reg', max_length=5, blank=True, null=True)  # Field name made lowercase.

    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    statut = models.CharField(db_column='Statut', max_length=1, blank=True, null=True)  # Field name made lowercase.

    tri = models.CharField(db_column='Tri', max_length=1, blank=True, null=True)  # Field name made lowercase.

    nomdep = models.CharField(db_column='NomDep', max_length=25, blank=True, null=True)  # Field name made lowercase.

    opra = models.DateTimeField(db_column='Opra', blank=True, null=True)  # Field name made lowercase.

    cltur = models.DateTimeField(db_column='Cltur', blank=True, null=True)  # Field name made lowercase.

    reg = models.CharField(db_column='Reg', max_length=2, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'depdel'





class Entgeo(models.Model):

    pk = models.CompositePrimaryKey('Code3A', 'Depart', 'CodPos', 'DatOuvL')

    code3a = models.CharField(db_column='Code3A', max_length=3)  # Field name made lowercase.

    depart = models.CharField(db_column='Depart', max_length=2)  # Field name made lowercase.

    codpos = models.CharField(db_column='CodPos', max_length=5)  # Field name made lowercase.

    datouvl = models.DateTimeField(db_column='DatOuvL')  # Field name made lowercase.

    datferl = models.DateTimeField(db_column='DatFerL', blank=True, null=True)  # Field name made lowercase.

    rseau = models.CharField(db_column='Rseau', max_length=1, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'entgeo'

        unique_together = (('code3a', 'depart', 'codpos', 'datouvl'),)





class Groudel(models.Model):

    codedlg = models.CharField(db_column='Codedlg', primary_key=True, max_length=5)  # Field name made lowercase.

    dlgation = models.CharField(db_column='Dlgation', max_length=80, blank=True, null=True)  # Field name made lowercase.

    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.

    valideleg = models.CharField(db_column='Valideleg', max_length=1, blank=True, null=True)  # Field name made lowercase.

    oprationnel = models.DateTimeField(db_column='Oprationnel', blank=True, null=True)  # Field name made lowercase.

    clotur = models.DateTimeField(db_column='Clotur', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'groudel'





class Montantcotisationsannee(models.Model):

    annee = models.IntegerField(unique=True)

    montant = models.FloatField()



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'montantcotisationsannee'





class Naf25(models.Model):

    pk = models.CompositePrimaryKey('Cod_div', 'NAF_Group', 'NAF_NAF')

    cod_div = models.CharField(db_column='Cod_div', max_length=2)  # Field name made lowercase.

    naf_group = models.CharField(db_column='NAF_Group', max_length=2)  # Field name made lowercase.

    naf_naf = models.CharField(db_column='NAF_NAF', max_length=1)  # Field name made lowercase.

    libel5 = models.CharField(db_column='Libel5', max_length=130, blank=True, null=True)  # Field name made lowercase.

    codnaf = models.CharField(db_column='CodNAF', unique=True, max_length=5, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'naf_25'

        unique_together = (('cod_div', 'naf_group', 'naf_naf'),)





class Services(models.Model):

    pk = models.CompositePrimaryKey('CodeServ', 'Exten')

    codeserv = models.CharField(db_column='CodeServ', max_length=4)  # Field name made lowercase.

    exten = models.CharField(db_column='Exten', max_length=2)  # Field name made lowercase.

    indice = models.SmallIntegerField(db_column='Indice')  # Field name made lowercase.

    datouvsrv = models.DateTimeField(db_column='DatOuvSrv', blank=True, null=True)  # Field name made lowercase.

    datclotsrv = models.DateTimeField(db_column='DatClotSrv', blank=True, null=True)  # Field name made lowercase.

    libelserv = models.CharField(db_column='LibelServ', max_length=150, blank=True, null=True)  # Field name made lowercase.

    titreserv = models.CharField(db_column='titreServ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    typserv = models.CharField(db_column='TypServ', max_length=1, blank=True, null=True)  # Field name made lowercase.

    courrier = models.IntegerField(db_column='Courrier', blank=True, null=True)  # Field name made lowercase.

    domsiege = models.IntegerField(db_column='DomSiege', blank=True, null=True)  # Field name made lowercase.

    adr1 = models.CharField(max_length=100, blank=True, null=True)

    adr2 = models.CharField(max_length=100, blank=True, null=True)

    codpostal = models.CharField(db_column='CodPostal', max_length=10, blank=True, null=True)  # Field name made lowercase.

    ville = models.CharField(db_column='Ville', max_length=30, blank=True, null=True)  # Field name made lowercase.

    codepays = models.CharField(db_column='CodePays', max_length=3, blank=True, null=True)  # Field name made lowercase.

    ville_eng = models.CharField(db_column='Ville_Eng', max_length=30, blank=True, null=True)  # Field name made lowercase.

    pays_eng = models.CharField(db_column='Pays_Eng', max_length=50, blank=True, null=True)  # Field name made lowercase.

    tlp = models.CharField(db_column='Tlp', max_length=50, blank=True, null=True)  # Field name made lowercase.

    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    site = models.CharField(db_column='Site', max_length=50, blank=True, null=True)  # Field name made lowercase.

    permanence = models.CharField(db_column='Permanence', max_length=60, blank=True, null=True)  # Field name made lowercase.

    observations = models.CharField(db_column='Observations', max_length=155, blank=True, null=True)  # Field name made lowercase.

    localisation = models.CharField(db_column='Localisation', max_length=80, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'services'

        unique_together = (('codeserv', 'exten'),)





class Statmis(models.Model):

    code_pays = models.CharField(db_column='Code_Pays', max_length=5, blank=True, null=True)  # Field name made lowercase.

    nmission = models.FloatField(db_column='NMission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    codedlg = models.CharField(db_column='Codedlg', max_length=5, blank=True, null=True)  # Field name made lowercase.

    statut = models.CharField(db_column='Statut', max_length=1, blank=True, null=True)  # Field name made lowercase.

    suite_de = models.FloatField(db_column='Suite_de', blank=True, null=True)  # Field name made lowercase.

    numadh = models.SmallIntegerField(db_column='NUMADH', blank=True, null=True)  # Field name made lowercase.

    raison_soc = models.CharField(db_column='RAISON_SOC', max_length=60, blank=True, null=True)  # Field name made lowercase.

    filiale_de = models.FloatField(db_column='Filiale_de', blank=True, null=True)  # Field name made lowercase.

    code_posta = models.CharField(db_column='CODE_POSTA', max_length=5, blank=True, null=True)  # Field name made lowercase.

    categ = models.CharField(db_column='Categ', max_length=3, blank=True, null=True)  # Field name made lowercase.

    correspondant = models.CharField(db_column='Correspondant', max_length=70, blank=True, null=True)  # Field name made lowercase.

    date_demande = models.DateTimeField(db_column='Date_demande', blank=True, null=True)  # Field name made lowercase.

    objet_demande = models.CharField(db_column='Objet_demande', max_length=255, blank=True, null=True)  # Field name made lowercase.

    filire = models.CharField(db_column='Filire', max_length=3, blank=True, null=True)  # Field name made lowercase.

    code_fonction = models.CharField(db_column='Code_Fonction', max_length=2, blank=True, null=True)  # Field name made lowercase.

    initiateur = models.CharField(db_column='Initiateur', max_length=5, blank=True, null=True)  # Field name made lowercase.

    dlgation = models.CharField(db_column='Dlgation', max_length=30, blank=True, null=True)  # Field name made lowercase.

    monteur = models.CharField(db_column='Monteur', max_length=27, blank=True, null=True)  # Field name made lowercase.

    loc_monteur = models.CharField(db_column='Loc_Monteur', max_length=2, blank=True, null=True)  # Field name made lowercase.

    date_enregistrement = models.DateTimeField(db_column='Date_Enregistrement', blank=True, null=True)  # Field name made lowercase.

    date_convention = models.DateTimeField(db_column='Date_Convention', blank=True, null=True)  # Field name made lowercase.

    date_dbut_mission = models.DateTimeField(db_column='Date_Dbut_Mission', blank=True, null=True)  # Field name made lowercase.

    date_fin_mission = models.DateTimeField(db_column='Date_Fin_Mission', blank=True, null=True)  # Field name made lowercase.

    dure_convention = models.SmallIntegerField(db_column='Dure_Convention', blank=True, null=True)  # Field name made lowercase.

    date_fin_convention = models.DateTimeField(db_column='Date_Fin_Convention', blank=True, null=True)  # Field name made lowercase.

    nbre_jours_mission = models.SmallIntegerField(db_column='Nbre_Jours_Mission', blank=True, null=True)  # Field name made lowercase.

    observations = models.CharField(db_column='Observations', max_length=60, blank=True, null=True)  # Field name made lowercase.

    nbre_jours_prpar = models.SmallIntegerField(db_column='Nbre_Jours_Prpar', blank=True, null=True)  # Field name made lowercase.

    nbre_jours_rapport = models.SmallIntegerField(db_column='Nbre_Jours_Rapport', blank=True, null=True)  # Field name made lowercase.

    date_de_clture = models.DateTimeField(db_column='Date_de_Clture', blank=True, null=True)  # Field name made lowercase.

    rgion = models.SmallIntegerField(db_column='Rgion', blank=True, null=True)  # Field name made lowercase.

    classement = models.SmallIntegerField(db_column='Classement', blank=True, null=True)  # Field name made lowercase.

    paysetr = models.CharField(db_column='Paysetr', max_length=5, blank=True, null=True)  # Field name made lowercase.

    nmisetr = models.FloatField(db_column='NMisetr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    delegetr = models.CharField(db_column='Delegetr', max_length=5, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'statmis'





class Statuttiers(models.Model):

    id = models.IntegerField(blank=True, null=True)

    nom = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)

    lucratif = models.CharField(db_column='Lucratif', max_length=2)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'statuttiers'





class TAdress(models.Model):

    pk = models.CompositePrimaryKey('Necti', 'Nadres')

    necti = models.IntegerField(db_column='Necti')  # Field name made lowercase.

    nadres = models.SmallIntegerField(db_column='Nadres')  # Field name made lowercase.

    adrbas = models.CharField(db_column='AdrBas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    adrcom = models.CharField(db_column='AdrCom', max_length=50, blank=True, null=True)  # Field name made lowercase.

    vil = models.CharField(db_column='Vil', max_length=50)  # Field name made lowercase.

    copos = models.CharField(db_column='CoPos', max_length=6, blank=True, null=True)  # Field name made lowercase.

    pays = models.CharField(db_column='Pays', max_length=3)  # Field name made lowercase.

    tel = models.CharField(db_column='Tel', max_length=15, blank=True, null=True)  # Field name made lowercase.

    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.

    valide = models.CharField(db_column='Valide', max_length=1, blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMaj', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_adress'

        unique_together = (('necti', 'nadres'),)





class TAffvers(models.Model):

    numaff = models.AutoField(db_column='NumAff', primary_key=True)  # Field name made lowercase.

    numversr = models.IntegerField(db_column='NumVersR', blank=True, null=True)  # Field name made lowercase.

    codedlg = models.CharField(db_column='Codedlg', max_length=50)  # Field name made lowercase.

    dataff = models.DateTimeField(db_column='DatAff')  # Field name made lowercase.

    dataff0 = models.DateTimeField(db_column='DatAff0')  # Field name made lowercase.

    monaff = models.DecimalField(db_column='MonAff', max_digits=65, decimal_places=4)  # Field name made lowercase.

    contrepass = models.IntegerField(db_column='ContrePass', blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_affvers'





class TCorresp(models.Model):

    pk = models.CompositePrimaryKey('NumPM', 'NumCor')

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    numcor = models.IntegerField(db_column='NumCor')  # Field name made lowercase.

    titre = models.CharField(db_column='Titre', max_length=4, blank=True, null=True)  # Field name made lowercase.

    nomcor = models.CharField(db_column='NomCor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    foncor = models.CharField(db_column='FonCor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    tel1 = models.CharField(db_column='Tel1', max_length=20, blank=True, null=True)  # Field name made lowercase.

    tel2 = models.CharField(db_column='Tel2', max_length=20, blank=True, null=True)  # Field name made lowercase.

    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.

    datemaj = models.DateTimeField(db_column='DateMAJ', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_corresp'

        unique_together = (('numpm', 'numcor'),)





class TCoti(models.Model):

    pk = models.CompositePrimaryKey('NEcti', 'An', 'typ')

    necti = models.IntegerField(db_column='NEcti')  # Field name made lowercase.

    an = models.SmallIntegerField(db_column='An')  # Field name made lowercase.

    typ = models.CharField(max_length=1)

    numordre = models.SmallIntegerField(db_column='NumOrdre', blank=True, null=True)  # Field name made lowercase.

    datver = models.DateTimeField(db_column='DatVer')  # Field name made lowercase.

    mont = models.DecimalField(db_column='Mont', max_digits=65, decimal_places=4)  # Field name made lowercase.

    mode_de_paiement = models.CharField(db_column='Mode de paiement', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    banque = models.CharField(db_column='Banque', max_length=30, blank=True, null=True)  # Field name made lowercase.

    edite = models.DateTimeField(db_column='Edite', blank=True, null=True)  # Field name made lowercase.

    raicoti = models.CharField(db_column='RaiCoti', max_length=2, blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_coti'

        unique_together = (('necti', 'an', 'typ'),)





class TErreurmail(models.Model):

    pk = models.CompositePrimaryKey('Cotisation', 'NumExp')

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    cotisation = models.IntegerField(db_column='Cotisation')  # Field name made lowercase.

    datemail = models.DateTimeField(db_column='DateMail', blank=True, null=True)  # Field name made lowercase.

    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.

    mail = models.CharField(db_column='Mail', max_length=100, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_erreurmail'





class TEtacivil(models.Model):

    numpm = models.IntegerField(db_column='NumPM', primary_key=True)  # Field name made lowercase.

    codeclient = models.CharField(db_column='CodeClient', max_length=6, blank=True, null=True)  # Field name made lowercase.

    datadh = models.DateTimeField(db_column='DatAdh', blank=True, null=True)  # Field name made lowercase.

    datrad = models.DateTimeField(db_column='DatRad', blank=True, null=True)  # Field name made lowercase.

    unitgestion = models.CharField(db_column='UnitGestion', max_length=5)  # Field name made lowercase.

    correcti = models.CharField(db_column='CorrECTI', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=200)  # Field name made lowercase.

    activprinc = models.CharField(db_column='ActivPrinc', max_length=200, blank=True, null=True)  # Field name made lowercase.

    codnaf = models.CharField(db_column='CodNAF', max_length=5)  # Field name made lowercase.

    codnaf_rev2 = models.CharField(db_column='CodNAF_Rev2', max_length=6, blank=True, null=True)  # Field name made lowercase.

    siret = models.CharField(db_column='SIRET', max_length=17, blank=True, null=True)  # Field name made lowercase.

    catgorie = models.CharField(db_column='Catgorie', max_length=2)  # Field name made lowercase.

    effectif = models.CharField(db_column='Effectif', max_length=2, blank=True, null=True)  # Field name made lowercase.

    ca = models.CharField(db_column='CA', max_length=2, blank=True, null=True)  # Field name made lowercase.

    adresbas = models.CharField(db_column='AdresBas', max_length=36, blank=True, null=True)  # Field name made lowercase.

    adrescompl = models.CharField(db_column='AdresCompl', max_length=36, blank=True, null=True)  # Field name made lowercase.

    codpost = models.CharField(db_column='CodPost', max_length=10, blank=True, null=True)  # Field name made lowercase.

    ville = models.CharField(db_column='Ville', max_length=100)  # Field name made lowercase.

    code3a = models.CharField(db_column='Code3A', max_length=5)  # Field name made lowercase.

    tl = models.CharField(db_column='Tl', max_length=20, blank=True, null=True)  # Field name made lowercase.

    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    codalerte = models.CharField(db_column='CodAlerte', max_length=1, blank=True, null=True)  # Field name made lowercase.

    cometat = models.CharField(db_column='ComEtat', max_length=240, blank=True, null=True)  # Field name made lowercase.

    ajoutmission = models.IntegerField(db_column='AjoutMission', blank=True, null=True)  # Field name made lowercase.

    validresp = models.IntegerField(db_column='ValidResp', blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_etacivil'





class TExpert(models.Model):

    numexp = models.IntegerField(db_column='NumExp', primary_key=True)  # Field name made lowercase.

    datvis = models.DateTimeField(db_column='DatVis', blank=True, null=True)  # Field name made lowercase.

    datins = models.DateTimeField(db_column='DatIns', blank=True, null=True)  # Field name made lowercase.

    autredeleg = models.CharField(db_column='AutreDeleg', max_length=5, blank=True, null=True)  # Field name made lowercase.

    titre = models.CharField(db_column='Titre', max_length=3)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=27)  # Field name made lowercase.

    prnom = models.CharField(db_column='Prnom', max_length=20)  # Field name made lowercase.

    telpor = models.CharField(db_column='TelPor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    emel = models.CharField(db_column='Emel', max_length=50, blank=True, null=True)  # Field name made lowercase.

    datmajtel = models.DateTimeField(db_column='DatMajTel', blank=True, null=True)  # Field name made lowercase.

    datnai = models.DateTimeField(db_column='DatNai', blank=True, null=True)  # Field name made lowercase.

    villenai = models.CharField(db_column='VilleNai', max_length=50, blank=True, null=True)  # Field name made lowercase.

    paysnai = models.CharField(db_column='PaysNai', max_length=3, blank=True, null=True)  # Field name made lowercase.

    nationalit = models.CharField(db_column='Nationalit', max_length=3)  # Field name made lowercase.

    connu = models.CharField(db_column='Connu', max_length=2, blank=True, null=True)  # Field name made lowercase.

    profil = models.TextField(db_column='Profil', blank=True, null=True)  # Field name made lowercase.

    acquispro = models.TextField(db_column='AcquisPro', blank=True, null=True)  # Field name made lowercase.

    m_etranger = models.IntegerField(db_column='M_Etranger', blank=True, null=True)  # Field name made lowercase.

    m_france = models.IntegerField(db_column='M_France', blank=True, null=True)  # Field name made lowercase.

    m_enseignement = models.IntegerField(db_column='M_Enseignement', blank=True, null=True)  # Field name made lowercase.

    m_social = models.IntegerField(db_column='M_Social', blank=True, null=True)  # Field name made lowercase.

    m_ecti = models.IntegerField(db_column='M_Ecti', blank=True, null=True)  # Field name made lowercase.

    m_collectterritoriale = models.IntegerField(db_column='M_CollectTerritoriale', blank=True, null=True)  # Field name made lowercase.

    m_tpe_pme = models.IntegerField(db_column='M_TPE_PME', blank=True, null=True)  # Field name made lowercase.

    perm = models.CharField(db_column='Perm', max_length=5, blank=True, null=True)  # Field name made lowercase.

    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    datmajstatus = models.DateTimeField(db_column='DatMajStatus', blank=True, null=True)  # Field name made lowercase.

    spec1 = models.CharField(db_column='Spec1', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier1 = models.CharField(db_column='Metier1', max_length=3, blank=True, null=True)  # Field name made lowercase.

    spec2 = models.CharField(db_column='Spec2', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier2 = models.CharField(db_column='Metier2', max_length=3, blank=True, null=True)  # Field name made lowercase.

    spec3 = models.CharField(db_column='Spec3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier3 = models.CharField(db_column='Metier3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    acfon = models.CharField(db_column='ACFON', max_length=80, blank=True, null=True)  # Field name made lowercase.

    cotis = models.CharField(db_column='Cotis', max_length=4, blank=True, null=True)  # Field name made lowercase.

    numpar = models.CharField(db_column='NumPar', max_length=50, blank=True, null=True)  # Field name made lowercase.

    datpar = models.DateTimeField(db_column='DatPar', blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMaj', blank=True, null=True)  # Field name made lowercase.

    payment_validated = models.IntegerField()

    commentaire = models.CharField(db_column='Commentaire', max_length=400, blank=True, null=True)  # Field name made lowercase.

    dateenvoimaildt = models.DateTimeField(db_column='DateEnvoiMailDT', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_expert'





class TExprint(models.Model):

    necti = models.IntegerField(db_column='NEcti')  # Field name made lowercase.

    pay = models.CharField(db_column='Pay', max_length=3)  # Field name made lowercase.

    nature = models.CharField(db_column='Nature', max_length=255, blank=True, null=True)  # Field name made lowercase.

    periodeduree = models.CharField(db_column='PeriodeDuree', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_exprint'





class TForm(models.Model):

    pk = models.CompositePrimaryKey('NEcti', 'Form')

    necti = models.IntegerField(db_column='NEcti')  # Field name made lowercase.

    form = models.CharField(db_column='Form', max_length=3)  # Field name made lowercase.

    comment = models.CharField(db_column='Comment', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_form'

        unique_together = (('necti', 'form'),)





class TLang(models.Model):

    pk = models.CompositePrimaryKey('NEcti', 'Lang')

    necti = models.IntegerField(db_column='NEcti')  # Field name made lowercase.

    lang = models.CharField(db_column='Lang', max_length=3)  # Field name made lowercase.

    deg = models.CharField(db_column='Deg', max_length=1, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_lang'

        unique_together = (('necti', 'lang'),)





class TLienperso(models.Model):

    pk = models.CompositePrimaryKey('CodeServ', 'Exten', 'NumExp', 'DateDebFonc')

    codeserv = models.CharField(db_column='CodeServ', max_length=4)  # Field name made lowercase.

    exten = models.CharField(db_column='Exten', max_length=2)  # Field name made lowercase.

    indice = models.SmallIntegerField(db_column='Indice')  # Field name made lowercase.

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    fonct = models.CharField(db_column='Fonct', max_length=1)  # Field name made lowercase.

    tlphone = models.CharField(db_column='Tlphone', max_length=32, blank=True, null=True)  # Field name made lowercase.

    melpro = models.CharField(db_column='MelPro', max_length=50, blank=True, null=True)  # Field name made lowercase.

    perm = models.CharField(db_column='Perm', max_length=60, blank=True, null=True)  # Field name made lowercase.

    datedebfonc = models.DateTimeField(db_column='DateDebFonc')  # Field name made lowercase.

    datefinfonc = models.DateTimeField(db_column='DateFinFonc', blank=True, null=True)  # Field name made lowercase.

    annuaire = models.IntegerField(db_column='Annuaire', blank=True, null=True)  # Field name made lowercase.

    courrier = models.IntegerField(db_column='Courrier', blank=True, null=True)  # Field name made lowercase.

    motdepasse = models.CharField(db_column='MotDePasse', max_length=15, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_lienperso'

        unique_together = (('codeserv', 'exten', 'numexp', 'datedebfonc'),)





class TLienserv(models.Model):

    pk = models.CompositePrimaryKey('CodeServ1', 'Exten1', 'CodeServ2', 'Exten2', 'DatOuvLien')

    codeserv1 = models.CharField(db_column='CodeServ1', max_length=4)  # Field name made lowercase.

    exten1 = models.CharField(db_column='Exten1', max_length=2)  # Field name made lowercase.

    indice1 = models.SmallIntegerField(db_column='Indice1')  # Field name made lowercase.

    codeserv2 = models.CharField(db_column='CodeServ2', max_length=4)  # Field name made lowercase.

    exten2 = models.CharField(db_column='Exten2', max_length=2)  # Field name made lowercase.

    indice2 = models.SmallIntegerField(db_column='Indice2')  # Field name made lowercase.

    datouvlien = models.DateTimeField(db_column='DatOuvLien')  # Field name made lowercase.

    datfinlien = models.DateTimeField(db_column='DatFinLien', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_lienserv'

        unique_together = (('codeserv1', 'exten1', 'codeserv2', 'exten2', 'datouvlien'),)





class TSitu(models.Model):

    pk = models.CompositePrimaryKey('NumPM', 'RangSitu')

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    rangsitu = models.SmallIntegerField(db_column='RangSitu')  # Field name made lowercase.

    position = models.CharField(db_column='Position', max_length=50)  # Field name made lowercase.

    coddure = models.CharField(db_column='CodDure', max_length=1)  # Field name made lowercase.

    codepayeur = models.CharField(db_column='CodePayeur', max_length=50)  # Field name made lowercase.

    numpayeur = models.IntegerField(db_column='NumPayeur')  # Field name made lowercase.

    rsitupayeur = models.SmallIntegerField(db_column='RSituPayeur', blank=True, null=True)  # Field name made lowercase.

    typecotis = models.CharField(db_column='TypeCotis', max_length=2, blank=True, null=True)  # Field name made lowercase.

    debvalid = models.DateTimeField(db_column='DebValid')  # Field name made lowercase.

    finvalid = models.DateTimeField(db_column='FinValid', blank=True, null=True)  # Field name made lowercase.

    cotht = models.DecimalField(db_column='CotHT', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    tauxtva = models.FloatField(db_column='TauxTVA', blank=True, null=True)  # Field name made lowercase.

    rglementrduit = models.IntegerField(db_column='RglementRduit', blank=True, null=True)  # Field name made lowercase.

    frac = models.CharField(db_column='Frac', max_length=1, blank=True, null=True)  # Field name made lowercase.

    numappel = models.CharField(db_column='NumAppel', max_length=10, blank=True, null=True)  # Field name made lowercase.

    datappel = models.DateTimeField(db_column='DatAppel', blank=True, null=True)  # Field name made lowercase.

    appelenvoy = models.IntegerField(db_column='AppelEnvoy', blank=True, null=True)  # Field name made lowercase.

    mlappelenvoy = models.IntegerField(db_column='MlAppelEnvoy', blank=True, null=True)  # Field name made lowercase.

    datsuivi = models.DateTimeField(db_column='DatSuivi', blank=True, null=True)  # Field name made lowercase.

    codsuivi = models.SmallIntegerField(db_column='CodSuivi', blank=True, null=True)  # Field name made lowercase.

    actionsuivi = models.CharField(db_column='ActionSuivi', max_length=100, blank=True, null=True)  # Field name made lowercase.

    mlsuivienvoy = models.IntegerField(db_column='MlSuiviEnvoy', blank=True, null=True)  # Field name made lowercase.

    rponsedlg = models.CharField(db_column='RponseDlg', max_length=100, blank=True, null=True)  # Field name made lowercase.

    datrelan = models.DateTimeField(db_column='DatRelan', blank=True, null=True)  # Field name made lowercase.

    relanceenvoye = models.IntegerField(db_column='RelanceEnvoye', blank=True, null=True)  # Field name made lowercase.

    questionnaireenvoy = models.IntegerField(db_column='QuestionnaireEnvoy', blank=True, null=True)  # Field name made lowercase.

    prov = models.IntegerField(db_column='Prov')  # Field name made lowercase.

    comsitu = models.CharField(db_column='ComSitu', max_length=160, blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_situ'

        unique_together = (('numpm', 'rangsitu'),)





class TTva(models.Model):

    code3a = models.CharField(db_column='Code3A', primary_key=True, max_length=3)  # Field name made lowercase.

    tauxtva = models.FloatField(db_column='TauxTVA')  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_tva'





class TValidationexp(models.Model):

    pk = models.CompositePrimaryKey('Code', 'NumExp')

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    code = models.IntegerField(db_column='Code')  # Field name made lowercase.

    datestatut = models.DateTimeField(db_column='dateStatut', blank=True, null=True)  # Field name made lowercase.

    par = models.IntegerField(db_column='Par', blank=True, null=True)  # Field name made lowercase.

    deleg = models.CharField(db_column='Deleg', max_length=6, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_validationexp'





class TVersprv(models.Model):

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    rangsitu = models.SmallIntegerField(db_column='RangSitu')  # Field name made lowercase.

    numvers = models.SmallIntegerField(db_column='NumVers', blank=True, null=True)  # Field name made lowercase.

    datvers = models.DateTimeField(db_column='DatVers')  # Field name made lowercase.

    natversprv = models.CharField(db_column='NatVersPrv', max_length=3, blank=True, null=True)  # Field name made lowercase.

    monhtprv = models.DecimalField(db_column='MonHTPrv', max_digits=65, decimal_places=4)  # Field name made lowercase.

    monttcprv = models.DecimalField(db_column='MonTTCPrv', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    numfactprv = models.CharField(db_column='NumFactPrv', max_length=50, blank=True, null=True)  # Field name made lowercase.

    numligneprv = models.SmallIntegerField(db_column='NumLignePrv', blank=True, null=True)  # Field name made lowercase.

    datfactprv = models.DateTimeField(db_column='DatFactPrv', blank=True, null=True)  # Field name made lowercase.

    nummissprv = models.CharField(db_column='NumMissPrv', max_length=50, blank=True, null=True)  # Field name made lowercase.

    envfactprv = models.IntegerField(db_column='EnvFactPrv', blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_versprv'





class TVersrel(models.Model):

    numversr = models.AutoField(db_column='NumVersR', primary_key=True)  # Field name made lowercase.

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    rangsitu = models.SmallIntegerField(db_column='RangSitu')  # Field name made lowercase.

    datvers = models.DateTimeField(db_column='DatVers')  # Field name made lowercase.

    datvers0 = models.DateTimeField(db_column='DatVers0', blank=True, null=True)  # Field name made lowercase.

    natvers = models.CharField(db_column='NatVers', max_length=3)  # Field name made lowercase.

    monhtrel = models.DecimalField(db_column='MonHTRel', max_digits=65, decimal_places=4)  # Field name made lowercase.

    monttc = models.DecimalField(db_column='MonTTC', max_digits=65, decimal_places=4)  # Field name made lowercase.

    numfact = models.CharField(db_column='NumFact', max_length=10, blank=True, null=True)  # Field name made lowercase.

    numligne = models.SmallIntegerField(db_column='NumLigne', blank=True, null=True)  # Field name made lowercase.

    datfact = models.DateTimeField(db_column='DatFact', blank=True, null=True)  # Field name made lowercase.

    nummiss = models.CharField(db_column='NumMiss', max_length=10, blank=True, null=True)  # Field name made lowercase.

    comver = models.CharField(db_column='ComVer', max_length=40, blank=True, null=True)  # Field name made lowercase.

    factureenvoye = models.IntegerField(db_column='FactureEnvoye', blank=True, null=True)  # Field name made lowercase.

    contrepass = models.IntegerField(db_column='ContrePass', blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 't_versrel'





class Tauxtvasitu(models.Model):

    code = models.FloatField()

    taux = models.CharField(max_length=155)



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tauxtvasitu'





class TcCatgorie(models.Model):

    catgorie = models.CharField(db_column='Catgorie', primary_key=True, max_length=3)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=100, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_catgorie'





class TcEffectif(models.Model):

    effsal = models.CharField(db_column='EFFSAL', primary_key=True, max_length=2)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_effectif'





class TcFonction(models.Model):

    codfonc = models.CharField(db_column='CodFonc', primary_key=True, max_length=1)  # Field name made lowercase.

    libelfonc = models.CharField(db_column='LibelFonc', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_fonction'





class TcForm(models.Model):

    formation = models.CharField(db_column='Formation', primary_key=True, max_length=3)  # Field name made lowercase.

    libell_formation = models.CharField(db_column='Libell Formation', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    complment = models.CharField(db_column='Complment', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_form'





class TcLang(models.Model):

    codlang = models.CharField(db_column='CodLang', primary_key=True, max_length=3)  # Field name made lowercase.

    libell = models.CharField(db_column='Libell', max_length=20, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_lang'





class TcPays(models.Model):

    code3a = models.CharField(db_column='Code3A', primary_key=True, max_length=5)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.

    titre = models.CharField(db_column='Titre', max_length=55, blank=True, null=True)  # Field name made lowercase.

    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.

    rgion = models.CharField(db_column='Rgion', max_length=3, blank=True, null=True)  # Field name made lowercase.

    lpays = models.CharField(db_column='Lpays', max_length=4, blank=True, null=True)  # Field name made lowercase.

    gpays = models.CharField(db_column='GPays', max_length=5, blank=True, null=True)  # Field name made lowercase.

    delreg = models.CharField(db_column='DelReg', max_length=5, blank=True, null=True)  # Field name made lowercase.

    hors_norme = models.IntegerField(db_column='Hors_Norme', blank=True, null=True)  # Field name made lowercase.

    risque = models.CharField(db_column='Risque', max_length=1, blank=True, null=True)  # Field name made lowercase.

    nomang = models.CharField(db_column='NomAng', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nomesp = models.CharField(db_column='NomEsp', max_length=50, blank=True, null=True)  # Field name made lowercase.

    etranger = models.IntegerField(db_column='Etranger', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_pays'





class TcPos(models.Model):

    position = models.CharField(db_column='Position', primary_key=True, max_length=1)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=70, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_pos'





class TcSitu(models.Model):

    codsortie = models.CharField(db_column='CodSortie', primary_key=True, max_length=1)  # Field name made lowercase.

    libsortie = models.CharField(db_column='LibSortie', max_length=50, blank=True, null=True)  # Field name made lowercase.

    applicat = models.CharField(db_column='Applicat', max_length=1, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_situ'





class TcSpe(models.Model):

    filire = models.IntegerField(db_column='Filire', primary_key=True)  # Field name made lowercase.

    libell_filire = models.CharField(db_column='Libell_Filire', max_length=255, blank=True, null=True)  # Field name made lowercase.

    validit = models.CharField(db_column='Validit', max_length=255, blank=True, null=True)  # Field name made lowercase.

    expert = models.CharField(db_column='Expert', max_length=255, blank=True, null=True)  # Field name made lowercase.

    numexpert = models.IntegerField(db_column='NumExpert', blank=True, null=True)  # Field name made lowercase.

    expert2 = models.CharField(db_column='Expert2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    anciencodeferry = models.CharField(db_column='AncienCodeFerry', max_length=255, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_spe'





class TcTitre(models.Model):

    n = models.SmallIntegerField(db_column='N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    titre = models.CharField(db_column='Titre', primary_key=True, max_length=4)  # Field name made lowercase.

    titrelong = models.CharField(db_column='TitreLong', max_length=20, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_titre'





class TcTranca(models.Model):

    tranca = models.CharField(db_column='TranCA', primary_key=True, max_length=2)  # Field name made lowercase.

    dfinition = models.CharField(db_column='Dfinition', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_tranca'





class TcTypserv(models.Model):

    codtypser = models.CharField(db_column='CodTypSer', primary_key=True, max_length=1)  # Field name made lowercase.

    libtypser = models.CharField(db_column='LibTypSer', max_length=60, blank=True, null=True)  # Field name made lowercase.

    abrev = models.CharField(db_column='Abrev', max_length=4, blank=True, null=True)  # Field name made lowercase.

    niveau = models.SmallIntegerField(db_column='Niveau', blank=True, null=True)  # Field name made lowercase.

    rseau = models.CharField(db_column='Rseau', max_length=1, blank=True, null=True)  # Field name made lowercase.

    affgeo = models.IntegerField(db_column='AffGeo')  # Field name made lowercase.

    attachinf = models.IntegerField(db_column='AttachInf', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tc_typserv'





class TciChampsr(models.Model):

    champr = models.CharField(db_column='ChampR', primary_key=True, max_length=12)  # Field name made lowercase.

    nr = models.SmallIntegerField(db_column='NR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'tci_champsr'





class TiAdh(models.Model):

    numexp = models.IntegerField(db_column='NumExp', primary_key=True)  # Field name made lowercase.

    titre = models.CharField(db_column='Titre', max_length=3)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=27, blank=True, null=True)  # Field name made lowercase.

    datnai = models.DateTimeField(db_column='DatNai', blank=True, null=True)  # Field name made lowercase.

    spec1 = models.CharField(db_column='Spec1', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier1 = models.CharField(db_column='Metier1', max_length=3, blank=True, null=True)  # Field name made lowercase.

    spec2 = models.CharField(db_column='Spec2', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier2 = models.CharField(db_column='Metier2', max_length=3, blank=True, null=True)  # Field name made lowercase.

    spec3 = models.CharField(db_column='Spec3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    metier3 = models.CharField(db_column='Metier3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    adrbas = models.CharField(db_column='AdrBas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    adrcom = models.CharField(db_column='AdrCom', max_length=50, blank=True, null=True)  # Field name made lowercase.

    vil = models.CharField(db_column='Vil', max_length=50, blank=True, null=True)  # Field name made lowercase.

    pays = models.CharField(db_column='Pays', max_length=3, blank=True, null=True)  # Field name made lowercase.

    payr = models.CharField(db_column='PayR', max_length=3, blank=True, null=True)  # Field name made lowercase.

    copos = models.CharField(db_column='CoPos', max_length=6, blank=True, null=True)  # Field name made lowercase.

    tel = models.CharField(db_column='Tel', max_length=15, blank=True, null=True)  # Field name made lowercase.

    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.

    langues = models.CharField(db_column='Langues', max_length=30, blank=True, null=True)  # Field name made lowercase.

    codregion = models.CharField(db_column='CodRegion', max_length=5, blank=True, null=True)  # Field name made lowercase.

    dep = models.CharField(db_column='Dep', max_length=2, blank=True, null=True)  # Field name made lowercase.

    coti = models.CharField(db_column='Coti', max_length=8, blank=True, null=True)  # Field name made lowercase.

    profil = models.TextField(db_column='Profil', blank=True, null=True)  # Field name made lowercase.

    acquispro = models.TextField(db_column='AcquisPro', blank=True, null=True)  # Field name made lowercase.

    specia = models.CharField(db_column='Specia', max_length=11, blank=True, null=True)  # Field name made lowercase.

    metiers = models.CharField(db_column='Metiers', max_length=11, blank=True, null=True)  # Field name made lowercase.

    telpor = models.CharField(db_column='TelPor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    emel = models.CharField(db_column='Emel', max_length=50, blank=True, null=True)  # Field name made lowercase.

    datadh = models.DateTimeField(db_column='DatAdh', blank=True, null=True)  # Field name made lowercase.

    m_etranger = models.IntegerField(db_column='M_Etranger', blank=True, null=True)  # Field name made lowercase.

    m_france = models.IntegerField(db_column='M_France', blank=True, null=True)  # Field name made lowercase.

    m_enseignement = models.IntegerField(db_column='M_Enseignement', blank=True, null=True)  # Field name made lowercase.

    m_social = models.IntegerField(db_column='M_Social', blank=True, null=True)  # Field name made lowercase.

    m_ecti = models.IntegerField(db_column='M_Ecti', blank=True, null=True)  # Field name made lowercase.

    m_collectterritoriale = models.IntegerField(db_column='M_CollectTerritoriale', blank=True, null=True)  # Field name made lowercase.

    m_tpe_pme = models.IntegerField(db_column='M_TPE_PME', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_adh'





class TiAppelprpa(models.Model):

    pk = models.CompositePrimaryKey('NumPM', 'RangSitu')

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    rangsitu = models.SmallIntegerField(db_column='RangSitu')  # Field name made lowercase.

    somdue = models.DecimalField(db_column='SomDue', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    unitgestion = models.CharField(db_column='UnitGestion', max_length=5, blank=True, null=True)  # Field name made lowercase.

    codeserv = models.CharField(db_column='CodeServ', max_length=4, blank=True, null=True)  # Field name made lowercase.

    exten = models.CharField(db_column='Exten', max_length=1, blank=True, null=True)  # Field name made lowercase.

    stopenvoi = models.IntegerField(db_column='StopEnvoi')  # Field name made lowercase.

    envoyeur = models.CharField(db_column='Envoyeur', max_length=50, blank=True, null=True)  # Field name made lowercase.

    valide = models.IntegerField(db_column='Valide')  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_appelprpa'

        unique_together = (('numpm', 'rangsitu'),)





class TiAppelquest(models.Model):

    pk = models.CompositePrimaryKey('NumPM', 'RangSitu')

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    rangsitu = models.SmallIntegerField(db_column='RangSitu')  # Field name made lowercase.

    unitgestion = models.CharField(db_column='UnitGestion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    dlgation = models.CharField(db_column='Dlgation', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=80, blank=True, null=True)  # Field name made lowercase.

    adresbas = models.CharField(db_column='AdresBas', max_length=80, blank=True, null=True)  # Field name made lowercase.

    adrescompl = models.CharField(db_column='AdresCompl', max_length=80, blank=True, null=True)  # Field name made lowercase.

    codpost = models.CharField(db_column='CodPost', max_length=12, blank=True, null=True)  # Field name made lowercase.

    ville = models.CharField(db_column='Ville', max_length=80, blank=True, null=True)  # Field name made lowercase.

    code3a = models.CharField(db_column='Code3A', max_length=5, blank=True, null=True)  # Field name made lowercase.

    titrelong = models.CharField(db_column='TitreLong', max_length=50, blank=True, null=True)  # Field name made lowercase.

    nomcor = models.CharField(db_column='NomCor', max_length=80, blank=True, null=True)  # Field name made lowercase.

    debvalid = models.DateTimeField(db_column='DebValid', blank=True, null=True)  # Field name made lowercase.

    finvalid = models.DateTimeField(db_column='FinValid', blank=True, null=True)  # Field name made lowercase.

    cotht = models.DecimalField(db_column='CotHT', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    nbmois = models.SmallIntegerField(db_column='NbMois', blank=True, null=True)  # Field name made lowercase.

    somversr1 = models.DecimalField(db_column='SomVersR1', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    modevers = models.TextField(db_column='ModeVers', blank=True, null=True)  # Field name made lowercase.

    datlimite = models.DateTimeField(db_column='DatLimite', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_appelquest'

        unique_together = (('numpm', 'rangsitu'),)





class TiCommetiers(models.Model):

    pk = models.CompositePrimaryKey('NumExp', 'Metier')

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    metier = models.CharField(db_column='Metier', max_length=3)  # Field name made lowercase.

    metierpere = models.CharField(db_column='MetierPere', max_length=3, blank=True, null=True)  # Field name made lowercase.

    nomlon = models.CharField(db_column='NomLon', max_length=100, blank=True, null=True)  # Field name made lowercase.

    metiercon = models.CharField(db_column='MetierCon', max_length=11, blank=True, null=True)  # Field name made lowercase.

    rang = models.SmallIntegerField(db_column='Rang', blank=True, null=True)  # Field name made lowercase.

    dep = models.CharField(db_column='Dep', max_length=3, blank=True, null=True)  # Field name made lowercase.

    pays = models.CharField(max_length=3, blank=True, null=True)

    profil = models.TextField(db_column='Profil', blank=True, null=True)  # Field name made lowercase.

    acquispro = models.TextField(db_column='AcquisPro', blank=True, null=True)  # Field name made lowercase.

    lancon = models.CharField(db_column='LanCon', max_length=24, blank=True, null=True)  # Field name made lowercase.

    datepremcoti = models.DateTimeField(db_column='DatePremCoti', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_commetiers'

        unique_together = (('numexp', 'metier'),)





class TiComspe(models.Model):

    pk = models.CompositePrimaryKey('NumExp', 'Spec')

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    spec = models.CharField(db_column='Spec', max_length=3)  # Field name made lowercase.

    secteurpere = models.CharField(db_column='SecteurPere', max_length=3, blank=True, null=True)  # Field name made lowercase.

    nomlon = models.CharField(db_column='NomLon', max_length=100, blank=True, null=True)  # Field name made lowercase.

    specon = models.CharField(db_column='SpeCon', max_length=11, blank=True, null=True)  # Field name made lowercase.

    rang = models.SmallIntegerField(db_column='Rang', blank=True, null=True)  # Field name made lowercase.

    dep = models.CharField(db_column='Dep', max_length=3, blank=True, null=True)  # Field name made lowercase.

    pays = models.CharField(max_length=3, blank=True, null=True)

    profil = models.TextField(db_column='Profil', blank=True, null=True)  # Field name made lowercase.

    acquispro = models.TextField(db_column='AcquisPro', blank=True, null=True)  # Field name made lowercase.

    lancon = models.CharField(db_column='LanCon', max_length=24, blank=True, null=True)  # Field name made lowercase.

    datepremcoti = models.DateTimeField(db_column='DatePremCoti', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_comspe'

        unique_together = (('numexp', 'spec'),)





class TiCoti1(models.Model):

    necti = models.IntegerField(db_column='NEcti', primary_key=True)  # Field name made lowercase.

    coti1 = models.SmallIntegerField(db_column='Coti1', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_coti1'





class TiCoti2(models.Model):

    necti = models.IntegerField(db_column='NEcti', primary_key=True)  # Field name made lowercase.

    coti2 = models.SmallIntegerField(db_column='Coti2', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_coti2'





class TiCoti3(models.Model):

    necti = models.IntegerField(db_column='NEcti', primary_key=True)  # Field name made lowercase.

    coti3 = models.SmallIntegerField(db_column='Coti3', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_coti3'





class TiCourrielversdlg(models.Model):

    unitgestion = models.CharField(db_column='UnitGestion', max_length=5, blank=True, null=True)  # Field name made lowercase.

    codeserv = models.CharField(db_column='CodeServ', max_length=4, blank=True, null=True)  # Field name made lowercase.

    exten = models.CharField(db_column='Exten', max_length=2, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    comptedenumpm = models.IntegerField(db_column='CompteDeNumPM', blank=True, null=True)  # Field name made lowercase.

    mlenvoy = models.IntegerField(db_column='MlEnvoy')  # Field name made lowercase.

    stopenvoi = models.IntegerField(db_column='StopEnvoi')  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_courrielversdlg'





class TiDept(models.Model):

    dep = models.CharField(db_column='Dep', max_length=2, blank=True, null=True)  # Field name made lowercase.

    nomdep = models.CharField(db_column='NomDep', max_length=25, blank=True, null=True)  # Field name made lowercase.

    slection = models.IntegerField(db_column='Slection', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_dept'





class TiDpassvalid(models.Model):

    numpm = models.IntegerField(db_column='NumPM', primary_key=True)  # Field name made lowercase.

    dernsitu = models.SmallIntegerField(db_column='DernSitu', blank=True, null=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=64, blank=True, null=True)  # Field name made lowercase.

    unitgestion = models.CharField(db_column='UnitGestion', max_length=5, blank=True, null=True)  # Field name made lowercase.

    codeserv = models.CharField(db_column='CodeServ', max_length=4, blank=True, null=True)  # Field name made lowercase.

    exten = models.CharField(db_column='Exten', max_length=2, blank=True, null=True)  # Field name made lowercase.

    finvalidnp = models.DateTimeField(db_column='FinValidNP', blank=True, null=True)  # Field name made lowercase.

    datappel = models.DateTimeField(db_column='DatAppel', blank=True, null=True)  # Field name made lowercase.

    datrelan = models.DateTimeField(db_column='DatRelan', blank=True, null=True)  # Field name made lowercase.

    datderncotis = models.DateTimeField(db_column='DatDernCotis', blank=True, null=True)  # Field name made lowercase.

    monderncotis = models.DecimalField(db_column='MonDernCotis', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    datfinvalid = models.DateTimeField(db_column='DatFinValid', blank=True, null=True)  # Field name made lowercase.

    stopenvoi = models.IntegerField(db_column='StopEnvoi')  # Field name made lowercase.

    envoyeur = models.CharField(db_column='Envoyeur', max_length=50, blank=True, null=True)  # Field name made lowercase.

    valide = models.IntegerField(db_column='Valide')  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_dpassvalid'





class TiInter(models.Model):

    numexp = models.IntegerField(db_column='NumExp', blank=True, null=True)  # Field name made lowercase.

    nlon = models.CharField(db_column='Nlon', max_length=255, blank=True, null=True)  # Field name made lowercase.

    specon = models.CharField(db_column='SpeCon', max_length=255, blank=True, null=True)  # Field name made lowercase.

    dep = models.CharField(db_column='Dep', max_length=2, blank=True, null=True)  # Field name made lowercase.

    profil = models.CharField(db_column='Profil', max_length=235, blank=True, null=True)  # Field name made lowercase.

    lancon = models.CharField(db_column='LanCon', max_length=30, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_inter'





class TiLang(models.Model):

    necti = models.IntegerField(db_column='NEcti', blank=True, null=True)  # Field name made lowercase.

    lang = models.CharField(max_length=255, blank=True, null=True)



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_lang'





class TiLang1(models.Model):

    necti = models.IntegerField(db_column='NEcti', blank=True, null=True)  # Field name made lowercase.

    langc = models.CharField(max_length=255, blank=True, null=True)

    sup = models.IntegerField(blank=True, null=True)



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_lang1'





class TiLexp(models.Model):

    numexp = models.IntegerField(db_column='NumExp', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_lexp'





class TiListpm(models.Model):

    champ1 = models.CharField(db_column='Champ1', max_length=50, blank=True, null=True)  # Field name made lowercase.

    numpm = models.IntegerField(db_column='NumPM', primary_key=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=200, blank=True, null=True)  # Field name made lowercase.

    unitgestion = models.CharField(db_column='UnitGestion', max_length=5, blank=True, null=True)  # Field name made lowercase.

    dpartement = models.CharField(db_column='Dpartement', max_length=2, blank=True, null=True)  # Field name made lowercase.

    codpost = models.CharField(db_column='CodPost', max_length=10, blank=True, null=True)  # Field name made lowercase.

    code3a = models.CharField(db_column='Code3A', max_length=3, blank=True, null=True)  # Field name made lowercase.

    codnaf = models.CharField(db_column='CodNAF', max_length=5, blank=True, null=True)  # Field name made lowercase.

    position = models.CharField(db_column='Position', max_length=1, blank=True, null=True)  # Field name made lowercase.

    cotht = models.DecimalField(db_column='CotHT', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    cotttc = models.DecimalField(db_column='CotTTC', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    somversr = models.DecimalField(db_column='SomVersR', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    somttc = models.DecimalField(db_column='SomTTC', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    debvalid = models.DateTimeField(db_column='DebValid', blank=True, null=True)  # Field name made lowercase.

    finvalid = models.DateTimeField(db_column='FinValid', blank=True, null=True)  # Field name made lowercase.

    sdure = models.CharField(db_column='sDure', max_length=2, blank=True, null=True)  # Field name made lowercase.

    datadh = models.DateTimeField(db_column='DatAdh', blank=True, null=True)  # Field name made lowercase.

    datrad = models.DateTimeField(db_column='DatRad', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_listpm'





class TiMail(models.Model):

    typepj = models.CharField(db_column='TypePJ', primary_key=True, max_length=4)  # Field name made lowercase.

    txtdpassvalid = models.TextField(db_column='TxtDpassValid', blank=True, null=True)  # Field name made lowercase.

    txtappelprpa1 = models.TextField(db_column='TxtAppelPrpa1', blank=True, null=True)  # Field name made lowercase.

    txtappelprpa2 = models.TextField(db_column='TxtAppelPrpa2', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_mail'





class TiMissiondpassvalid(models.Model):

    pk = models.CompositePrimaryKey('NumPM', 'Code_Pays', 'NumMission')

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    code_pays = models.CharField(db_column='Code_Pays', max_length=50)  # Field name made lowercase.

    nummission = models.IntegerField(db_column='NumMission')  # Field name made lowercase.

    dbutconvention = models.DateTimeField(db_column='DbutConvention', blank=True, null=True)  # Field name made lowercase.

    finconvention = models.DateTimeField(db_column='FinConvention', blank=True, null=True)  # Field name made lowercase.

    finvalid = models.DateTimeField(db_column='FinValid', blank=True, null=True)  # Field name made lowercase.

    actionsuivi = models.TextField(db_column='ActionSuivi', blank=True, null=True)  # Field name made lowercase.

    remarquepm = models.TextField(db_column='RemarquePM', blank=True, null=True)  # Field name made lowercase.

    datemaj = models.DateTimeField(db_column='DateMAJ', blank=True, null=True)  # Field name made lowercase.

    signature = models.IntegerField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_missiondpassvalid'

        unique_together = (('numpm', 'code_pays', 'nummission'),)





class TiParam(models.Model):

    retardmin = models.SmallIntegerField(db_column='RetardMin', blank=True, null=True)  # Field name made lowercase.

    retardmax = models.SmallIntegerField(db_column='RetardMax')  # Field name made lowercase.

    sommax = models.DecimalField(db_column='SomMax', max_digits=65, decimal_places=4)  # Field name made lowercase.

    finvalidmin = models.DateTimeField(db_column='FinValidMin')  # Field name made lowercase.

    finvalidmax = models.DateTimeField(db_column='FinValidMax')  # Field name made lowercase.

    datfinvalid = models.DateTimeField(db_column='DatFinValid')  # Field name made lowercase.

    debmissmin = models.DateTimeField(db_column='DebMissMin')  # Field name made lowercase.

    debmissmax = models.DateTimeField(db_column='DebMissMax')  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ')  # Field name made lowercase.

    datfactmin = models.DateTimeField(db_column='DatFactMin', blank=True, null=True)  # Field name made lowercase.

    datfactmax = models.DateTimeField(db_column='DatFactMax', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_param'





class TiPmnonenrgle(models.Model):

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_pmnonenrgle'





class TiRenouvellementCoti(models.Model):

    pk = models.CompositePrimaryKey('NEcti', 'An', 'typ')

    necti = models.IntegerField(db_column='NEcti')  # Field name made lowercase.

    an = models.SmallIntegerField(db_column='An')  # Field name made lowercase.

    typ = models.CharField(max_length=1)

    numordre = models.SmallIntegerField(db_column='NumOrdre', blank=True, null=True)  # Field name made lowercase.

    datver = models.DateTimeField(db_column='DatVer')  # Field name made lowercase.

    mont = models.DecimalField(db_column='Mont', max_digits=65, decimal_places=4)  # Field name made lowercase.

    mode_de_paiement = models.CharField(db_column='Mode de paiement', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    banque = models.CharField(db_column='Banque', max_length=30, blank=True, null=True)  # Field name made lowercase.

    edite = models.DateTimeField(db_column='Edite', blank=True, null=True)  # Field name made lowercase.

    raicoti = models.CharField(db_column='RaiCoti', max_length=2, blank=True, null=True)  # Field name made lowercase.

    datmaj = models.DateTimeField(db_column='DatMAJ', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_renouvellement_coti'

        unique_together = (('necti', 'an', 'typ'),)





class TiStatutexperttoupdt(models.Model):

    numexp = models.IntegerField(db_column='NumExp', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_statutexperttoupdt'





class TiTabexp(models.Model):

    numexp = models.IntegerField(db_column='NumExp', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_tabexp'





class TiVisexp(models.Model):

    numexp = models.IntegerField(db_column='NumExp', blank=True, null=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=27, blank=True, null=True)  # Field name made lowercase.

    prnom = models.CharField(db_column='Prnom', max_length=20, blank=True, null=True)  # Field name made lowercase.

    nadres = models.SmallIntegerField(db_column='Nadres', blank=True, null=True)  # Field name made lowercase.

    copos = models.CharField(db_column='CoPos', max_length=6, blank=True, null=True)  # Field name made lowercase.

    pays = models.CharField(db_column='Pays', max_length=3, blank=True, null=True)  # Field name made lowercase.

    profil = models.CharField(db_column='Profil', max_length=235, blank=True, null=True)  # Field name made lowercase.

    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'tablecti'

        managed = False

        db_table = 'ti_visexp'

