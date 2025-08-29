from rest_framework import viewsets

from .models_tablecti import Affectations
from .models_ecti import Categorielucrative
from .models_ecti import Conventionfiliere
from .models_ecti import Conventionfonction
from .models_ecti import Conventionnature
from .models_ecti import Conventionstatut
from .models_ecti import Conventionsuiviedition
from .models_ecti import Correspdelegsage
from .models_ecti import Correspfichier
from .models_infolocales import Cv
from .models_infolocales import Cvnew
from .models_tablecti import Depdel
from .models_ecti import Devise
from .models_tablecti import Entgeo
from .models_ecti import Expertmission
from .models_ecti import FeedbackConsultant
from .models_ecti import FeedbackFollowup
from .models_ecti import FeedbackInfo
from .models_tstatic import Filieres
from .models_tstatic import Fonction
from .models_tablecti import Groudel
from .models_ecti import Historiquesage
from .models_ecti import Imputationcomptablendf
from .models_ecti import Imputationcomptablendfi
from .models_infolocales import Langues
from .models_ecti import Lignedefrais
from .models_ecti import Lignedekm
from .models_ecti import Log
from .models_ecti import MissionetatTransition
from .models_ecti import Missions
from .models_ecti import MissionsV2
from .models_ecti import Missionsetat
from .models_tablecti import Montantcotisationsannee
from .models_ecti import Motifrejet
from .models_tstatic import Naf24
from .models_tablecti import Naf25
from .models_tstatic import Naf25
from .models_tstatic import NafCode1
from .models_tstatic import NafCode2
from .models_tstatic import NafRev2
from .models_ecti import Notedefrais
from .models_ecti import Notedefraisjustificatifs
from .models_ecti import Notedefraisplafond
from .models_ecti import Notedefraisrejet
from .models_ecti import Notedefraissage
from .models_ecti import Notedefraisstatut
from .models_ecti import Notedefraistaux
from .models_infolocales import Parametres
from .models_ecti import Partenariats
from .models_tablecti import Services
from .models_tablecti import Statmis
from .models_tablecti import Statuttiers
from .models_ecti import Suivikmexpert
from .models_tablecti import TAdress
from .models_tablecti import TAffvers
from .models_tstatic import TContact
from .models_tablecti import TCorresp
from .models_tablecti import TCoti
from .models_tablecti import TErreurmail
from .models_tablecti import TEtacivil
from .models_tablecti import TExpert
from .models_tablecti import TExprint
from .models_tablecti import TForm
from .models_tablecti import TLang
from .models_tablecti import TLienperso
from .models_tablecti import TLienserv
from .models_tstatic import TServicescourriels
from .models_tablecti import TSitu
from .models_tablecti import TTva
from .models_tablecti import TValidationexp
from .models_tablecti import TVersprv
from .models_tablecti import TVersrel
from .models_tablecti import Tauxtvasitu
from .models_tstatic import TcAdress
from .models_tstatic import TcBank
from .models_tablecti import TcCatgorie
from .models_tstatic import TcCatgorie
from .models_tstatic import TcCodpostal
from .models_tstatic import TcConnu
from .models_tstatic import TcCotis
from .models_tstatic import TcDep
from .models_tstatic import TcDure
from .models_tablecti import TcEffectif
from .models_tablecti import TcFonction
from .models_tablecti import TcForm
from .models_tstatic import TcInfor
from .models_tablecti import TcLang
from .models_tstatic import TcNatvers
from .models_tstatic import TcPayeur
from .models_tablecti import TcPays
from .models_tablecti import TcPos
from .models_tstatic import TcPos
from .models_tablecti import TcSitu
from .models_tablecti import TcSpe
from .models_tstatic import TcSuivi
from .models_tablecti import TcTitre
from .models_tablecti import TcTranca
from .models_tstatic import TcTranca
from .models_tablecti import TcTypserv
from .models_tstatic import TcTypserv
from .models_tablecti import TciChampsr
from .models_infolocales import Telechargement
from .models_tablecti import TiAdh
from .models_tablecti import TiAppelprpa
from .models_tablecti import TiAppelquest
from .models_tablecti import TiCommetiers
from .models_tablecti import TiComspe
from .models_tablecti import TiCoti1
from .models_tablecti import TiCoti2
from .models_tablecti import TiCoti3
from .models_tablecti import TiCourrielversdlg
from .models_tablecti import TiDept
from .models_tablecti import TiDpassvalid
from .models_tablecti import TiInter
from .models_tablecti import TiLang
from .models_tablecti import TiLang1
from .models_tablecti import TiLexp
from .models_tablecti import TiListpm
from .models_tablecti import TiMail
from .models_tablecti import TiMissiondpassvalid
from .models_tablecti import TiParam
from .models_tablecti import TiPmnonenrgle
from .models_tablecti import TiRenouvellementCoti
from .models_tablecti import TiStatutexperttoupdt
from .models_tablecti import TiTabexp
from .models_tablecti import TiVisexp
from .models_ecti import TmpLignedefrais
from .models_ecti import TmpLignedekm
from .models_ecti import TmpNotedefraissage
from .models_ecti import Typedefrais
from .models_ecti import Typedepense
from .models_ecti import Typedetaux
from .serializers import (
    AffectationsSerializer,
    CategorielucrativeSerializer,
    ConventionfiliereSerializer,
    ConventionfonctionSerializer,
    ConventionnatureSerializer,
    ConventionstatutSerializer,
    ConventionsuivieditionSerializer,
    CorrespdelegsageSerializer,
    CorrespfichierSerializer,
    CvSerializer,
    CvnewSerializer,
    DepdelSerializer,
    DeviseSerializer,
    EntgeoSerializer,
    ExpertmissionSerializer,
    FeedbackConsultantSerializer,
    FeedbackFollowupSerializer,
    FeedbackInfoSerializer,
    FilieresSerializer,
    FonctionSerializer,
    GroudelSerializer,
    HistoriquesageSerializer,
    ImputationcomptablendfSerializer,
    ImputationcomptablendfiSerializer,
    LanguesSerializer,
    LignedefraisSerializer,
    LignedekmSerializer,
    LogSerializer,
    MissionetatTransitionSerializer,
    MissionsSerializer,
    MissionsV2Serializer,
    MissionsetatSerializer,
    MontantcotisationsanneeSerializer,
    MotifrejetSerializer,
    Naf24Serializer,
    Naf25Serializer,
    Naf25Serializer,
    NafCode1Serializer,
    NafCode2Serializer,
    NafRev2Serializer,
    NotedefraisSerializer,
    NotedefraisjustificatifsSerializer,
    NotedefraisplafondSerializer,
    NotedefraisrejetSerializer,
    NotedefraissageSerializer,
    NotedefraisstatutSerializer,
    NotedefraistauxSerializer,
    ParametresSerializer,
    PartenariatsSerializer,
    ServicesSerializer,
    StatmisSerializer,
    StatuttiersSerializer,
    SuivikmexpertSerializer,
    TAdressSerializer,
    TAffversSerializer,
    TContactSerializer,
    TCorrespSerializer,
    TCotiSerializer,
    TErreurmailSerializer,
    TEtacivilSerializer,
    TExpertSerializer,
    TExprintSerializer,
    TFormSerializer,
    TLangSerializer,
    TLienpersoSerializer,
    TLienservSerializer,
    TServicescourrielsSerializer,
    TSituSerializer,
    TTvaSerializer,
    TValidationexpSerializer,
    TVersprvSerializer,
    TVersrelSerializer,
    TauxtvasituSerializer,
    TcAdressSerializer,
    TcBankSerializer,
    TcCatgorieSerializer,
    TcCatgorieSerializer,
    TcCodpostalSerializer,
    TcConnuSerializer,
    TcCotisSerializer,
    TcDepSerializer,
    TcDureSerializer,
    TcEffectifSerializer,
    TcFonctionSerializer,
    TcFormSerializer,
    TcInforSerializer,
    TcLangSerializer,
    TcNatversSerializer,
    TcPayeurSerializer,
    TcPaysSerializer,
    TcPosSerializer,
    TcPosSerializer,
    TcSituSerializer,
    TcSpeSerializer,
    TcSuiviSerializer,
    TcTitreSerializer,
    TcTrancaSerializer,
    TcTrancaSerializer,
    TcTypservSerializer,
    TcTypservSerializer,
    TciChampsrSerializer,
    TelechargementSerializer,
    TiAdhSerializer,
    TiAppelprpaSerializer,
    TiAppelquestSerializer,
    TiCommetiersSerializer,
    TiComspeSerializer,
    TiCoti1Serializer,
    TiCoti2Serializer,
    TiCoti3Serializer,
    TiCourrielversdlgSerializer,
    TiDeptSerializer,
    TiDpassvalidSerializer,
    TiInterSerializer,
    TiLangSerializer,
    TiLang1Serializer,
    TiLexpSerializer,
    TiListpmSerializer,
    TiMailSerializer,
    TiMissiondpassvalidSerializer,
    TiParamSerializer,
    TiPmnonenrgleSerializer,
    TiRenouvellementCotiSerializer,
    TiStatutexperttoupdtSerializer,
    TiTabexpSerializer,
    TiVisexpSerializer,
    TmpLignedefraisSerializer,
    TmpLignedekmSerializer,
    TmpNotedefraissageSerializer,
    TypedefraisSerializer,
    TypedepenseSerializer,
    TypedetauxSerializer,
)

