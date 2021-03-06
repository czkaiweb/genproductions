import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PyquenDefaultSettings_cff import *
from GeneratorInterface.HiGenCommon.upsilon1sMuMuTrigSettings_cff import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
                        upsilon1sMuMuTrigCommon,
                        collisionParameters2760GeV,
                        qgpParameters,
                        pyquenParameters,
                        doQuench = cms.bool(False),
                        bFixed = cms.double(0.0), ## fixed impact param (fm); valid only if cflag_=0
                        cFlag = cms.int32(0), ## centrality flag
                        bMin = cms.double(0.0), ## min impact param (fm); valid only if cflag_!=0
                        bMax = cms.double(0.0), ## max impact param (fm); valid only if cflag_!=0
                        ExternalDecays = cms.PSet(EvtGen = cms.untracked.PSet(use_internal_pythia = cms.untracked.bool(False),
                                                                              operates_on_particles = cms.vint32( 100553 ), # 0 (zero) means default list (hardcoded)
                                                                              # you can put here the list of particles (PDG IDs)
                                                                              # that you want decayed by EvtGen
                                                                              use_default_decay = cms.untracked.bool(False),
                                                                              decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
                                                                              particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
                                                                              user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Onia_mumu.dec'),
                                                                              list_forced_decays = cms.vstring('MyUpsilon(2S)'),
                                                                              ),
                                                  parameterSets = cms.vstring('EvtGen')
                                                  ),
                        PythiaParameters = cms.PSet(pyquenPythiaDefaultBlock,
                                                    kinematics = cms.vstring ("CKIN(7)=-3.0",  #min rapidity
                                                                              "CKIN(8)= 3.0"    #max rapidity
                                                                              ),
                                                    pythiaNRQCD = cms.vstring('MSEL=62          ! Quarkonia NRQCD ', 
                                                                              'KFPR(461,1)  = 100553     ! change 461 to Upsilon(2S) + g', 
                                                                              'PMAS(365,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
                                                                              'PMAS(366,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
                                                                              'PMAS(367,1)  = 10.0300   ! change bb~ mass larger than Upsilon(2S) 10.02330',
                                                                              'KFDP(4214,1) = 100553     ! bb~ -> Upsilon(2S)',
                                                                              'KFDP(4215,1) = 100553     ! bb~ -> Upsilon(2S)',
                                                                              'KFDP(4216,1) = 100553     ! bb~ -> Upsilon(2S)',
                                                                              'PMAS(278,1)  = 10.23250   ! change chi_0b(1P) mass to chi_0b(2P)', 
                                                                              'KFDP(1520,1) = 100553     ! chi_0b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1520)   = 0.046      ! br of chi_0b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1521)   = 0.954      ! br of chi_0b(2P) -> rndmflav rndmflavbar', 
                                                                              'PMAS(294,1)  = 10.25546   ! change chi_1b(1P) mass to chi_1b(2P)', 
                                                                              'KFDP(1565,1) = 100553     ! chi_1b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1565)   = 0.210      ! br of chi_1b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1566)   = 0.790      ! br of chi_1b(2P) -> rndmflav rndmflavbar', 
                                                                              'PMAS(148,1)  = 10.26865   ! change chi_2b(1P) mass to chi_2b(2P)', 
                                                                              'KFDP(1043,1) = 100553     ! chi_2b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1043)   = 0.162      ! br of chi_2b(2P) -> Upsilon(2S)', 
                                                                              'BRAT(1044)   = 0.838      ! br of chi_2b(2P) -> rndmflav rndmflavbar', 
                                                                              'PARP(146)=4.63   ! New values for COM matrix elements', 
                                                                              'PARP(147)=0.045  ! New values for COM matrix elements', 
                                                                              'PARP(148)=0.006  ! New values for COM matrix elements', 
                                                                              'PARP(149)=0.006  ! New values for COM matrix elements', 
                                                                              'PARP(150)=0.108  ! New values for COM matrix elements', 
                                                                              'MDME(1578,1) = 0 ! 0.014000    e-              e+', 
                                                                              'MDME(1579,1) = 0 ! 0.014000    mu-             mu+', 
                                                                              'MDME(1580,1) = 0 ! 0.014000    tau-            tau+', 
                                                                              'MDME(1581,1) = 0 ! 0.008000    d               dbar', 
                                                                              'MDME(1582,1) = 0 ! 0.024000    u               ubar', 
                                                                              'MDME(1583,1) = 0 ! 0.008000    s               sbar', 
                                                                              'MDME(1584,1) = 0 ! 0.024000    c               cbar', 
                                                                              'MDME(1585,1) = 0 ! 0.425000    g               g            g', 
                                                                              'MDME(1586,1) = 0 ! 0.020000    gamma           g            g', 
                                                                              'MDME(1587,1) = 0 ! 0.185000    Upsilon         pi+          pi-', 
                                                                              'MDME(1588,1) = 0 ! 0.088000    Upsilon         pi0          pi0', 
                                                                              'MDME(1589,1) = 0 ! 0.043000    chi_0b          gamma', 
                                                                              'MDME(1590,1) = 0 ! 0.067000    chi_1b          gamma', 
                                                                              'MDME(1591,1) = 0 ! 0.066000    chi_2b          gamma', 
                                                                              'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine', 
                                                                              'PARJ(13)=0.750   ! probability that a c or b meson has S=1', 
                                                                              'PARJ(14)=0.162   ! probability that a meson with S=0 is produced with L=1, J=1', 
                                                                              'PARJ(15)=0.018   ! probability that a meson with S=1 is produced with L=1, J=0', 
                                                                              'PARJ(16)=0.054   ! probability that a meson with S=1 is produced with L=1, J=1', 
                                                                              'MSTP(145)=0      ! choice of polarization', 
                                                                              'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1', 
                                                                              'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1', 
                                                                              'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !', 
                                                                              'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching'),
                                                    CSAParameters = cms.vstring('CSAMODE=6     ! cross-section reweighted quarkonia'),
                                                    parameterSets = cms.vstring('pythiaUESettings',
                                                                                'kinematics',
                                                                                'pythiaNRQCD',
                                                                                'CSAParameters'
                                                                                )
                                                    )
                        )

hiSignal.embeddingMode = True
hiSignal.hadrons      = cms.vint32(100553)
hiSignal.hadronPtMax  = cms.vdouble(30.)
hiSignal.hadronPtMin  = cms.vdouble(15.)

ProductionFilterSequence = cms.Sequence(hiSignal)
