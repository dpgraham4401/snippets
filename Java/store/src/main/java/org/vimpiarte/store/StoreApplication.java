package org.vimpiarte.store;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.vimpiarte.store.dataAccess.models.Address;
import org.vimpiarte.store.dataAccess.models.User;

@SpringBootApplication
public class StoreApplication {

    public static void main(String[] args) {
        SpringApplication.run(StoreApplication.class, args);

        var user = User.builder()
                .name("John Doe")
                .email("dpgraham4401@gmail.com")
                .password("password")
                .build();

        var address = Address.builder()
                .street("street 123")
                .city("Dallas")
                .state("TX")
                .zip("12345")
                .build();

        user.addAddress(address);
        System.out.println(user);
    }

}