from rest_framework import mixins, viewsets
from .models_tablecti import Affectations
from .serializers import AffectationsSerializer

class AffectationsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AffectationsSerializer
    def get_queryset(self):
        return Affectations.objects.using('tablecti').all()

    filterset_fields  = ['codeserva','extena','code3a','depar','codpos']
    ordering_fields   = ['datouvl','datouvaff']
    search_fields     = ['codeserva','code3a','depar','codpos']


from rest_framework import mixins, viewsets
from .models_ecti import Categorielucrative
from .serializers import CategorielucrativeSerializer

class CategorielucrativeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorielucrativeSerializer

    def get_queryset(self):
        return Categorielucrative.objects.using('ecti').all()

    filterset_fields = ['code']
    ordering_fields  = ['code', 'libelle']
    search_fields    = ['code', 'libelle']



from rest_framework import mixins, viewsets

from .models_ecti import (
    Conventionfiliere, Conventionfonction, Conventionnature, Conventionsuiviedition,
    Correspdelegsage, Correspfichier, Devise, Expertmission,
    FeedbackConsultant, FeedbackFollowup, FeedbackInfo, Conventionstatut
)
from .serializers import (
    ConventionfiliereSerializer, ConventionfonctionSerializer, ConventionnatureSerializer,
    ConventionsuivieditionSerializer, CorrespdelegsageSerializer, CorrespfichierSerializer,
    DeviseSerializer, ExpertmissionSerializer, FeedbackConsultantSerializer,
    FeedbackFollowupSerializer, FeedbackInfoSerializer, ConventionstatutSerializer
)

class BaseEctiListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('ecti').all()

class ConventionfiliereViewSet(BaseEctiListViewSet):
    queryset = Conventionfiliere.objects
    serializer_class = ConventionfiliereSerializer
    filterset_fields = ['id', 'nom']
    ordering_fields  = ['id', 'nom']
    search_fields    = ['nom']

class ConventionfonctionViewSet(BaseEctiListViewSet):
    queryset = Conventionfonction.objects
    serializer_class = ConventionfonctionSerializer
    filterset_fields = ['id', 'nom']
    ordering_fields  = ['id', 'nom']
    search_fields    = ['nom']

class ConventionnatureViewSet(BaseEctiListViewSet):
    queryset = Conventionnature.objects
    serializer_class = ConventionnatureSerializer
    filterset_fields = ['id', 'nomcategorie', 'nom', 'lucratif']
    ordering_fields  = ['id', 'nom', 'nomcategorie']
    search_fields    = ['nom', 'nomcategorie']

class ConventionstatutViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ConventionstatutSerializer
    def get_queryset(self):
        return Conventionstatut.objects.using('ecti').all()

    filterset_fields = ['id', 'nom', 'lucratif']
    ordering_fields  = ['id', 'nom']
    search_fields    = ['nom']

class ConventionsuivieditionViewSet(BaseEctiListViewSet):
    queryset = Conventionsuiviedition.objects
    serializer_class = ConventionsuivieditionSerializer
    filterset_fields = ['nummission', 'numsuivi', 'numexp']
    ordering_fields  = ['nummission', 'numsuivi', 'numexp', 'datesuivi']
    search_fields    = ['nummission']

class CorrespdelegsageViewSet(BaseEctiListViewSet):
    queryset = Correspdelegsage.objects
    serializer_class = CorrespdelegsageSerializer
    filterset_fields = ['codedeleg', 'codecomptable']
    ordering_fields  = ['codedeleg']
    search_fields    = ['codedeleg', 'nom', 'codecomptable']

class CorrespfichierViewSet(BaseEctiListViewSet):
    queryset = Correspfichier.objects
    serializer_class = CorrespfichierSerializer
    filterset_fields = ['nom', 'type']
    ordering_fields  = ['nom', 'type']
    search_fields    = ['nom', 'chemin', 'type']

class DeviseViewSet(BaseEctiListViewSet):
    queryset = Devise.objects
    serializer_class = DeviseSerializer
    filterset_fields = ['codealpha', 'pays', 'nom']
    ordering_fields  = ['codealpha', 'pays', 'nom']
    search_fields    = ['codealpha', 'pays', 'nom']

class ExpertmissionViewSet(BaseEctiListViewSet):
    queryset = Expertmission.objects
    serializer_class = ExpertmissionSerializer
    filterset_fields = ['nummission', 'numexpert']
    ordering_fields  = ['nummission', 'numexpert']
    search_fields    = ['nummission']

class FeedbackConsultantViewSet(BaseEctiListViewSet):
    queryset = FeedbackConsultant.objects
    serializer_class = FeedbackConsultantSerializer
    filterset_fields = ['mid', 'consultant_nr']
    ordering_fields  = ['mid', 'consultant_nr', 'days']
    search_fields    = ['mid']

class FeedbackFollowupViewSet(BaseEctiListViewSet):
    queryset = FeedbackFollowup.objects
    serializer_class = FeedbackFollowupSerializer
    filterset_fields = ['mid']
    ordering_fields  = ['mid']
    search_fields    = ['mid', 'c_name', 'c_info', 'c_action']

