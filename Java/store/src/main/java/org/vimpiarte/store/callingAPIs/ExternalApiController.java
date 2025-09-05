package org.vimpiarte.store.callingAPIs;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ExternalApiController {

    private ToDoJsonApiProxy api;

    public ExternalApiController(ToDoJsonApiProxy api) {
        this.api = api;
    }

    @GetMapping("/api/example/{id}")
    @ResponseBody
    public ToDo getExampleJson(@PathVariable Integer id) {
        return api.getToDo(id);
    }
}
