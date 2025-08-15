package org.vimpiarte.store.services;

import org.springframework.stereotype.Service;

//@Service("paypal")
public class PaypalPaymentService implements PaymentService {
    @Override
    public void processPayment(double amount) {
        System.out.println("PayPal");
        System.out.println("Amount " + amount);
    }
}
