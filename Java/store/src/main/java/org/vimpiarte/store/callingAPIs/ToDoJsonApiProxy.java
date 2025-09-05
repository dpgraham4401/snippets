package org.vimpiarte.store.callingAPIs;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpHeaders;

import java.util.UUID;

@Component
public class ToDoJsonApiProxy {
    private final RestTemplate rest;

    @Value("${externalJson.service.url}")
    private String exampleJsonServiceUrl;

    public ToDoJsonApiProxy(RestTemplate rest) {
        this.rest = rest;
    }

    public ToDo getToDo(Integer toDoId) {
        String url = exampleJsonServiceUrl + "/todos/" + toDoId.toString();
        HttpHeaders headers = new HttpHeaders();
        headers.add("requestId", UUID.randomUUID().toString());

        HttpEntity<Void> entity = new HttpEntity<>(headers);

        // If we want to add something like Headers to our HTTP request, we need to drop back to 'exchange'
        // a little more verbose, but more control.
        // Note we need to pass the class to use a the response body ('ToDo.class')
        ResponseEntity<ToDo> response = rest.exchange(url, HttpMethod.GET, entity, ToDo.class);
        System.out.println(response.getStatusCode());
        return response.getBody();
    }

}
