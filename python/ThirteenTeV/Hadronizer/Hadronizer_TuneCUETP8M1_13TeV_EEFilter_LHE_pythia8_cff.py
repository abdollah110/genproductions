import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    )
    )
)

eeFilter = cms.EDFilter("LHEGenericFilter",
    src = cms.InputTag("source"),
    NumRequired = cms.int32(2),
    ParticleID = cms.vint32(11),
    AcceptLogic = cms.string("EQ") # LT meaning < NumRequired, GT >, EQ =, NE !=
)                   

ProductionFilterSequence = cms.Sequence(generator+eeFilter)
