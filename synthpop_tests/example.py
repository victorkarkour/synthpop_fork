import synthpop

model = synthpop.SynthPop("config.synthpop_conf", default_config = "macy_defaults.synthpop_conf")
model.init_populations()

model.process_location(0, -6, 1.0e-3)