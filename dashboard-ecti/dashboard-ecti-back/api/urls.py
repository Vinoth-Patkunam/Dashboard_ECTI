from rest_framework.routers import DefaultRouter
from .views import (
    AffectationsViewSet,
    CategorielucrativeViewSet,
    ConventionfiliereViewSet,
    ConventionfonctionViewSet,
    ConventionnatureViewSet,
    ConventionstatutViewSet,
    ConventionsuivieditionViewSet,
    CorrespdelegsageViewSet,
    CorrespfichierViewSet,
    CvViewSet,
    CvnewViewSet,
    DepdelViewSet,
    DeviseViewSet,
    EntgeoViewSet,
    ExpertmissionViewSet,
    FeedbackConsultantViewSet,
    FeedbackFollowupViewSet,
    FeedbackInfoViewSet,
    FilieresViewSet,
    FonctionViewSet,
    GroudelViewSet,
    HistoriquesageViewSet,
    ImputationcomptablendfViewSet,
    ImputationcomptablendfiViewSet,
    LanguesViewSet,
    LignedefraisViewSet,
    LignedekmViewSet,
    LogViewSet,
    MissionetatTransitionViewSet,
    MissionsViewSet,
    MissionsV2ViewSet,
    MissionsetatViewSet,
    MontantcotisationsanneeViewSet,
    MotifrejetViewSet,
    Naf24ViewSet,
    Naf25ViewSet,
    NafCode1ViewSet,
    NafCode2ViewSet,
    NafRev2ViewSet,
    NotedefraisViewSet,
    NotedefraisjustificatifsViewSet,
    NotedefraisplafondViewSet,
    NotedefraisrejetViewSet,
    NotedefraissageViewSet,
    NotedefraisstatutViewSet,
    NotedefraistauxViewSet,
    ParametresViewSet,
    PartenariatsViewSet,
    ServicesViewSet,
    StatmisViewSet,
    StatuttiersViewSet,
    SuivikmexpertViewSet,
    TAdressViewSet,
    TAffversViewSet,
    TContactViewSet,
    TCorrespViewSet,
    TCotiViewSet,
    TErreurmailViewSet,
    TEtacivilViewSet,
    TExpertViewSet,
    TExprintViewSet,
    TFormViewSet,
    TLangViewSet,
    TLienpersoViewSet,
    TLienservViewSet,
    TServicescourrielsViewSet,
    TSituViewSet,
    TTvaViewSet,
    TValidationexpViewSet,
    TVersprvViewSet,
    TVersrelViewSet,
    TauxtvasituViewSet,
    TcAdressViewSet,
    TcBankViewSet,
    TcCatgorieViewSet,
    TcCatgorieViewSet,
    TcCodpostalViewSet,
    TcConnuViewSet,
    TcCotisViewSet,
    TcDepViewSet,
    TcDureViewSet,
    TcEffectifViewSet,
    TcFonctionViewSet,
    TcFormViewSet,
    TcInforViewSet,
    TcLangViewSet,
    TcNatversViewSet,
    TcPayeurViewSet,
    TcPaysViewSet,
    TcPosViewSet,
    TcSituViewSet,
    TcSpeViewSet,
    TcSuiviViewSet,
    TcTitreViewSet,
    TcTrancaViewSet,
    TcTypservViewSet,
    TciChampsrViewSet,
    TelechargementViewSet,
    TiAdhViewSet,
    TiAppelprpaViewSet,
    TiAppelquestViewSet,
    TiCommetiersViewSet,
    TiComspeViewSet,
    TiCoti1ViewSet,
    TiCoti2ViewSet,
    TiCoti3ViewSet,
    TiCourrielversdlgViewSet,
    TiDeptViewSet,
    TiDpassvalidViewSet,
    TiInterViewSet,
    TiLangViewSet,
    TiLang1ViewSet,
    TiLexpViewSet,
    TiListpmViewSet,
    TiMailViewSet,
    TiMissiondpassvalidViewSet,
    TiParamViewSet,
    TiPmnonenrgleViewSet,
    TiRenouvellementCotiViewSet,
    TiStatutexperttoupdtViewSet,
    TiTabexpViewSet,
    TiVisexpViewSet,
    TmpLignedefraisViewSet,
    TmpLignedekmViewSet,
    TmpNotedefraissageViewSet,
    TypedefraisViewSet,
    TypedepenseViewSet,
    TypedetauxViewSet,
)

