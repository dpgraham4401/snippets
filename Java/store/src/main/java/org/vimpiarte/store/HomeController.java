package org.vimpiarte.store;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.vimpiarte.store.services.OrderService;

@Controller
public class HomeController {
    @Value("${spring.application.name}")
    private String appName;

    private OrderService orderService;

    public HomeController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping("/")
    public String index() {
        orderService.placeOrder();
        System.out.println(appName);
        return "index.html";
    }

}