class FeedbackInfoViewSet(BaseEctiListViewSet):
    queryset = FeedbackInfo.objects
    serializer_class = FeedbackInfoSerializer
    filterset_fields = ['fb_id', 'mission_id', 'date_from', 'date_to']
    ordering_fields  = ['fb_id', 'date_from', 'date_to']
    search_fields    = ['rcp_name', 'location', 'feedback']

from rest_framework import mixins, viewsets
from .models_ecti import (
    Historiquesage, Imputationcomptablendf, Imputationcomptablendfi,
    Lignedefrais, Lignedekm, Log, MissionetatTransition, Missions
)
from .serializers import (
    HistoriquesageSerializer, ImputationcomptablendfSerializer, ImputationcomptablendfiSerializer,
    LignedefraisSerializer, LignedekmSerializer, LogSerializer, MissionetatTransitionSerializer, MissionsSerializer
)

class BaseEctiListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('ecti').all()

class HistoriquesageViewSet(BaseEctiListViewSet):
    queryset = Historiquesage.objects
    serializer_class = HistoriquesageSerializer
    ordering_fields = ['dateenvoi']; search_fields = ['nomfichier']

class ImputationcomptablendfViewSet(BaseEctiListViewSet):
    queryset = Imputationcomptablendf.objects
    serializer_class = ImputationcomptablendfSerializer
    filterset_fields = ['codecomptable','typemission','fraiscompris']; search_fields = ['libelle']

class ImputationcomptablendfiViewSet(BaseEctiListViewSet):
    queryset = Imputationcomptablendfi.objects
    serializer_class = ImputationcomptablendfiSerializer
    filterset_fields = ['codebusiness','codeanalytique','codecomptable']; search_fields = ['libellebusiness']

class LignedefraisViewSet(BaseEctiListViewSet):
    queryset = Lignedefrais.objects
    serializer_class = LignedefraisSerializer
    filterset_fields = ['idnote','typedefrais','devise','date_frais']; ordering_fields = ['date_frais','montant','montanteuro']

class LignedekmViewSet(BaseEctiListViewSet):
    queryset = Lignedekm.objects
    serializer_class = LignedekmSerializer
    filterset_fields = ['idnote','typedepense','is2roues']; ordering_fields = ['jour','nbkm']

class LogViewSet(BaseEctiListViewSet):
    queryset = Log.objects
    serializer_class = LogSerializer
    ordering_fields = ['date']; search_fields = ['log']

class MissionetatTransitionViewSet(BaseEctiListViewSet):
    queryset = MissionetatTransition.objects
    serializer_class = MissionetatTransitionSerializer
    filterset_fields = ['etat','etat_possible']

class MissionsViewSet(BaseEctiListViewSet):
    queryset = Missions.objects
    serializer_class = MissionsSerializer
    filterset_fields = ['nummission','delegationid','etat','filiere','fonction','codepays','expertprincipal']
    ordering_fields = ['nummission','datedemande','datedebut','datefin']
    search_fields = ['objet','beneficiaire','lieu','persencharge']

from rest_framework import mixins, viewsets
from .models_ecti import (
    MissionsV2, Missionsetat, Motifrejet, Notedefrais,
    Notedefraisjustificatifs, Notedefraisplafond, Notedefraisrejet, Notedefraissage
)
from .serializers import (
    MissionsV2Serializer, MissionsetatSerializer, MotifrejetSerializer, NotedefraisSerializer,
    NotedefraisjustificatifsSerializer, NotedefraisplafondSerializer,
    NotedefraisrejetSerializer, NotedefraissageSerializer
)

class BaseEctiListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('ecti').all()

class MissionsV2ViewSet(BaseEctiListViewSet):
    queryset = MissionsV2.objects
    serializer_class = MissionsV2Serializer
    filterset_fields = ['nummission', 'statut', 'nature', 'lucratif', 'facturation']
    ordering_fields  = ['nummission', 'datecontact', 'montanttotal', 'montanttotalpfg', 'montanttotalfrais']
    search_fields    = ['tradfiliere','tradfonction','tradstatut','tradnature','pmdemandeur','adresdemandeur','adresville']

class MissionsetatViewSet(BaseEctiListViewSet):
    queryset = Missionsetat.objects
    serializer_class = MissionsetatSerializer
    ordering_fields = ['position']; search_fields = ['nom']

class MotifrejetViewSet(BaseEctiListViewSet):
    queryset = Motifrejet.objects
    serializer_class = MotifrejetSerializer
    search_fields = ['nom', 'codeinterne']

class NotedefraisViewSet(BaseEctiListViewSet):
    queryset = Notedefrais.objects
    serializer_class = NotedefraisSerializer
    filterset_fields = ['id','nummission','statut','expert']
    ordering_fields  = ['datesaisie','datepaiement','montanttotal','montantpaye']
    search_fields    = ['commentairesirefus']

