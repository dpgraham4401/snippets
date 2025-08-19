package org.vimpiarte.store.basicBeans;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

//@Service("paypal")
public class PaypalPaymentService implements PaymentService {

    /**
     * Bean lifecycle hooks.
     * <p>
     * Spring offers a few annotations that we can use to hook into the
     * lifecycle of the beans. Some common annotations include
     * - @PostConstruct --> after the constructor
     * - @PreDestroy
     * <p>
     * The name of this method doesn't, just that we apply the annotation.
     *
     */
    @PostConstruct
    public void init() {
        System.out.println("PayPal paypal service created");
    }


    /**
     * Useful if we need to release resources like files, database connections, etc.
     */
    @PreDestroy
    public void cleanup() {
        System.out.println("PayPal paypal pre-destroy");
    }

    @Override
    public void processPayment(double amount) {
        System.out.println("PayPal");
        System.out.println("Amount " + amount);
    }
}
