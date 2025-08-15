package org.vimpiarte.store.services;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * If we're using dependency injection with an interface, and have multiple
 * classes that implement that interface, we need to either
 * 1. specify a default bean (using the @Primary bean)
 * 2. specify which bean in the constructor.
 * <p>
 * Reading values from externalized configuration.
 * We can use the @Value decorator to pull values from the application.properties
 */
//@Service("stripe")
//@Primary
public class StripePaymentService implements PaymentService {

    @Value("${stripe.enabled}")
    private boolean enabled;

    // We can provide default values after the `:`
    @Value("${stripe.timeout:3000}")
    private int timeout;

    @Value("${stripe.apiUrl}")
    private String apiUrl;

    // We can also have a list, which is created from the comma separated values.
    @Value("${stripe.supported-currencies}")
    private List<String> supportedCurrencies;

    @Override
    public void processPayment(double amount) {
        System.out.println("Stripe");
        System.out.println("Amount " + amount);
    }
}
