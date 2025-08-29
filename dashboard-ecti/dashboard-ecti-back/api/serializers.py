from rest_framework import serializers

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


from rest_framework import serializers
from .models_tablecti import Affectations

class AffectationsSerializer(serializers.ModelSerializer):
    CodeServA  = serializers.CharField(source='codeserva')
    ExtenA     = serializers.CharField(source='extena')
    IndiceA    = serializers.IntegerField(source='indicea', required=False)
    Code3A     = serializers.CharField(source='code3a')
    Depar      = serializers.CharField(source='depar')
    CodPos     = serializers.CharField(source='codpos')
    DatOuvL    = serializers.DateTimeField(source='datouvl')
    DatOuvAff  = serializers.DateTimeField(source='datouvaff')
    DatClotAff = serializers.DateTimeField(source='datclotaff', required=False, allow_null=True)

    class Meta:
        model  = Affectations
        fields = ['CodeServA','ExtenA','IndiceA','Code3A','Depar','CodPos','DatOuvL','DatOuvAff','DatClotAff']


class CategorielucrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorielucrative
        fields = '__all__'


class ConventionfiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conventionfiliere
        fields = '__all__'


class ConventionfonctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conventionfonction
        fields = '__all__'


class ConventionnatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conventionnature
        fields = '__all__'


class ConventionstatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conventionstatut
        fields = '__all__'


class ConventionsuivieditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conventionsuiviedition
        fields = '__all__'


class CorrespdelegsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspdelegsage
        fields = '__all__'


class CorrespfichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspfichier
        fields = '__all__'


class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = '__all__'


class CvnewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cvnew
        fields = '__all__'


class DepdelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depdel
        fields = '__all__'


class DeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devise
        fields = '__all__'


class EntgeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entgeo
        fields = '__all__'


class ExpertmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertmission
        fields = '__all__'


class FeedbackConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackConsultant
        fields = '__all__'


class FeedbackFollowupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackFollowup
        fields = '__all__'


class FeedbackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackInfo
        fields = '__all__'


class FilieresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filieres
        fields = '__all__'


class FonctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonction
        fields = '__all__'


class GroudelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groudel
        fields = '__all__'


class HistoriquesageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historiquesage
        fields = '__all__'


class ImputationcomptablendfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imputationcomptablendf
        fields = '__all__'


class ImputationcomptablendfiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imputationcomptablendfi
        fields = '__all__'


class LanguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langues
        fields = '__all__'


class LignedefraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lignedefrais
        fields = '__all__'


class LignedekmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lignedekm
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class MissionetatTransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionetatTransition
        fields = '__all__'


class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = '__all__'


class MissionsV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = MissionsV2
        fields = '__all__'


class MissionsetatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missionsetat
        fields = '__all__'


class MontantcotisationsanneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montantcotisationsannee
        fields = '__all__'


class MotifrejetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motifrejet
        fields = '__all__'


class Naf24Serializer(serializers.ModelSerializer):
    class Meta:
        model = Naf24
        fields = '__all__'


class Naf25Serializer(serializers.ModelSerializer):
    class Meta:
        model = Naf25
        fields = '__all__'


class Naf25Serializer(serializers.ModelSerializer):
    class Meta:
        model = Naf25
        fields = '__all__'


class NafCode1Serializer(serializers.ModelSerializer):
    class Meta:
        model = NafCode1
        fields = '__all__'


class NafCode2Serializer(serializers.ModelSerializer):
    class Meta:
        model = NafCode2
        fields = '__all__'


class NafRev2Serializer(serializers.ModelSerializer):
    class Meta:
        model = NafRev2
        fields = '__all__'


class NotedefraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefrais
        fields = '__all__'


class NotedefraisjustificatifsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraisjustificatifs
        fields = '__all__'


class NotedefraisplafondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraisplafond
        fields = '__all__'


class NotedefraisrejetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraisrejet
        fields = '__all__'


class NotedefraissageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraissage
        fields = '__all__'


class NotedefraisstatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraisstatut
        fields = '__all__'


class NotedefraistauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notedefraistaux
        fields = '__all__'


class ParametresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametres
        fields = '__all__'


class PartenariatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenariats
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class StatmisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statmis
        fields = '__all__'


class StatuttiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuttiers
        fields = '__all__'


class SuivikmexpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suivikmexpert
        fields = '__all__'


class TAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAdress
        fields = '__all__'


class TAffversSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAffvers
        fields = '__all__'


class TContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TContact
        fields = '__all__'


class TCorrespSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCorresp
        fields = '__all__'


class TCotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCoti
        fields = '__all__'


class TErreurmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TErreurmail
        fields = '__all__'


class TEtacivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEtacivil
        fields = '__all__'


class TExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TExpert
        fields = '__all__'


class TExprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = TExprint
        fields = '__all__'


class TFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TForm
        fields = '__all__'


class TLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLang
        fields = '__all__'


class TLienpersoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLienperso
        fields = '__all__'


class TLienservSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLienserv
        fields = '__all__'


class TServicescourrielsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TServicescourriels
        fields = '__all__'


class TSituSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSitu
        fields = '__all__'


class TTvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTva
        fields = '__all__'


class TValidationexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TValidationexp
        fields = '__all__'


class TVersprvSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVersprv
        fields = '__all__'


class TVersrelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVersrel
        fields = '__all__'


class TauxtvasituSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tauxtvasitu
        fields = '__all__'


class TcAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcAdress
        fields = '__all__'


class TcBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcBank
        fields = '__all__'


class TcCatgorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcCatgorie
        fields = '__all__'


class TcCatgorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcCatgorie
        fields = '__all__'


class TcCodpostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcCodpostal
        fields = '__all__'


class TcConnuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcConnu
        fields = '__all__'


class TcCotisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcCotis
        fields = '__all__'


class TcDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcDep
        fields = '__all__'


class TcDureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcDure
        fields = '__all__'


class TcEffectifSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcEffectif
        fields = '__all__'


class TcFonctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcFonction
        fields = '__all__'


class TcFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcForm
        fields = '__all__'


class TcInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcInfor
        fields = '__all__'


class TcLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcLang
        fields = '__all__'


class TcNatversSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcNatvers
        fields = '__all__'


class TcPayeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcPayeur
        fields = '__all__'


class TcPaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcPays
        fields = '__all__'


class TcPosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcPos
        fields = '__all__'


class TcPosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcPos
        fields = '__all__'


class TcSituSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcSitu
        fields = '__all__'


class TcSpeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcSpe
        fields = '__all__'


class TcSuiviSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcSuivi
        fields = '__all__'


class TcTitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcTitre
        fields = '__all__'


class TcTrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcTranca
        fields = '__all__'


class TcTrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcTranca
        fields = '__all__'


class TcTypservSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcTypserv
        fields = '__all__'


class TcTypservSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcTypserv
        fields = '__all__'


class TciChampsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TciChampsr
        fields = '__all__'


class TelechargementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telechargement
        fields = '__all__'


class TiAdhSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiAdh
        fields = ['numexp', 'nom', 'pays', 'copos', 'emel', 'telpor']



class TiAppelprpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiAppelprpa
        fields = '__all__'


class TiAppelquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiAppelquest
        fields = '__all__'


class TiCommetiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiCommetiers
        fields = '__all__'


class TiComspeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiComspe
        fields = '__all__'


class TiCoti1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TiCoti1
        fields = '__all__'


class TiCoti2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TiCoti2
        fields = '__all__'


class TiCoti3Serializer(serializers.ModelSerializer):
    class Meta:
        model = TiCoti3
        fields = '__all__'


class TiCourrielversdlgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiCourrielversdlg
        fields = '__all__'


class TiDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiDept
        fields = '__all__'


class TiDpassvalidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiDpassvalid
        fields = '__all__'


class TiInterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiInter
        fields = '__all__'


class TiLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiLang
        fields = '__all__'


class TiLang1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TiLang1
        fields = '__all__'


class TiLexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiLexp
        fields = '__all__'


class TiListpmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiListpm
        fields = '__all__'


class TiMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiMail
        fields = '__all__'


class TiMissiondpassvalidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiMissiondpassvalid
        fields = '__all__'


class TiParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiParam
        fields = '__all__'


class TiPmnonenrgleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiPmnonenrgle
        fields = '__all__'


class TiRenouvellementCotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiRenouvellementCoti
        fields = '__all__'


class TiStatutexperttoupdtSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiStatutexperttoupdt
        fields = '__all__'


class TiTabexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiTabexp
        fields = '__all__'


class TiVisexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiVisexp
        fields = '__all__'


class TmpLignedefraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmpLignedefrais
        fields = '__all__'


class TmpLignedekmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmpLignedekm
        fields = '__all__'


class TmpNotedefraissageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmpNotedefraissage
        fields = '__all__'


class TypedefraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typedefrais
        fields = '__all__'


class TypedepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typedepense
        fields = '__all__'


class TypedetauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typedetaux
        fields = '__all__'


class TiLangSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TiLang
        fields = '__all__'
