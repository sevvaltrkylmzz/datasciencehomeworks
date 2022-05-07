data{
    int<lower=0> N;
    vector[N] y;
    vector[N] x;
}

parameters{
    real beta1;
    real beta2;
    real beta3;
    real<lower=0,upper=50> sigma;
}

model{
    vector[N] mu;

    sigma ~ uniform( 0 , 50 );
    beta1 ~ normal( 178 , 20 );
    beta2 ~ normal( 0 , 10 );
    beta3 ~ normal( 0 , 10 );

    for ( i in 1:N ) {
        mu[i] = beta1 +  beta2 * x[i] + beta3 * x[i] *x[i];
    }

    y  ~ normal(mu, sigma);
}