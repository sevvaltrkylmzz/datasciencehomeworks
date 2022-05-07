data{
    int<lower=0> N;
    vector[N] x;
    vector[N] y;
}

parameters{
    real alpha;
    real beta;
    real<lower=0,upper=50> sigma;
}

model{
    vector[346] mu;

    alpha ~ normal( 178 , 20 );
    beta ~ normal( 0 , 10 );
    sigma ~ uniform( 0 , 50 );

    for ( i in 1:346 ) {
        mu[i] = alpha + beta * x[i];
    }

    y ~ normal(alpha + beta * x, sigma);
}