class NotedefraisjustificatifsViewSet(BaseEctiListViewSet):
    queryset = Notedefraisjustificatifs.objects
    serializer_class = NotedefraisjustificatifsSerializer
    filterset_fields = ['idndf','type']; search_fields = ['originalfilename','renamedfilename']

class NotedefraisplafondViewSet(BaseEctiListViewSet):
    queryset = Notedefraisplafond.objects
    serializer_class = NotedefraisplafondSerializer
    filterset_fields = ['typefrais','typedepense']

class NotedefraisrejetViewSet(BaseEctiListViewSet):
    queryset = Notedefraisrejet.objects
    serializer_class = NotedefraisrejetSerializer
    filterset_fields = ['notedefrais','motifrejet']

class NotedefraissageViewSet(BaseEctiListViewSet):
    queryset = Notedefraissage.objects
    serializer_class = NotedefraissageSerializer
    filterset_fields = ['idndf','codejournal','typepiece','codejournal']
    search_fields    = ['libecriture','refecriture','comptegeneral','compteaux']

from rest_framework import mixins, viewsets
from .models_ecti import (
    Notedefraisstatut, Notedefraistaux, Partenariats, Suivikmexpert,
    TmpLignedefrais, TmpLignedekm, TmpNotedefraissage,
    Typedefrais, Typedepense, Typedetaux
)
from .serializers import (
    NotedefraisstatutSerializer, NotedefraistauxSerializer, PartenariatsSerializer, SuivikmexpertSerializer,
    TmpLignedefraisSerializer, TmpLignedekmSerializer, TmpNotedefraissageSerializer,
    TypedefraisSerializer, TypedepenseSerializer, TypedetauxSerializer
)

class BaseEctiListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('ecti').all()

class NotedefraisstatutViewSet(BaseEctiListViewSet):
    queryset = Notedefraisstatut.objects
    serializer_class = NotedefraisstatutSerializer
    filterset_fields = ['id','ordre','codeinterne']; search_fields = ['nom']; ordering_fields = ['ordre','id']

class NotedefraistauxViewSet(BaseEctiListViewSet):
    queryset = Notedefraistaux.objects
    serializer_class = NotedefraistauxSerializer
    filterset_fields = ['idtypetaux','datedebut','taux']; ordering_fields = ['datedebut','taux']

class PartenariatsViewSet(BaseEctiListViewSet):
    queryset = Partenariats.objects
    serializer_class = PartenariatsSerializer
    ordering_fields = ['ordre']; search_fields = ['nom']

class SuivikmexpertViewSet(BaseEctiListViewSet):
    queryset = Suivikmexpert.objects
    serializer_class = SuivikmexpertSerializer
    filterset_fields = ['expert','annee']; ordering_fields = ['annee','nbkm']

class TmpLignedefraisViewSet(BaseEctiListViewSet):
    queryset = TmpLignedefrais.objects
    serializer_class = TmpLignedefraisSerializer
    filterset_fields = ['numexp','nummission','typedefrais','typedepense','devise','date_frais']
    ordering_fields = ['dateinsert','date_frais','montant','montanteuro']

class TmpLignedekmViewSet(BaseEctiListViewSet):
    queryset = TmpLignedekm.objects
    serializer_class = TmpLignedekmSerializer
    filterset_fields = ['numexp','nummission','typedepense','is2roues']
    ordering_fields = ['jour','nbkm']

class TmpNotedefraissageViewSet(BaseEctiListViewSet):
    queryset = TmpNotedefraissage.objects
    serializer_class = TmpNotedefraissageSerializer
    filterset_fields = ['idndf','codejournal','typepiece','numexp']
    search_fields = ['libecriture','refecriture','comptegeneral','compteaux']

class TypedefraisViewSet(BaseEctiListViewSet):
    queryset = Typedefrais.objects
    serializer_class = TypedefraisSerializer
    filterset_fields = ['tva','parent']; search_fields = ['label']; ordering_fields = ['ordre']

class TypedepenseViewSet(BaseEctiListViewSet):
    queryset = Typedepense.objects
    serializer_class = TypedepenseSerializer
    search_fields = ['nom','codeinterne']

class TypedetauxViewSet(BaseEctiListViewSet):
    queryset = Typedetaux.objects
    serializer_class = TypedetauxSerializer
    search_fields = ['nom','codeinterne']

from rest_framework import mixins, viewsets
from .models_infolocales import Cv, Cvnew, Langues, Parametres, Telechargement
from .serializers import (
    CvSerializer, CvnewSerializer, LanguesSerializer, ParametresSerializer, TelechargementSerializer
)

class BaseInfolocalesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('infolocales').all()

