package org.vimpiarte.store.services;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

//@Service
public class OrderService {
    private PaymentService paymentService;


    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void placeOrder() {
        double payment = 10.0;
        paymentService.processPayment(payment);
    }
}
