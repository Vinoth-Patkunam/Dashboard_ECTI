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

class AffectationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Affectations.objects.all()
    serializer_class = AffectationsSerializer


class CategorielucrativeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorielucrative.objects.all()
    serializer_class = CategorielucrativeSerializer


class ConventionfiliereViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conventionfiliere.objects.all()
    serializer_class = ConventionfiliereSerializer


class ConventionfonctionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conventionfonction.objects.all()
    serializer_class = ConventionfonctionSerializer


class ConventionnatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conventionnature.objects.all()
    serializer_class = ConventionnatureSerializer


class ConventionstatutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conventionstatut.objects.all()
    serializer_class = ConventionstatutSerializer


class ConventionsuivieditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conventionsuiviedition.objects.all()
    serializer_class = ConventionsuivieditionSerializer


class CorrespdelegsageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Correspdelegsage.objects.all()
    serializer_class = CorrespdelegsageSerializer


class CorrespfichierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Correspfichier.objects.all()
    serializer_class = CorrespfichierSerializer


class CvViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cv.objects.all()
    serializer_class = CvSerializer


class CvnewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cvnew.objects.all()
    serializer_class = CvnewSerializer


class DepdelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Depdel.objects.all()
    serializer_class = DepdelSerializer


class DeviseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer


class EntgeoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entgeo.objects.all()
    serializer_class = EntgeoSerializer


class ExpertmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Expertmission.objects.all()
    serializer_class = ExpertmissionSerializer


class FeedbackConsultantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeedbackConsultant.objects.all()
    serializer_class = FeedbackConsultantSerializer


class FeedbackFollowupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeedbackFollowup.objects.all()
    serializer_class = FeedbackFollowupSerializer


class FeedbackInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeedbackInfo.objects.all()
    serializer_class = FeedbackInfoSerializer


class FilieresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filieres.objects.all()
    serializer_class = FilieresSerializer


class FonctionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fonction.objects.all()
    serializer_class = FonctionSerializer


class GroudelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Groudel.objects.all()
    serializer_class = GroudelSerializer


class HistoriquesageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historiquesage.objects.all()
    serializer_class = HistoriquesageSerializer


class ImputationcomptablendfViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Imputationcomptablendf.objects.all()
    serializer_class = ImputationcomptablendfSerializer


class ImputationcomptablendfiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Imputationcomptablendfi.objects.all()
    serializer_class = ImputationcomptablendfiSerializer


class LanguesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Langues.objects.all()
    serializer_class = LanguesSerializer


class LignedefraisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lignedefrais.objects.all()
    serializer_class = LignedefraisSerializer


class LignedekmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lignedekm.objects.all()
    serializer_class = LignedekmSerializer


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class MissionetatTransitionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MissionetatTransition.objects.all()
    serializer_class = MissionetatTransitionSerializer


class MissionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer


class MissionsV2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MissionsV2.objects.all()
    serializer_class = MissionsV2Serializer


class MissionsetatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Missionsetat.objects.all()
    serializer_class = MissionsetatSerializer


class MontantcotisationsanneeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Montantcotisationsannee.objects.all()
    serializer_class = MontantcotisationsanneeSerializer


class MotifrejetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Motifrejet.objects.all()
    serializer_class = MotifrejetSerializer


class Naf24ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Naf24.objects.all()
    serializer_class = Naf24Serializer


class Naf25ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Naf25.objects.all()
    serializer_class = Naf25Serializer


class Naf25ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Naf25.objects.all()
    serializer_class = Naf25Serializer


class NafCode1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NafCode1.objects.all()
    serializer_class = NafCode1Serializer


class NafCode2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NafCode2.objects.all()
    serializer_class = NafCode2Serializer


class NafRev2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NafRev2.objects.all()
    serializer_class = NafRev2Serializer


class NotedefraisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefrais.objects.all()
    serializer_class = NotedefraisSerializer


class NotedefraisjustificatifsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraisjustificatifs.objects.all()
    serializer_class = NotedefraisjustificatifsSerializer


class NotedefraisplafondViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraisplafond.objects.all()
    serializer_class = NotedefraisplafondSerializer


class NotedefraisrejetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraisrejet.objects.all()
    serializer_class = NotedefraisrejetSerializer


class NotedefraissageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraissage.objects.all()
    serializer_class = NotedefraissageSerializer


class NotedefraisstatutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraisstatut.objects.all()
    serializer_class = NotedefraisstatutSerializer


class NotedefraistauxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notedefraistaux.objects.all()
    serializer_class = NotedefraistauxSerializer


class ParametresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Parametres.objects.all()
    serializer_class = ParametresSerializer


class PartenariatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partenariats.objects.all()
    serializer_class = PartenariatsSerializer


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class StatmisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Statmis.objects.all()
    serializer_class = StatmisSerializer


class StatuttiersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Statuttiers.objects.all()
    serializer_class = StatuttiersSerializer


class SuivikmexpertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Suivikmexpert.objects.all()
    serializer_class = SuivikmexpertSerializer


class TAdressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TAdress.objects.all()
    serializer_class = TAdressSerializer


class TAffversViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TAffvers.objects.all()
    serializer_class = TAffversSerializer


class TContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TContact.objects.all()
    serializer_class = TContactSerializer


class TCorrespViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TCorresp.objects.all()
    serializer_class = TCorrespSerializer


class TCotiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TCoti.objects.all()
    serializer_class = TCotiSerializer


class TErreurmailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TErreurmail.objects.all()
    serializer_class = TErreurmailSerializer


class TEtacivilViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TEtacivil.objects.all()
    serializer_class = TEtacivilSerializer


class TExpertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TExpert.objects.all()
    serializer_class = TExpertSerializer


class TExprintViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TExprint.objects.all()
    serializer_class = TExprintSerializer


class TFormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TForm.objects.all()
    serializer_class = TFormSerializer


class TLangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TLang.objects.all()
    serializer_class = TLangSerializer


class TLienpersoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TLienperso.objects.all()
    serializer_class = TLienpersoSerializer


class TLienservViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TLienserv.objects.all()
    serializer_class = TLienservSerializer


class TServicescourrielsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TServicescourriels.objects.all()
    serializer_class = TServicescourrielsSerializer


class TSituViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TSitu.objects.all()
    serializer_class = TSituSerializer


class TTvaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TTva.objects.all()
    serializer_class = TTvaSerializer


class TValidationexpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TValidationexp.objects.all()
    serializer_class = TValidationexpSerializer


class TVersprvViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TVersprv.objects.all()
    serializer_class = TVersprvSerializer


class TVersrelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TVersrel.objects.all()
    serializer_class = TVersrelSerializer


class TauxtvasituViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tauxtvasitu.objects.all()
    serializer_class = TauxtvasituSerializer


class TcAdressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcAdress.objects.all()
    serializer_class = TcAdressSerializer


class TcBankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcBank.objects.all()
    serializer_class = TcBankSerializer


class TcCatgorieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcCatgorie.objects.all()
    serializer_class = TcCatgorieSerializer


class TcCatgorieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcCatgorie.objects.all()
    serializer_class = TcCatgorieSerializer


class TcCodpostalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcCodpostal.objects.all()
    serializer_class = TcCodpostalSerializer


class TcConnuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcConnu.objects.all()
    serializer_class = TcConnuSerializer


class TcCotisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcCotis.objects.all()
    serializer_class = TcCotisSerializer


class TcDepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcDep.objects.all()
    serializer_class = TcDepSerializer


class TcDureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcDure.objects.all()
    serializer_class = TcDureSerializer


class TcEffectifViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcEffectif.objects.all()
    serializer_class = TcEffectifSerializer


class TcFonctionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcFonction.objects.all()
    serializer_class = TcFonctionSerializer


class TcFormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcForm.objects.all()
    serializer_class = TcFormSerializer


class TcInforViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcInfor.objects.all()
    serializer_class = TcInforSerializer


class TcLangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcLang.objects.all()
    serializer_class = TcLangSerializer


class TcNatversViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcNatvers.objects.all()
    serializer_class = TcNatversSerializer


class TcPayeurViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcPayeur.objects.all()
    serializer_class = TcPayeurSerializer


class TcPaysViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcPays.objects.all()
    serializer_class = TcPaysSerializer


class TcPosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcPos.objects.all()
    serializer_class = TcPosSerializer


class TcPosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcPos.objects.all()
    serializer_class = TcPosSerializer


class TcSituViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcSitu.objects.all()
    serializer_class = TcSituSerializer


class TcSpeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcSpe.objects.all()
    serializer_class = TcSpeSerializer


class TcSuiviViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcSuivi.objects.all()
    serializer_class = TcSuiviSerializer


class TcTitreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcTitre.objects.all()
    serializer_class = TcTitreSerializer


class TcTrancaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcTranca.objects.all()
    serializer_class = TcTrancaSerializer


class TcTrancaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcTranca.objects.all()
    serializer_class = TcTrancaSerializer


class TcTypservViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcTypserv.objects.all()
    serializer_class = TcTypservSerializer


class TcTypservViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TcTypserv.objects.all()
    serializer_class = TcTypservSerializer


class TciChampsrViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TciChampsr.objects.all()
    serializer_class = TciChampsrSerializer


class TelechargementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Telechargement.objects.all()
    serializer_class = TelechargementSerializer


class TiAdhViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiAdh.objects.all()
    serializer_class = TiAdhSerializer


class TiAppelprpaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiAppelprpa.objects.all()
    serializer_class = TiAppelprpaSerializer


class TiAppelquestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiAppelquest.objects.all()
    serializer_class = TiAppelquestSerializer


class TiCommetiersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiCommetiers.objects.all()
    serializer_class = TiCommetiersSerializer


class TiComspeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiComspe.objects.all()
    serializer_class = TiComspeSerializer


class TiCoti1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiCoti1.objects.all()
    serializer_class = TiCoti1Serializer


class TiCoti2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiCoti2.objects.all()
    serializer_class = TiCoti2Serializer


class TiCoti3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiCoti3.objects.all()
    serializer_class = TiCoti3Serializer


class TiCourrielversdlgViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiCourrielversdlg.objects.all()
    serializer_class = TiCourrielversdlgSerializer


class TiDeptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiDept.objects.all()
    serializer_class = TiDeptSerializer


class TiDpassvalidViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiDpassvalid.objects.all()
    serializer_class = TiDpassvalidSerializer


class TiInterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiInter.objects.all()
    serializer_class = TiInterSerializer


class TiLangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiLang.objects.all()
    serializer_class = TiLangSerializer


class TiLang1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiLang1.objects.all()
    serializer_class = TiLang1Serializer


class TiLexpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiLexp.objects.all()
    serializer_class = TiLexpSerializer


class TiListpmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiListpm.objects.all()
    serializer_class = TiListpmSerializer


class TiMailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiMail.objects.all()
    serializer_class = TiMailSerializer


class TiMissiondpassvalidViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiMissiondpassvalid.objects.all()
    serializer_class = TiMissiondpassvalidSerializer


class TiParamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiParam.objects.all()
    serializer_class = TiParamSerializer


class TiPmnonenrgleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiPmnonenrgle.objects.all()
    serializer_class = TiPmnonenrgleSerializer


class TiRenouvellementCotiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiRenouvellementCoti.objects.all()
    serializer_class = TiRenouvellementCotiSerializer


class TiStatutexperttoupdtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiStatutexperttoupdt.objects.all()
    serializer_class = TiStatutexperttoupdtSerializer


class TiTabexpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiTabexp.objects.all()
    serializer_class = TiTabexpSerializer


class TiVisexpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TiVisexp.objects.all()
    serializer_class = TiVisexpSerializer


class TmpLignedefraisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TmpLignedefrais.objects.all()
    serializer_class = TmpLignedefraisSerializer


class TmpLignedekmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TmpLignedekm.objects.all()
    serializer_class = TmpLignedekmSerializer


class TmpNotedefraissageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TmpNotedefraissage.objects.all()
    serializer_class = TmpNotedefraissageSerializer


class TypedefraisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Typedefrais.objects.all()
    serializer_class = TypedefraisSerializer


class TypedepenseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Typedepense.objects.all()
    serializer_class = TypedepenseSerializer


class TypedetauxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Typedetaux.objects.all()
    serializer_class = TypedetauxSerializer