class CvViewSet(BaseInfolocalesListViewSet):
    queryset = Cv.objects
    serializer_class = CvSerializer
    filterset_fields = ['numexp','langue','typedoc']
    ordering_fields  = ['dateinser','datemodif','nbtelecharge']
    search_fields    = ['nomfichier']

class CvnewViewSet(BaseInfolocalesListViewSet):
    queryset = Cvnew.objects
    serializer_class = CvnewSerializer
    filterset_fields = ['numexp','langue','validation','nouvelleadhesion','typedoc']
    ordering_fields  = ['dateinser']
    search_fields    = ['nomfichier','commentairerefus']

class LanguesViewSet(BaseInfolocalesListViewSet):
    queryset = Langues.objects
    serializer_class = LanguesSerializer
    search_fields    = ['nom','suffixe','repertoire']

class ParametresViewSet(BaseInfolocalesListViewSet):
    queryset = Parametres.objects
    serializer_class = ParametresSerializer
    search_fields    = ['nom','valeur']

class TelechargementViewSet(BaseInfolocalesListViewSet):
    queryset = Telechargement.objects
    serializer_class = TelechargementSerializer
    filterset_fields = ['numexp']
    ordering_fields  = ['lastdate','nbcvjour','nbcvtotal']

from rest_framework import mixins, viewsets
from .models_infolocales import Cv, Cvnew, Langues, Parametres, Telechargement
from .serializers import (
    CvSerializer, CvnewSerializer, LanguesSerializer,
    ParametresSerializer, TelechargementSerializer
)

# lit sur la base 'infolocales'
class BaseInfolocalesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('infolocales').all()

class CvViewSet(BaseInfolocalesListViewSet):
    queryset = Cv.objects
    serializer_class = CvSerializer
    filterset_fields = ['numexp', 'langue', 'typedoc']
    ordering_fields  = ['dateinser', 'datemodif', 'nbtelecharge']
    search_fields    = ['nomfichier']

class CvnewViewSet(BaseInfolocalesListViewSet):
    queryset = Cvnew.objects
    serializer_class = CvnewSerializer
    filterset_fields = ['numexp', 'langue', 'validation', 'nouvelleadhesion', 'typedoc']
    ordering_fields  = ['dateinser']
    search_fields    = ['nomfichier', 'commentairerefus']

class LanguesViewSet(BaseInfolocalesListViewSet):
    queryset = Langues.objects
    serializer_class = LanguesSerializer
    search_fields    = ['nom', 'suffixe', 'repertoire']

class ParametresViewSet(BaseInfolocalesListViewSet):
    queryset = Parametres.objects
    serializer_class = ParametresSerializer
    search_fields    = ['nom', 'valeur']

class TelechargementViewSet(BaseInfolocalesListViewSet):
    queryset = Telechargement.objects
    serializer_class = TelechargementSerializer
    filterset_fields = ['numexp']
    ordering_fields  = ['lastdate', 'nbcvjour', 'nbcvtotal']

from rest_framework import mixins, viewsets
from .models_tstatic import (
    Filieres, Fonction, Naf24, Naf25, NafCode1, NafCode2, NafRev2,
    TContact, TServicescourriels, TcAdress, TcBank, TcCatgorie, TcCodpostal,
    TcConnu, TcCotis, TcDep, TcDure, TcInfor, TcNatvers, TcPayeur,
    TcPos, TcSuivi, TcTranca, TcTypserv
)
from .serializers import (
    FilieresSerializer, FonctionSerializer, Naf24Serializer, Naf25Serializer,
    NafCode1Serializer, NafCode2Serializer, NafRev2Serializer,
    TContactSerializer, TServicescourrielsSerializer, TcAdressSerializer, TcBankSerializer,
    TcCatgorieSerializer, TcCodpostalSerializer, TcConnuSerializer, TcCotisSerializer,
    TcDepSerializer, TcDureSerializer, TcInforSerializer, TcNatversSerializer, TcPayeurSerializer,
    TcPosSerializer, TcSuiviSerializer, TcTrancaSerializer, TcTypservSerializer
)

# Base: lit sur la DB 'tstatic'
class BaseTstaticListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('tstatic').all()

