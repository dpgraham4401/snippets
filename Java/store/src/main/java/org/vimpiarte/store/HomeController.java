package org.vimpiarte.store;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.vimpiarte.store.services.OrderService;

@Controller
public class HomeController {

    private OrderService orderService;

    public HomeController(OrderService orderService){
        this.orderService = orderService;
    }

    @Value("${spring.application.name}")
    private String appName;

    @GetMapping("/")
    public String index() {
        orderService.placeOrder();
        System.out.println(appName);
        return "index.html";
    }

}
