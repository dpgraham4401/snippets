package org.vimpiarte.store.callingAPIs;

import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@EnableFeignClients
@Configuration
public class ProjectConfig {

    @Bean
    RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
