/**
 * Main.java
 * makes a request to the Pre-production Auth endpoint and prints the response to std out
 */
package org.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {
    public static void main(String[] args) {
        String baseURL = "https://rcrainfopreprod.epa.gov/rcrainfo/rest/api/v1/auth/";
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(baseURL + "/" + "myApiId" + "/" + "apiKey"))
                .build();
        client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
                .thenApply(HttpResponse::body)
                .thenAccept(System.out::println)
                .join();
    }
}