package org.vimpiarte.store;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.vimpiarte.store.dataAccess.models.Address;
import org.vimpiarte.store.dataAccess.models.Profile;
import org.vimpiarte.store.dataAccess.models.Tag;
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

        user.addTag("Tag 1");

        var profile = Profile.builder()
                .bio("bio")
                .build();
        user.setProfile(profile);
        profile.setUser(user);

        System.out.println(profile);
        System.out.println(user);
    }

}
