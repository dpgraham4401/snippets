package org.vimpiarte.store;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.vimpiarte.store.basicBeans.OrderService;

@Controller
public class HomeController {

    private OrderService orderService;

    public HomeController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping("/")
    public String index() {
        orderService.placeOrder();
        return "index.html";
    }

}