class FilieresViewSet(BaseTstaticListViewSet):           queryset=Filieres.objects;           serializer_class=FilieresSerializer
class FonctionViewSet(BaseTstaticListViewSet):           queryset=Fonction.objects;           serializer_class=FonctionSerializer
class Naf24ViewSet(BaseTstaticListViewSet):              queryset=Naf24.objects;              serializer_class=Naf24Serializer
class Naf25ViewSet(BaseTstaticListViewSet):              queryset=Naf25.objects;              serializer_class=Naf25Serializer
class NafCode1ViewSet(BaseTstaticListViewSet):           queryset=NafCode1.objects;           serializer_class=NafCode1Serializer
class NafCode2ViewSet(BaseTstaticListViewSet):           queryset=NafCode2.objects;           serializer_class=NafCode2Serializer
class NafRev2ViewSet(BaseTstaticListViewSet):            queryset=NafRev2.objects;            serializer_class=NafRev2Serializer
class TContactViewSet(BaseTstaticListViewSet):           queryset=TContact.objects;           serializer_class=TContactSerializer
class TServicescourrielsViewSet(BaseTstaticListViewSet): queryset=TServicescourriels.objects; serializer_class=TServicescourrielsSerializer
class TcAdressViewSet(BaseTstaticListViewSet):           queryset=TcAdress.objects;           serializer_class=TcAdressSerializer
class TcBankViewSet(BaseTstaticListViewSet):             queryset=TcBank.objects;             serializer_class=TcBankSerializer
class TcCatgorieViewSet(BaseTstaticListViewSet):         queryset=TcCatgorie.objects;         serializer_class=TcCatgorieSerializer
class TcCodpostalViewSet(BaseTstaticListViewSet):        queryset=TcCodpostal.objects;        serializer_class=TcCodpostalSerializer
class TcConnuViewSet(BaseTstaticListViewSet):            queryset=TcConnu.objects;            serializer_class=TcConnuSerializer
class TcCotisViewSet(BaseTstaticListViewSet):            queryset=TcCotis.objects;            serializer_class=TcCotisSerializer
class TcDepViewSet(BaseTstaticListViewSet):              queryset=TcDep.objects;              serializer_class=TcDepSerializer
class TcDureViewSet(BaseTstaticListViewSet):             queryset=TcDure.objects;             serializer_class=TcDureSerializer
class TcInforViewSet(BaseTstaticListViewSet):            queryset=TcInfor.objects;            serializer_class=TcInforSerializer
class TcNatversViewSet(BaseTstaticListViewSet):          queryset=TcNatvers.objects;          serializer_class=TcNatversSerializer
class TcPayeurViewSet(BaseTstaticListViewSet):           queryset=TcPayeur.objects;           serializer_class=TcPayeurSerializer
class TcPosViewSet(BaseTstaticListViewSet):              queryset=TcPos.objects;              serializer_class=TcPosSerializer
class TcSuiviViewSet(BaseTstaticListViewSet):            queryset=TcSuivi.objects;            serializer_class=TcSuiviSerializer
class TcTrancaViewSet(BaseTstaticListViewSet):           queryset=TcTranca.objects;           serializer_class=TcTrancaSerializer
class TcTypservViewSet(BaseTstaticListViewSet):          queryset=TcTypserv.objects;          serializer_class=TcTypservSerializer

from rest_framework import mixins, viewsets
from .models_tablecti import (
    Affectations, Depdel, Entgeo, Groudel, Montantcotisationsannee, Naf25, Services, Statmis, Statuttiers,
    TAdress, TAffvers, TCorresp, TCoti, TErreurmail, TEtacivil, TExpert, TExprint, TForm, TLang, TLienperso,
    TLienserv, TSitu, TTva, TValidationexp, TVersprv, TVersrel, Tauxtvasitu,
    TcCatgorie, TcEffectif, TcFonction, TcForm, TcLang, TcPays, TcPos, TcSitu, TcSpe, TcTitre, TcTranca, TcTypserv,
    TciChampsr, TiAdh, TiAppelprpa, TiAppelquest, TiCommetiers, TiComspe,
    TiCoti1, TiCoti2, TiCoti3, TiCourrielversdlg, TiDept, TiDpassvalid, TiInter,
    TiLang, TiLang1, TiLexp, TiListpm, TiMail, TiMissiondpassvalid, TiParam, TiPmnonenrgle,
    TiRenouvellementCoti, TiStatutexperttoupdt, TiTabexp, TiVisexp
)
from .serializers import *
from .models_tablecti import TiLang
from .serializers import TiLangSerializer

