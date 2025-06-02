# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class Categorielucrative(models.Model):

    code = models.CharField(max_length=2, db_collation='utf8mb4_general_ci', blank=True, null=True)

    libelle = models.CharField(max_length=255, db_collation='utf8mb4_general_ci', blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'categorielucrative'





class Conventionfiliere(models.Model):

    id = models.IntegerField(blank=True, null=True)

    nom = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'conventionfiliere'





class Conventionfonction(models.Model):

    id = models.IntegerField(blank=True, null=True)

    nom = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'conventionfonction'





class Conventionnature(models.Model):

    id = models.IntegerField(blank=True, null=True)

    nomcategorie = models.CharField(db_column='nomCategorie', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    nom = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)

    lucratif = models.CharField(db_column='Lucratif', max_length=2)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'conventionnature'





class Conventionstatut(models.Model):

    id = models.IntegerField(blank=True, null=True)

    nom = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)

    lucratif = models.CharField(db_column='Lucratif', max_length=2)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'conventionstatut'





class Conventionsuiviedition(models.Model):

    nummission = models.IntegerField(db_column='NumMission')  # Field name made lowercase.

    numsuivi = models.IntegerField(db_column='NumSuivi')  # Field name made lowercase.

    numexp = models.IntegerField(db_column='NumExp')  # Field name made lowercase.

    datesuivi = models.DateTimeField(db_column='DateSuivi', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'conventionsuiviedition'





class Correspdelegsage(models.Model):

    codedeleg = models.TextField(db_column='codeDeleg')  # Field name made lowercase.

    nom = models.TextField()

    codecomptable = models.TextField(db_column='codeComptable')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'correspdelegsage'





class Correspfichier(models.Model):

    nom = models.TextField()

    chemin = models.TextField()

    type = models.TextField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'correspfichier'





class Devise(models.Model):

    pays = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)

    nom = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)

    codealpha = models.CharField(db_column='codeAlpha', max_length=3, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    codenum = models.IntegerField(db_column='codeNum', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'devise'





class Expertmission(models.Model):

    nummission = models.IntegerField(db_column='NumMission', blank=True, null=True)  # Field name made lowercase.

    numexpert = models.IntegerField(db_column='NumExpert', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'expertmission'





class FeedbackConsultant(models.Model):

    mid = models.IntegerField(blank=True, null=True)

    consultant_nr = models.IntegerField(blank=True, null=True)

    days = models.FloatField(blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'feedback_consultant'





class FeedbackFollowup(models.Model):

    mid = models.IntegerField(blank=True, null=True)

    c_name = models.CharField(max_length=765, blank=True, null=True)

    c_info = models.CharField(max_length=765, blank=True, null=True)

    c_action = models.CharField(max_length=765, blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'feedback_followup'





class FeedbackInfo(models.Model):

    fb_id = models.AutoField(primary_key=True)

    mission_id = models.IntegerField(blank=True, null=True)

    date_from = models.DateField(blank=True, null=True)

    date_to = models.DateField(blank=True, null=True)

    rcp_name = models.CharField(max_length=765, blank=True, null=True)

    days_nr = models.FloatField(blank=True, null=True)

    location = models.CharField(max_length=765, blank=True, null=True)

    feedback = models.CharField(max_length=1500, blank=True, null=True)

    fb_date = models.DateTimeField(blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'feedback_info'





class Historiquesage(models.Model):

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    dateenvoi = models.DateTimeField(db_column='dateEnvoi')  # Field name made lowercase.

    idndf = models.IntegerField(db_column='idNdf')  # Field name made lowercase.

    numexp = models.IntegerField(db_column='numExp')  # Field name made lowercase.

    nomfichier = models.CharField(db_column='nomFichier', max_length=65)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'historiquesage'





class Imputationcomptablendf(models.Model):

    libelle = models.TextField()

    typemission = models.TextField(db_column='typeMission', blank=True, null=True)  # Field name made lowercase.

    fraiscompris = models.TextField(db_column='fraisCompris', blank=True, null=True)  # Field name made lowercase.

    codecomptable = models.IntegerField(db_column='codeComptable')  # Field name made lowercase.

    codeassocie = models.IntegerField(db_column='codeAssocie', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'imputationcomptablendf'





class Imputationcomptablendfi(models.Model):

    codebusiness = models.TextField(db_column='codeBusiness')  # Field name made lowercase.

    libellebusiness = models.TextField(db_column='libelleBusiness')  # Field name made lowercase.

    codeanalytique = models.TextField(db_column='codeAnalytique')  # Field name made lowercase.

    codecomptable = models.IntegerField(db_column='codeComptable', blank=True, null=True)  # Field name made lowercase.

    tva = models.TextField(db_column='TVA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    commentaire = models.TextField(db_column='Commentaire', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'imputationcomptablendfi'





class Lignedefrais(models.Model):

    idnote = models.IntegerField(db_column='idNote')  # Field name made lowercase.

    typedefrais = models.IntegerField()

    typedepense = models.IntegerField(blank=True, null=True)

    description = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)

    montant = models.FloatField(blank=True, null=True)

    montanteuro = models.FloatField(db_column='montantEuro')  # Field name made lowercase.

    devise = models.CharField(max_length=3, db_collation='utf8_general_ci')

    quantite = models.IntegerField(blank=True, null=True)

    date_frais = models.DateField(blank=True, null=True)

    montant_ht = models.FloatField(blank=True, null=True)

    taux_tva = models.FloatField(blank=True, null=True)

    tva_rembourser = models.IntegerField(blank=True, null=True)

    tva_factu_ecti = models.IntegerField(blank=True, null=True)

    dateinsert = models.DateTimeField(db_column='dateInsert', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'lignedefrais'





class Lignedekm(models.Model):

    idnote = models.IntegerField(db_column='idNote')  # Field name made lowercase.

    description = models.CharField(max_length=255, blank=True, null=True)

    nbkm = models.FloatField(db_column='nbKm', blank=True, null=True)  # Field name made lowercase.

    is2roues = models.IntegerField(db_column='Is2Roues', blank=True, null=True)  # Field name made lowercase.

    jour = models.DateTimeField(blank=True, null=True)

    typedepense = models.IntegerField(blank=True, null=True)

    dateinsert = models.DateTimeField(db_column='dateInsert', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'lignedekm'





class Log(models.Model):

    date = models.DateTimeField()

    log = models.CharField(max_length=255)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'log'





class MissionetatTransition(models.Model):

    etat = models.IntegerField()

    etat_possible = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'missionetat_transition'





class Missions(models.Model):

    nummission = models.IntegerField(db_column='NumMission', primary_key=True)  # Field name made lowercase.

    delegationid = models.CharField(db_column='DelegationId', max_length=5, db_collation='utf8_general_ci')  # Field name made lowercase.

    pm = models.CharField(db_column='PM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    numpm = models.IntegerField(db_column='NumPM')  # Field name made lowercase.

    objet = models.CharField(db_column='Objet', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    filiere = models.CharField(db_column='Filiere', max_length=3, db_collation='utf8_general_ci')  # Field name made lowercase.

    fonction = models.CharField(db_column='Fonction', max_length=2, db_collation='utf8_general_ci')  # Field name made lowercase.

    missionlien = models.FloatField(db_column='MissionLien', blank=True, null=True)  # Field name made lowercase.

    monteur = models.IntegerField(db_column='Monteur', blank=True, null=True)  # Field name made lowercase.

    datedemande = models.DateTimeField(db_column='DateDemande', blank=True, null=True)  # Field name made lowercase.

    etat = models.IntegerField(db_column='Etat', blank=True, null=True)  # Field name made lowercase.

    codepays = models.CharField(db_column='CodePays', max_length=3, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    nummissionetranger = models.CharField(db_column='NumMissionEtranger', max_length=9, blank=True, null=True)  # Field name made lowercase.

    beneficiaire = models.CharField(db_column='Beneficiaire', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    persencharge = models.CharField(db_column='PersEnCharge', max_length=70, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    lieu = models.CharField(db_column='Lieu', max_length=140, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    datedebut = models.DateTimeField(db_column='DateDebut', blank=True, null=True)  # Field name made lowercase.

    datefin = models.DateTimeField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.

    nbjoursestimesfrance = models.FloatField(db_column='NbJoursEstimesFrance', blank=True, null=True)  # Field name made lowercase.

    nbjoursestimesetranger = models.FloatField(db_column='NbJoursEstimesEtranger', blank=True, null=True)  # Field name made lowercase.

    expertprincipal = models.IntegerField(db_column='ExpertPrincipal', blank=True, null=True)  # Field name made lowercase.

    fraisvoyage = models.IntegerField(db_column='FraisVoyage', blank=True, null=True)  # Field name made lowercase.

    fraislocaux = models.IntegerField(db_column='FraisLocaux', blank=True, null=True)  # Field name made lowercase.

    montantpfg = models.FloatField(db_column='MontantPFG', blank=True, null=True)  # Field name made lowercase.

    tauxtvapfg = models.FloatField(db_column='TauxTVAPFG', blank=True, null=True)  # Field name made lowercase.

    codepfg = models.IntegerField(db_column='CodePFG', blank=True, null=True)  # Field name made lowercase.

    montantforfait = models.FloatField(db_column='MontantForfait', blank=True, null=True)  # Field name made lowercase.

    tauxtvaforfait = models.FloatField(db_column='TauxTVAForfait', blank=True, null=True)  # Field name made lowercase.

    dispositionsparticulieres = models.CharField(db_column='DispositionsParticulieres', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    dateredaction = models.DateTimeField(db_column='DateRedaction', blank=True, null=True)  # Field name made lowercase.

    signataireecti = models.IntegerField(db_column='SignataireECTI', blank=True, null=True)  # Field name made lowercase.

    codeadhesion1 = models.CharField(db_column='CodeAdhesion1', max_length=5, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    codeadhesion2 = models.CharField(db_column='CodeAdhesion2', max_length=5, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    codeinformatique = models.CharField(db_column='CodeInformatique', max_length=5, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    echue_set = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'missions'





class MissionsV2(models.Model):

    statut = models.IntegerField(db_column='Statut', blank=True, null=True)  # Field name made lowercase.

    nature = models.IntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.

    lucratif = models.CharField(db_column='Lucratif', max_length=1, blank=True, null=True)  # Field name made lowercase.

    montantpfg = models.FloatField(db_column='MontantPFG', blank=True, null=True)  # Field name made lowercase.

    montanttotalpfg = models.FloatField(db_column='MontantTotalPFG', blank=True, null=True)  # Field name made lowercase.

    montantfrais = models.FloatField(db_column='MontantFrais', blank=True, null=True)  # Field name made lowercase.

    montanttotalfrais = models.FloatField(db_column='MontantTotalFrais', blank=True, null=True)  # Field name made lowercase.

    contrat = models.CharField(db_column='Contrat', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    frais = models.CharField(db_column='Frais', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    estimationfraisdep = models.FloatField(db_column='EstimationFraisDep', blank=True, null=True)  # Field name made lowercase.

    estimationfraisdivers = models.FloatField(db_column='EstimationFraisDivers', blank=True, null=True)  # Field name made lowercase.

    facturation = models.CharField(db_column='Facturation', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    frais_nbjour = models.IntegerField(db_column='Frais_Nbjour', blank=True, null=True)  # Field name made lowercase.

    montantindemnite = models.FloatField(db_column='MontantIndemnite', blank=True, null=True)  # Field name made lowercase.

    montantindemnitedivers = models.FloatField(db_column='MontantIndemniteDivers', blank=True, null=True)  # Field name made lowercase.

    frais_visa = models.IntegerField(db_column='Frais_Visa', blank=True, null=True)  # Field name made lowercase.

    frais_billetavion = models.IntegerField(db_column='Frais_BilletAvion', blank=True, null=True)  # Field name made lowercase.

    frais_approche = models.IntegerField(db_column='Frais_Approche', blank=True, null=True)  # Field name made lowercase.

    frais_accueil = models.IntegerField(db_column='Frais_Accueil', blank=True, null=True)  # Field name made lowercase.

    frais_sejour = models.IntegerField(db_column='Frais_Sejour', blank=True, null=True)  # Field name made lowercase.

    frais_indemnite = models.IntegerField(db_column='Frais_Indemnite', blank=True, null=True)  # Field name made lowercase.

    frais_indemnitedivers = models.IntegerField(db_column='Frais_IndemniteDivers', blank=True, null=True)  # Field name made lowercase.

    frais_reglepardemandeur = models.IntegerField(db_column='Frais_RegleParDemandeur', blank=True, null=True)  # Field name made lowercase.

    frais_professionnel = models.IntegerField(db_column='Frais_Professionnel', blank=True, null=True)  # Field name made lowercase.

    taux_kmhaut = models.FloatField(db_column='Taux_KmHaut')  # Field name made lowercase.

    taux_kmbas = models.FloatField(db_column='Taux_KmBas')  # Field name made lowercase.

    nummission = models.IntegerField(db_column='NumMission', primary_key=True)  # Field name made lowercase.

    modification = models.SmallIntegerField(db_column='Modification', blank=True, null=True)  # Field name made lowercase.

    adreshaut = models.CharField(db_column='AdresHaut', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    adresbas = models.CharField(db_column='AdresBas', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    typedocument = models.CharField(db_column='TypeDocument', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    typeenregistrement = models.CharField(db_column='TypeEnregistrement', max_length=20, blank=True, null=True)  # Field name made lowercase.

    oldtypeenregistrement = models.CharField(db_column='OldTypeEnregistrement', max_length=20, blank=True, null=True)  # Field name made lowercase.

    codeintcontrat = models.CharField(db_column='CodeIntContrat', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    codeintfrais = models.CharField(db_column='CodeIntFrais', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    codeintfacturation = models.CharField(db_column='CodeIntFacturation', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    adresville = models.CharField(db_column='AdresVille', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    adrescp = models.CharField(db_column='AdresCP', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    adrespays = models.CharField(db_column='AdresPays', max_length=5, blank=True, null=True)  # Field name made lowercase.

    adrestel = models.CharField(db_column='AdresTel', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    adresemail = models.CharField(db_column='AdresEmail', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    correction = models.IntegerField(blank=True, null=True)

    datecontact = models.DateTimeField(db_column='DateContact', blank=True, null=True)  # Field name made lowercase.

    comindemnite = models.CharField(db_column='ComIndemnite', max_length=255, blank=True, null=True)  # Field name made lowercase.

    comindemnitedivers = models.CharField(db_column='ComIndemniteDivers', max_length=255, blank=True, null=True)  # Field name made lowercase.

    combilletsavion = models.CharField(db_column='ComBilletsAvion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    comfraisapproche = models.CharField(db_column='ComFraisApproche', max_length=255, blank=True, null=True)  # Field name made lowercase.

    tradfiliere = models.CharField(db_column='TradFiliere', max_length=255, blank=True, null=True)  # Field name made lowercase.

    tradfonction = models.CharField(db_column='TradFonction', max_length=255, blank=True, null=True)  # Field name made lowercase.

    tradstatut = models.CharField(db_column='TradStatut', max_length=255, blank=True, null=True)  # Field name made lowercase.

    tradnature = models.CharField(db_column='TradNature', max_length=255, blank=True, null=True)  # Field name made lowercase.

    monnaie = models.CharField(db_column='Monnaie', max_length=100, blank=True, null=True)  # Field name made lowercase.

    pmdemandeur = models.CharField(db_column='PMDemandeur', max_length=100, blank=True, null=True)  # Field name made lowercase.

    adresdemandeur = models.CharField(db_column='AdresDemandeur', max_length=255, blank=True, null=True)  # Field name made lowercase.

    adresvilledemandeur = models.CharField(db_column='AdresVilleDemandeur', max_length=255, blank=True, null=True)  # Field name made lowercase.

    adrescpdemandeur = models.CharField(db_column='AdresCPDemandeur', max_length=45, blank=True, null=True)  # Field name made lowercase.

    partenariat = models.IntegerField(db_column='Partenariat', blank=True, null=True)  # Field name made lowercase.

    emailcompta = models.CharField(db_column='EmailCompta', max_length=160, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'missions_v2'





class Missionsetat(models.Model):

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    nom = models.CharField(db_column='Nom', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'missionsetat'





class Motifrejet(models.Model):

    id = models.IntegerField(unique=True)

    nom = models.CharField(max_length=50, db_collation='utf8_general_ci')

    codeinterne = models.CharField(db_column='codeInterne', max_length=10, db_collation='utf8_general_ci')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'motifrejet'





class Notedefrais(models.Model):

    id = models.AutoField(primary_key=True)

    nummission = models.IntegerField(db_column='NumMission')  # Field name made lowercase.

    expert = models.IntegerField(db_column='Expert')  # Field name made lowercase.

    delegationexpertsindfforcee = models.CharField(db_column='DelegationExpertSiNDFForcee', max_length=5, blank=True, null=True)  # Field name made lowercase.

    datedebut = models.DateTimeField(db_column='DateDebut', blank=True, null=True)  # Field name made lowercase.

    datefin = models.DateTimeField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.

    nbjours = models.FloatField(db_column='NbJours', blank=True, null=True)  # Field name made lowercase.

    montantpaye = models.FloatField(db_column='MontantPaye', blank=True, null=True)  # Field name made lowercase.

    tauxkm = models.FloatField(db_column='TauxKm')  # Field name made lowercase.

    tauxkmclient = models.FloatField(db_column='TauxKmClient', blank=True, null=True)  # Field name made lowercase.

    nbkm = models.FloatField(db_column='NbKm', blank=True, null=True)  # Field name made lowercase.

    tauxkm_2roues = models.FloatField(db_column='TauxKm_2Roues', blank=True, null=True)  # Field name made lowercase.

    nbkm_2roues = models.FloatField(db_column='NbKm_2Roues', blank=True, null=True)  # Field name made lowercase.

    datesaisie = models.DateTimeField(db_column='DateSaisie', blank=True, null=True)  # Field name made lowercase.

    datepaiement = models.DateTimeField(db_column='DatePaiement', blank=True, null=True)  # Field name made lowercase.

    statut = models.IntegerField(db_column='Statut')  # Field name made lowercase.

    montanttva = models.FloatField(db_column='montantTVA', blank=True, null=True)  # Field name made lowercase.

    montanttotal = models.FloatField(db_column='montantTotal', blank=True, null=True)  # Field name made lowercase.

    montanttotalclient = models.FloatField(db_column='MontantTotalClient', blank=True, null=True)  # Field name made lowercase.

    avance = models.FloatField(db_column='Avance', blank=True, null=True)  # Field name made lowercase.

    dateavance = models.DateTimeField(db_column='DateAvance', blank=True, null=True)  # Field name made lowercase.

    montantsage = models.FloatField(db_column='MontantSage', blank=True, null=True)  # Field name made lowercase.

    tauxkm2 = models.FloatField(db_column='TauxKm2', blank=True, null=True)  # Field name made lowercase.

    tauxkm2client = models.FloatField(db_column='TauxKm2Client', blank=True, null=True)  # Field name made lowercase.

    nbkm2 = models.FloatField(db_column='NbKm2', blank=True, null=True)  # Field name made lowercase.

    tauxkm2_2roues = models.FloatField(db_column='TauxKm2_2Roues', blank=True, null=True)  # Field name made lowercase.

    nbkm2_2roues = models.FloatField(db_column='NbKm2_2Roues', blank=True, null=True)  # Field name made lowercase.

    type_ndf = models.CharField(max_length=10, blank=True, null=True)

    imputdeleg = models.IntegerField(db_column='imputDeleg', blank=True, null=True)  # Field name made lowercase.

    delegationrattachementforcee = models.IntegerField(db_column='DelegationRattachementForcee', blank=True, null=True)  # Field name made lowercase.

    controlesecretariat = models.IntegerField(db_column='controleSecretariat', blank=True, null=True)  # Field name made lowercase.

    controlepar = models.IntegerField(db_column='controlePar', blank=True, null=True)  # Field name made lowercase.

    datemodifstatut = models.DateTimeField(db_column='DateModifStatut', blank=True, null=True)  # Field name made lowercase.

    modifparstatut = models.IntegerField(db_column='ModifParStatut', blank=True, null=True)  # Field name made lowercase.

    tva = models.IntegerField(blank=True, null=True)

    commentairesirefus = models.CharField(db_column='CommentaireSiRefus', max_length=80, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefrais'





class Notedefraisjustificatifs(models.Model):

    idndf = models.IntegerField(db_column='idNdf')  # Field name made lowercase.

    type = models.CharField(max_length=255)

    originalfilename = models.CharField(db_column='originalFilename', max_length=255)  # Field name made lowercase.

    renamedfilename = models.CharField(db_column='renamedFilename', max_length=255)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraisjustificatifs'





class Notedefraisplafond(models.Model):

    typefrais = models.IntegerField(db_column='typeFrais')  # Field name made lowercase.

    typedepense = models.IntegerField(db_column='typeDepense', blank=True, null=True)  # Field name made lowercase.

    montanteuro = models.FloatField(db_column='montantEuro')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraisplafond'

        unique_together = (('typefrais', 'typedepense'),)





class Notedefraisrejet(models.Model):

    motifrejet = models.IntegerField(db_column='MotifRejet')  # Field name made lowercase.

    notedefrais = models.IntegerField(db_column='NoteDeFrais')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraisrejet'

        unique_together = (('notedefrais', 'motifrejet'),)





class Notedefraissage(models.Model):

    ligne = models.IntegerField()

    idndf = models.IntegerField(db_column='IdNdf')  # Field name made lowercase.

    codejournal = models.CharField(db_column='codeJournal', max_length=3, blank=True, null=True)  # Field name made lowercase.

    dateope = models.CharField(db_column='DateOpe', max_length=6, blank=True, null=True)  # Field name made lowercase.

    typepiece = models.CharField(db_column='typePiece', max_length=2, blank=True, null=True)  # Field name made lowercase.

    comptegeneral = models.CharField(db_column='compteGeneral', max_length=13, blank=True, null=True)  # Field name made lowercase.

    typecompte = models.CharField(db_column='typeCompte', max_length=1, blank=True, null=True)  # Field name made lowercase.

    compteaux = models.CharField(db_column='compteAux', max_length=13, blank=True, null=True)  # Field name made lowercase.

    refecriture = models.CharField(db_column='RefEcriture', max_length=13, blank=True, null=True)  # Field name made lowercase.

    libecriture = models.CharField(db_column='LibEcriture', max_length=25, blank=True, null=True)  # Field name made lowercase.

    modepaiement = models.CharField(db_column='modePaiement', max_length=1, blank=True, null=True)  # Field name made lowercase.

    dateecheance = models.CharField(db_column='dateEcheance', max_length=6, blank=True, null=True)  # Field name made lowercase.

    sens = models.CharField(max_length=1, blank=True, null=True)

    montant = models.CharField(max_length=20, blank=True, null=True)

    typeecriture = models.CharField(db_column='typeEcriture', max_length=1, blank=True, null=True)  # Field name made lowercase.

    numpiece = models.CharField(db_column='NumPiece', max_length=7, blank=True, null=True)  # Field name made lowercase.

    zonesage = models.CharField(db_column='zoneSage', max_length=26, blank=True, null=True)  # Field name made lowercase.

    codedevise = models.CharField(db_column='codeDevise', max_length=3, blank=True, null=True)  # Field name made lowercase.

    montantdevise = models.CharField(db_column='montantDevise', max_length=20, blank=True, null=True)  # Field name made lowercase.

    codedeviseecriture = models.CharField(db_column='codeDeviseEcriture', max_length=3, blank=True, null=True)  # Field name made lowercase.

    axeanalytique = models.CharField(db_column='axeAnalytique', max_length=10, blank=True, null=True)  # Field name made lowercase.

    sectionanalytique = models.CharField(db_column='sectionAnalytique', max_length=25, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraissage'





class Notedefraisstatut(models.Model):

    id = models.IntegerField(unique=True)

    nom = models.CharField(max_length=50, db_collation='utf8_general_ci')

    ordre = models.IntegerField()

    codeinterne = models.CharField(db_column='codeInterne', max_length=10, db_collation='utf8_general_ci')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraisstatut'





class Notedefraistaux(models.Model):

    idtypetaux = models.IntegerField(db_column='idTypeTaux')  # Field name made lowercase.

    datedebut = models.DateTimeField(db_column='DateDebut')  # Field name made lowercase.

    taux = models.FloatField(db_column='Taux')  # Field name made lowercase.

    datefin = models.DateTimeField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.

    seuilhaut = models.FloatField(db_column='SeuilHaut', blank=True, null=True)  # Field name made lowercase.

    tolerance = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'notedefraistaux'

        unique_together = (('idtypetaux', 'datedebut', 'taux'),)





class Partenariats(models.Model):

    nom = models.CharField(max_length=65)

    ordre = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'partenariats'





class Suivikmexpert(models.Model):

    expert = models.IntegerField(db_column='Expert')  # Field name made lowercase.

    annee = models.IntegerField(db_column='Annee')  # Field name made lowercase.

    nbkm = models.FloatField(db_column='NbKm')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'suivikmexpert'

        unique_together = (('expert', 'annee'),)





class TmpLignedefrais(models.Model):

    id = models.AutoField(primary_key=True)

    numexp = models.IntegerField(db_column='numExp')  # Field name made lowercase.

    nummission = models.IntegerField(db_column='numMission', blank=True, null=True)  # Field name made lowercase.

    imputation = models.CharField(max_length=10, blank=True, null=True)

    typedefrais = models.IntegerField()

    typedepense = models.IntegerField(blank=True, null=True)

    description = models.CharField(max_length=255, db_collation='utf8_bin', blank=True, null=True)

    montant = models.FloatField(blank=True, null=True)

    montanteuro = models.FloatField(db_column='montantEuro')  # Field name made lowercase.

    devise = models.CharField(max_length=3)

    quantite = models.IntegerField(blank=True, null=True)

    date_frais = models.DateField(blank=True, null=True)

    montant_ht = models.FloatField(blank=True, null=True)

    taux_tva = models.FloatField(blank=True, null=True)

    tva_rembourser = models.IntegerField(blank=True, null=True)

    tva_factu_ecti = models.IntegerField(blank=True, null=True)

    dateinsert = models.DateTimeField(db_column='dateInsert', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'tmp_lignedefrais'





class TmpLignedekm(models.Model):

    id = models.IntegerField()

    numexp = models.IntegerField(db_column='numExp')  # Field name made lowercase.

    nummission = models.IntegerField(db_column='numMission', blank=True, null=True)  # Field name made lowercase.

    imputation = models.CharField(max_length=10, blank=True, null=True)

    description = models.CharField(max_length=255, blank=True, null=True)

    nbkm = models.FloatField(db_column='nbKm', blank=True, null=True)  # Field name made lowercase.

    is2roues = models.IntegerField(db_column='Is2Roues', blank=True, null=True)  # Field name made lowercase.

    jour = models.DateTimeField(blank=True, null=True)

    typedepense = models.IntegerField(blank=True, null=True)

    dateinsert = models.DateTimeField(blank=True, null=True)



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'tmp_lignedekm'





class TmpNotedefraissage(models.Model):

    ligne = models.IntegerField()

    idndf = models.IntegerField(db_column='IdNdf')  # Field name made lowercase.

    codejournal = models.CharField(db_column='codeJournal', max_length=3, blank=True, null=True)  # Field name made lowercase.

    dateope = models.CharField(db_column='DateOpe', max_length=6, blank=True, null=True)  # Field name made lowercase.

    typepiece = models.CharField(db_column='typePiece', max_length=2, blank=True, null=True)  # Field name made lowercase.

    comptegeneral = models.CharField(db_column='compteGeneral', max_length=13, blank=True, null=True)  # Field name made lowercase.

    typecompte = models.CharField(db_column='typeCompte', max_length=1, blank=True, null=True)  # Field name made lowercase.

    compteaux = models.CharField(db_column='compteAux', max_length=13, blank=True, null=True)  # Field name made lowercase.

    refecriture = models.CharField(db_column='RefEcriture', max_length=13, blank=True, null=True)  # Field name made lowercase.

    libecriture = models.CharField(db_column='LibEcriture', max_length=25, blank=True, null=True)  # Field name made lowercase.

    modepaiement = models.CharField(db_column='modePaiement', max_length=1, blank=True, null=True)  # Field name made lowercase.

    dateecheance = models.CharField(db_column='dateEcheance', max_length=6, blank=True, null=True)  # Field name made lowercase.

    sens = models.CharField(max_length=1, blank=True, null=True)

    montant = models.CharField(max_length=20, blank=True, null=True)

    typeecriture = models.CharField(db_column='typeEcriture', max_length=1, blank=True, null=True)  # Field name made lowercase.

    numpiece = models.CharField(db_column='NumPiece', max_length=7, blank=True, null=True)  # Field name made lowercase.

    zonesage = models.CharField(db_column='zoneSage', max_length=26, blank=True, null=True)  # Field name made lowercase.

    codedevise = models.CharField(db_column='codeDevise', max_length=3, blank=True, null=True)  # Field name made lowercase.

    montantdevise = models.CharField(db_column='montantDevise', max_length=20, blank=True, null=True)  # Field name made lowercase.

    codedeviseecriture = models.CharField(db_column='codeDeviseEcriture', max_length=3, blank=True, null=True)  # Field name made lowercase.

    axeanalytique = models.CharField(db_column='axeAnalytique', max_length=10, blank=True, null=True)  # Field name made lowercase.

    sectionanalytique = models.CharField(db_column='sectionAnalytique', max_length=25, blank=True, null=True)  # Field name made lowercase.

    numexp = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'tmp_notedefraissage'





class Typedefrais(models.Model):

    label = models.CharField(max_length=255)

    ordre = models.IntegerField(blank=True, null=True)

    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    tva = models.IntegerField()



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'typedefrais'





class Typedepense(models.Model):

    id = models.IntegerField(unique=True)

    nom = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)

    codeinterne = models.CharField(db_column='codeInterne', max_length=10, db_collation='utf8_general_ci')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'typedepense'





class Typedetaux(models.Model):

    id = models.IntegerField(unique=True)

    nom = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)

    codeinterne = models.CharField(db_column='codeInterne', max_length=15, db_collation='utf8_general_ci')  # Field name made lowercase.



    class Meta:
        app_label = 'ecti'

        managed = False

        db_table = 'typedetaux'



