data{
    int<lower=0> N;
    vector[N] time;
    vector[N] salary;
    vector[N] satisfactory;
}

parameters{
    real beta0;
    real beta1;
    real beta2;
    real<lower=0,upper=50> sigma;
}

model{
    vector[N] mu;

    beta0 ~ normal( 178 , 20 );
    beta1 ~ normal( 178 , 20 );
    beta2 ~ normal( 0 , 10 );
    sigma ~ uniform( 0 , 50 );

    for ( i in 1:N ) {
        mu[i] =beta0 + beta1 * time[i] + beta2 * salary[i];
    }

    satisfactory ~ normal(mu, sigma);
}