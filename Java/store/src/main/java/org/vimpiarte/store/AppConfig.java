package org.vimpiarte.store;

import org.aspectj.weaver.ast.Or;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.vimpiarte.store.services.OrderService;
import org.vimpiarte.store.services.PaymentService;
import org.vimpiarte.store.services.PaypalPaymentService;
import org.vimpiarte.store.services.StripePaymentService;

/**
 * The spring bean annotations are great, but we can also configure
 * the creation of beans with Java code directly. This gives us more control
 * and allows us to create beans conditionally. Also configuring beans with 3rd-party code.
 */
@Configuration
public class AppConfig {

    @Value("${payment-gateway:stripe}")
    private String paymentGateway;

    // The name of the beans should be a noun, not a verb like `get_stripe`
    @Bean
    public PaymentService stripe() {
        // Here we can use conditional logic to return the right class
        return new StripePaymentService();
    }

    @Bean
    public OrderService orderService() {
        // Again, there could be conditional logic here.
        // Allowing us full control over bean creation.
        if (paymentGateway.equals("paypal")) {
            return new OrderService(paypal());
        } else {
            return new OrderService(stripe());
        }
    }


    @Bean
    public PaymentService paypal() {
        return new PaypalPaymentService();
    }
}
