package org.vimpiarte.store.services;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

/**
 * If we're using dependency injection with an interface, and have multiple
 * classes that implement that interface, we need to either
 * 1. specify a default bean (using the @Primary bean)
 * 2. specify which bean in the constructor.
 */
@Service("stripe")
@Primary
public class StripePaymentService implements PaymentService {
    @Override
    public void processPayment(double amount) {
        System.out.println("Stripe");
        System.out.println("Amount " + amount);
    }
}