router = DefaultRouter()
router.register(r'affectations', AffectationsViewSet, basename='affectations')
router.register(r'categorielucratives', CategorielucrativeViewSet, basename='categorielucratives')
router.register(r'conventionfilieres', ConventionfiliereViewSet, basename='conventionfilieres')
router.register(r'conventionfonctions', ConventionfonctionViewSet, basename='conventionfonctions')
router.register(r'conventionnatures', ConventionnatureViewSet, basename='conventionnatures')
router.register(r'conventionstatuts', ConventionstatutViewSet, basename='conventionstatuts')
router.register(r'conventionsuivieditions', ConventionsuivieditionViewSet, basename='conventionsuivieditions')
router.register(r'correspdelegsages', CorrespdelegsageViewSet, basename='correspdelegsages')
router.register(r'correspfichiers', CorrespfichierViewSet, basename='correspfichiers')
router.register(r'cvs', CvViewSet, basename='cvs')
router.register(r'cvnews', CvnewViewSet, basename='cvnews')
router.register(r'depdels', DepdelViewSet, basename='depdels')
router.register(r'devises', DeviseViewSet, basename='devises')
router.register(r'entgeos', EntgeoViewSet, basename='entgeos')
router.register(r'expertmissions', ExpertmissionViewSet, basename='expertmissions')
router.register(r'feedbackconsultants', FeedbackConsultantViewSet, basename='feedbackconsultants')
router.register(r'feedbackfollowups', FeedbackFollowupViewSet, basename='feedbackfollowups')
router.register(r'feedbackinfos', FeedbackInfoViewSet, basename='feedbackinfos')
router.register(r'filieress', FilieresViewSet, basename='filieress')
router.register(r'fonctions', FonctionViewSet, basename='fonctions')
router.register(r'groudels', GroudelViewSet, basename='groudels')
router.register(r'historiquesages', HistoriquesageViewSet, basename='historiquesages')
router.register(r'imputationcomptablendfs', ImputationcomptablendfViewSet, basename='imputationcomptablendfs')
router.register(r'imputationcomptablendfis', ImputationcomptablendfiViewSet, basename='imputationcomptablendfis')
router.register(r'languess', LanguesViewSet, basename='languess')
router.register(r'lignedefrais', LignedefraisViewSet, basename='lignedefrais')
router.register(r'lignedekms', LignedekmViewSet, basename='lignedekms')
router.register(r'logs', LogViewSet, basename='logs')
router.register(r'missionetattransitions', MissionetatTransitionViewSet, basename='missionetattransitions')
router.register(r'missionss', MissionsViewSet, basename='missionss')
router.register(r'missionsv2s', MissionsV2ViewSet, basename='missionsv2s')
router.register(r'missionsetats', MissionsetatViewSet, basename='missionsetats')
router.register(r'montantcotisationsannees', MontantcotisationsanneeViewSet, basename='montantcotisationsannees')
router.register(r'motifrejets', MotifrejetViewSet, basename='motifrejets')
router.register(r'naf24s', Naf24ViewSet, basename='naf24s')
router.register(r'naf25s', Naf25ViewSet, basename='naf25s')
router.register(r'nafcode1s', NafCode1ViewSet, basename='nafcode1s')
router.register(r'nafcode2s', NafCode2ViewSet, basename='nafcode2s')
router.register(r'nafrev2s', NafRev2ViewSet, basename='nafrev2s')
router.register(r'notedefrais', NotedefraisViewSet, basename='notedefrais')
router.register(r'notedefraisjustificatifs', NotedefraisjustificatifsViewSet, basename='notedefraisjustificatifs')
router.register(r'notedefraisplafonds', NotedefraisplafondViewSet, basename='notedefraisplafonds')
router.register(r'notedefraisrejets', NotedefraisrejetViewSet, basename='notedefraisrejets')
router.register(r'notedefraissages', NotedefraissageViewSet, basename='notedefraissages')
router.register(r'notedefraisstatuts', NotedefraisstatutViewSet, basename='notedefraisstatuts')
router.register(r'notedefraistauxs', NotedefraistauxViewSet, basename='notedefraistauxs')
router.register(r'parametress', ParametresViewSet, basename='parametress')
router.register(r'partenariats', PartenariatsViewSet, basename='partenariatss')
router.register(r'servicess', ServicesViewSet, basename='servicess')
router.register(r'statmiss', StatmisViewSet, basename='statmiss')
router.register(r'statuttierss', StatuttiersViewSet, basename='statuttierss')
router.register(r'suivikmexperts', SuivikmexpertViewSet, basename='suivikmexperts')
router.register(r'tadresss', TAdressViewSet, basename='tadresss')
router.register(r'taffverss', TAffversViewSet, basename='taffverss')
router.register(r'tcontacts', TContactViewSet, basename='tcontacts')
router.register(r'tcorresps', TCorrespViewSet, basename='tcorresps')
router.register(r'tcotis', TCotiViewSet, basename='tcotis')
router.register(r'terreurmails', TErreurmailViewSet, basename='terreurmails')
router.register(r'tetacivils', TEtacivilViewSet, basename='tetacivils')
router.register(r'texperts', TExpertViewSet, basename='texperts')
router.register(r'texprints', TExprintViewSet, basename='texprints')
router.register(r'tforms', TFormViewSet, basename='tforms')
router.register(r'tlangs', TLangViewSet, basename='tlangs')
router.register(r'tlienpersos', TLienpersoViewSet, basename='tlienpersos')
router.register(r'tlienservs', TLienservViewSet, basename='tlienservs')
router.register(r'tservicescourrielss', TServicescourrielsViewSet, basename='tservicescourrielss')
router.register(r'tsitus', TSituViewSet, basename='tsitus')
router.register(r'ttvas', TTvaViewSet, basename='ttvas')
router.register(r'tvalidationexps', TValidationexpViewSet, basename='tvalidationexps')
router.register(r'tversprvs', TVersprvViewSet, basename='tversprvs')
router.register(r'tversrels', TVersrelViewSet, basename='tversrels')
router.register(r'tauxtvasitus', TauxtvasituViewSet, basename='tauxtvasitus')
router.register(r'tcadresss', TcAdressViewSet, basename='tcadresss')
router.register(r'tcbanks', TcBankViewSet, basename='tcbanks')
router.register(r'tccatgories', TcCatgorieViewSet, basename='tccatgories')
router.register(r'tccodpostals', TcCodpostalViewSet, basename='tccodpostals')
router.register(r'tcconnus', TcConnuViewSet, basename='tcconnus')
router.register(r'tccotiss', TcCotisViewSet, basename='tccotiss')
router.register(r'tcdeps', TcDepViewSet, basename='tcdeps')
router.register(r'tcdures', TcDureViewSet, basename='tcdures')
router.register(r'tceffectifs', TcEffectifViewSet, basename='tceffectifs')
router.register(r'tcfonctions', TcFonctionViewSet, basename='tcfonctions')
router.register(r'tcforms', TcFormViewSet, basename='tcforms')
router.register(r'tcinfors', TcInforViewSet, basename='tcinfors')
router.register(r'tclangs', TcLangViewSet, basename='tclangs')
router.register(r'tcnatverss', TcNatversViewSet, basename='tcnatverss')
router.register(r'tcpayeurs', TcPayeurViewSet, basename='tcpayeurs')
router.register(r'tcpayss', TcPaysViewSet, basename='tcpayss')
router.register(r'tcposs', TcPosViewSet, basename='tcposs')
router.register(r'tcsitus', TcSituViewSet, basename='tcsitus')
router.register(r'tcspes', TcSpeViewSet, basename='tcspes')
router.register(r'tcsuivis', TcSuiviViewSet, basename='tcsuivis')
router.register(r'tctitres', TcTitreViewSet, basename='tctitres')
router.register(r'tctrancas', TcTrancaViewSet, basename='tctrancas')
router.register(r'tctypservs', TcTypservViewSet, basename='tctypservs')
router.register(r'tcichampsrs', TciChampsrViewSet, basename='tcichampsrs')
router.register(r'telechargements', TelechargementViewSet, basename='telechargements')
router.register(r'tiadhs', TiAdhViewSet, basename='tiadhs')
router.register(r'tiappelprpas', TiAppelprpaViewSet, basename='tiappelprpas')
router.register(r'tiappelquests', TiAppelquestViewSet, basename='tiappelquests')
router.register(r'ticommetierss', TiCommetiersViewSet, basename='ticommetierss')
router.register(r'ticomspes', TiComspeViewSet, basename='ticomspes')
router.register(r'ticoti1s', TiCoti1ViewSet, basename='ticoti1s')
router.register(r'ticoti2s', TiCoti2ViewSet, basename='ticoti2s')
router.register(r'ticoti3s', TiCoti3ViewSet, basename='ticoti3s')
router.register(r'ticourrielversdlgs', TiCourrielversdlgViewSet, basename='ticourrielversdlgs')
router.register(r'tidepts', TiDeptViewSet, basename='tidepts')
router.register(r'tidpassvalids', TiDpassvalidViewSet, basename='tidpassvalids')
router.register(r'tiinters', TiInterViewSet, basename='tiinters')
router.register(r'tilangs', TiLangViewSet, basename='tilangs')
router.register(r'tilang1s', TiLang1ViewSet, basename='tilang1s')
router.register(r'tilexps', TiLexpViewSet, basename='tilexps')
router.register(r'tilistpms', TiListpmViewSet, basename='tilistpms')
router.register(r'timails', TiMailViewSet, basename='timails')
router.register(r'timissiondpassvalids', TiMissiondpassvalidViewSet, basename='timissiondpassvalids')
router.register(r'tiparams', TiParamViewSet, basename='tiparams')
router.register(r'tipmnonenrgles', TiPmnonenrgleViewSet, basename='tipmnonenrgles')
router.register(r'tirenouvellementcotis', TiRenouvellementCotiViewSet, basename='tirenouvellementcotis')
router.register(r'tistatutexperttoupdts', TiStatutexperttoupdtViewSet, basename='tistatutexperttoupdts')
router.register(r'titabexps', TiTabexpViewSet, basename='titabexps')
router.register(r'tivisexps', TiVisexpViewSet, basename='tivisexps')
router.register(r'tmplignedefraiss', TmpLignedefraisViewSet, basename='tmplignedefraiss')
router.register(r'tmplignedekms', TmpLignedekmViewSet, basename='tmplignedekms')
router.register(r'tmpnotedefraissages', TmpNotedefraissageViewSet, basename='tmpnotedefraissages')
router.register(r'typedefraiss', TypedefraisViewSet, basename='typedefraiss')
router.register(r'typedepenses', TypedepenseViewSet, basename='typedepenses')
router.register(r'typedetauxs', TypedetauxViewSet, basename='typedetauxs')

urlpatterns = router.urls