# base : lecture sur l'alias 'tablecti'
class BaseTableCtiListVS(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        return self.queryset.using('tablecti').all()

# une petite fabrique pour limiter le copier/coller
def make_vs(model, serializer):
    class _VS(BaseTableCtiListVS):
        queryset = model.objects
        serializer_class = serializer
    _VS.__name__ = f"{model.__name__}ViewSet"
    return _VS

AffectationsViewSet         = make_vs(Affectations, AffectationsSerializer)
DepdelViewSet               = make_vs(Depdel, DepdelSerializer)
EntgeoViewSet               = make_vs(Entgeo, EntgeoSerializer)
GroudelViewSet              = make_vs(Groudel, GroudelSerializer)
MontantcotisationsanneeViewSet = make_vs(Montantcotisationsannee, MontantcotisationsanneeSerializer)
Naf25ViewSet                = make_vs(Naf25, Naf25Serializer)
ServicesViewSet             = make_vs(Services, ServicesSerializer)
StatmisViewSet              = make_vs(Statmis, StatmisSerializer)
StatuttiersViewSet          = make_vs(Statuttiers, StatuttiersSerializer)
TAdressViewSet              = make_vs(TAdress, TAdressSerializer)
TAffversViewSet             = make_vs(TAffvers, TAffversSerializer)
TCorrespViewSet             = make_vs(TCorresp, TCorrespSerializer)
TCotiViewSet                = make_vs(TCoti, TCotiSerializer)
TErreurmailViewSet          = make_vs(TErreurmail, TErreurmailSerializer)
TEtacivilViewSet            = make_vs(TEtacivil, TEtacivilSerializer)
TExpertViewSet              = make_vs(TExpert, TExpertSerializer)
TExprintViewSet             = make_vs(TExprint, TExprintSerializer)
TFormViewSet                = make_vs(TForm, TFormSerializer)
TLangViewSet                = make_vs(TLang, TLangSerializer)
TLienpersoViewSet           = make_vs(TLienperso, TLienpersoSerializer)
TLienservViewSet            = make_vs(TLienserv, TLienservSerializer)
TSituViewSet                = make_vs(TSitu, TSituSerializer)
TTvaViewSet                 = make_vs(TTva, TTvaSerializer)
TValidationexpViewSet       = make_vs(TValidationexp, TValidationexpSerializer)
TVersprvViewSet             = make_vs(TVersprv, TVersprvSerializer)
TVersrelViewSet             = make_vs(TVersrel, TVersrelSerializer)
TauxtvasituViewSet          = make_vs(Tauxtvasitu, TauxtvasituSerializer)
TcCatgorieViewSet           = make_vs(TcCatgorie, TcCatgorieSerializer)
TcEffectifViewSet           = make_vs(TcEffectif, TcEffectifSerializer)
TcFonctionViewSet           = make_vs(TcFonction, TcFonctionSerializer)
TcFormViewSet               = make_vs(TcForm, TcFormSerializer)
TcLangViewSet               = make_vs(TcLang, TcLangSerializer)
TcPaysViewSet               = make_vs(TcPays, TcPaysSerializer)
TcPosViewSet                = make_vs(TcPos, TcPosSerializer)
TcSituViewSet               = make_vs(TcSitu, TcSituSerializer)
TcSpeViewSet                = make_vs(TcSpe, TcSpeSerializer)
TcTitreViewSet              = make_vs(TcTitre, TcTitreSerializer)
TcTrancaViewSet             = make_vs(TcTranca, TcTrancaSerializer)
TcTypservViewSet            = make_vs(TcTypserv, TcTypservSerializer)
TciChampsrViewSet           = make_vs(TciChampsr, TciChampsrSerializer)
TiAdhViewSet                = make_vs(TiAdh, TiAdhSerializer)
TiAppelprpaViewSet          = make_vs(TiAppelprpa, TiAppelprpaSerializer)
TiAppelquestViewSet         = make_vs(TiAppelquest, TiAppelquestSerializer)
TiCommetiersViewSet         = make_vs(TiCommetiers, TiCommetiersSerializer)
TiComspeViewSet             = make_vs(TiComspe, TiComspeSerializer)
TiCoti1ViewSet              = make_vs(TiCoti1, TiCoti1Serializer)
TiCoti2ViewSet              = make_vs(TiCoti2, TiCoti2Serializer)
TiCoti3ViewSet              = make_vs(TiCoti3, TiCoti3Serializer)
TiCourrielversdlgViewSet    = make_vs(TiCourrielversdlg, TiCourrielversdlgSerializer)
TiDeptViewSet               = make_vs(TiDept, TiDeptSerializer)
TiDpassvalidViewSet         = make_vs(TiDpassvalid, TiDpassvalidSerializer)
TiInterViewSet              = make_vs(TiInter, TiInterSerializer)
TiLangViewSet = make_vs(TiLang, TiLangSerializer)
TiLang1ViewSet              = make_vs(TiLang1, TiLang1Serializer)
TiLexpViewSet               = make_vs(TiLexp, TiLexpSerializer)
TiListpmViewSet             = make_vs(TiListpm, TiListpmSerializer)
TiMailViewSet               = make_vs(TiMail, TiMailSerializer)
TiMissiondpassvalidViewSet  = make_vs(TiMissiondpassvalid, TiMissiondpassvalidSerializer)
TiParamViewSet              = make_vs(TiParam, TiParamSerializer)
TiPmnonenrgleViewSet        = make_vs(TiPmnonenrgle, TiPmnonenrgleSerializer)
TiRenouvellementCotiViewSet = make_vs(TiRenouvellementCoti, TiRenouvellementCotiSerializer)
TiStatutexperttoupdtViewSet = make_vs(TiStatutexperttoupdt, TiStatutexperttoupdtSerializer)
TiTabexpViewSet             = make_vs(TiTabexp, TiTabexpSerializer)
TiVisexpViewSet             = make_vs(TiVisexp, TiVisexpSerializer)
