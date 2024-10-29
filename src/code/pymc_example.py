with infer.model(model, unconstr_priors, data):
    post_data = pymc.sample(draws=10_000, chains=1)
    post_pred = pymc.sample_posterior_predictive(post_data)
    prior_pred = pymc.sample_prior_predictive(10_000)
